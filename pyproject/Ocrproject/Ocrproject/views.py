import os

from django.http import JsonResponse
import uuid
import json
import time
import openai
import cv2
from django.conf import settings
from django import forms
from django.shortcuts import render, redirect
import requests
from django.http import JsonResponse, HttpResponse
from django.conf import settings
import json
openai.api_key = os.environ['OPENAI_API']
URL = "https://api.openai.com/v1/chat/completions"



def ocr_view(request):
    if request.method == "GET":
        response_data = {
            'store':"BBQ",
            'address': "대구 수성구 달구벌대로 2637 1층",
            # 'list': json.loads(list)['list'],
            # 'year': json.loads(year)['year'],
            # 'month': json.loads(month)['month'],
            'amount': 40000,
        }
        print(response_data)
        return JsonResponse(response_data)


def post_ocr(request): #가게 이름, 위치, 상품목록, 전체작업 앱에 주기
    if request.method == "GET":
        store = openai_api("store", request_ocr())
        address = openai_api("address", request_ocr())
        #list = openai_api("list", request_ocr())
        #year = openai_api("year", request_ocr())
        # month = openai_api("month", request_ocr())
        amount = openai_api("amount", request_ocr())

        response_data = {
            'store': json.loads(store)['store'],
            'address': json.loads(address)['address'],
            # 'list': json.loads(list)['list'],
            # 'year': json.loads(year)['year'],
            # 'month': json.loads(month)['month'],
            'amount': json.loads(amount)['amount'],
        }
        print(response_data)
        return JsonResponse(response_data)




# def post_pic(request): #앱에서 사진 받아오기
#     if request.method == "POST":
#         # ios에서 받은 이미지 바이너리
#         image_data = request.body
#
#          # 이미지 파일 데이터를 원하는 처리로 전달하고 결과를 받음
#          # 여기에서는 예시로 이미지 파일을 그대로 반환하는 것으로 가정합니다.
#         if image_data:
#              # 이미지 파일 데이터를 HttpResponse로 반환
#             response = HttpResponse(image_data, content_type='image/jpg')
#             handle_uploaded_file(image_data)
#             request_ocr()
#             return redirect('/api/ocr2')

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
def upload_file(request):
    if request.method == 'POST':
        response_data = {
            'message': "업로드 완료"
        }
        # form = UploadFileForm(request.POST, request.FILES)
        print(request.FILES)
        handle_uploaded_file(request.FILES['fileupload'])
        request_ocr()
        return redirect('/api/ocr2')

def handle_uploaded_file(f):
    with open('../test.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def request_ocr():
    api_url = 'https://8locpw2vhm.apigw.ntruss.com/custom/v1/23425/b139d913788d1fd2d29aca11565edaa7d6b191d2712fa39c4fece477e0d18884/general'
    secret_key = os.environ['NAVER_OCR_API']
    # files = post_pic
 # 로컬에서 불러온거니까
    path = '../test.jpg'
    files = [('file', open(path, 'rb'))]

    request_json = {'images': [{'format': 'jpg',
                                'name': 'demo'
                                }],
                    'requestId': str(uuid.uuid4()),
                    'version': 'V2',
                    'timestamp': int(round(time.time() * 1000))
                    }

    payload = {'message': json.dumps(request_json).encode('UTF-8')}

    headers = {
        'X-OCR-SECRET': secret_key,
    }

    response = requests.request("POST", api_url, headers=headers, data=payload, files=files)
    result = response.json()

    # img = cv2.imread(path)
    # roi_img = img.copy()
    a_list = []
    for field in result['images'][0]['fields']:
        text = field['inferText']
        # decoded_str = bytes(text, 'utf-8').decode('unicode-escape')
        a_list.append(text)
        # vertices_list = field['boundingPoly']['vertices']
    return "\t".join(a_list)
def openai_api(a, text):
    if(a == "month") :
        message = "이 텍스트중 날짜에서 몇월인지를 json 형식과 MM형식으로 알려줘,key는 month 로 잡아줘\n" + text
    # elif (a == "year"):
    #     message = "이 텍스트중 날짜에서 연도를 json 형식과 yyyy형식으로 알려줘,key는 year 로 잡아줘\n" + text
    elif (a == "store"):
        message = "이 텍스트에서 영업장 이름을 json 형식으로 알려줘, 영업장 값이 있다면 key는 store 로 잡아줘\n" + text
    elif (a == "address"):
        message = "이 텍스트에서 영업장의 주소를 json 형식으로 알려줘, 주소 값이 있다면 key는 address 로 잡아줘\n" + text
    # elif (a == "list"):
    #     message = "이 텍스트에서 상품 목록을 json 형식으로 알려줘. 상품명과 수량과 금액이 나와있는 목록으로 부탁해. key값은 list로 설정해줘.\n" + text
    elif (a == "amount"):
        message = "이 텍스트에서 총 금액을 json 형식으로 알려줘, 총합 값이 있다면 key는 amount 로 잡아줘\n" + text

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": f"{message}"}],
        "temperature": 1.0,
        "top_p": 1.0,
        "n": 1,
        "stream": False,
        "presence_penalty": 0,
        "frequency_penalty": 0,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai.api_key}"
    }

    response = requests.post(URL, headers=headers, json=payload, stream=False)

    resp = json.loads(response.content)
    # pprint(resp)
    # print(message)
    file_path = 'receipt.json'
    with open(file_path, 'w') as f:
        json.dump(resp, f, ensure_ascii=False)

    return resp['choices'][0]['message']['content']



