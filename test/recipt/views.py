from django.shortcuts import render
from .models import Recipt, Budget
# Category, Product
import json
# Create your views here.
from django.http import JsonResponse, HttpResponse

def get_budget(request): #총 예산관리
    if request.method == 'POST':
        device_id = request.POST.get('device_id')
        living_expenses = request.POST.get('living_expenses')
        budget = Budget.objects.create(device_id=device_id, living_expenses=living_expenses)
        budget.save()
        return JsonResponse({'device_id': budget.device_id, 'living_expenses': budget.living_expenses})
    if request.method == 'UPDATE':
        device_id = request.UPDATE.get('device_id')
        living_expenses = request.UPDATE.get('living_expenses')
        budget = Budget.objects.get(device_id=device_id)
        budget.living_expenses = living_expenses
        budget.save()
        return JsonResponse({'device_id': budget.device_id, 'living_expenses': budget.living_expenses})

    if request.method == 'GET':
        device_id = request.GET.get('device_id')
        budget = Budget.objects.get(device_id=device_id)
        if budget:
            # Budget.objects.first().living_expenses -= amount  # 총 지출 금액에 앱에서 받아온 금액을 더함
            # Budget.living_expenses.save()  # 변경사항을 저장
            return JsonResponse({'device_id': budget.device_id, 'living_expenses': budget.living_expenses})
        else:
            return JsonResponse({'message': 'Not found device id'})
            # Budget.objects.create(total_spending=int(amount))  # Budget 객체 생성
        # return JsonResponse({'message': 'Budget updated successfully.'})

    # return JsonResponse({'budget': budget.living_expenses})

# response_data['list'][0]

def get_recipt(request): #ios로부터 영수증 json 데이터 받기
    if request.method == 'POST':
        data = json.loads(request.body.decode('UTF-8'))
        # 카테고리
        # data['category'] = parse_category(data)
        # recipt = Recipt.objects.create(device_id=1, category=parse_category(data), year=2022, month=8, store="홈플러스",
        #                                address="울산광역시 남구 수암로 148", amount=10600)

        recipt = Recipt.objects.create(data)

        # products_data = data['list']
        # products_data = [{'name': '푸주', 'amount': 1, 'price': 500}, {'name': '두부', 'amount': 2, 'price': 750}]

        # for product_data in products_data:
        #     Product.objects.create(recipt=recipt, **product_data)

        budget = Budget.objects.get(device_id=recipt.device_id)


        if (budget.living_expenses < recipt.amount):
            return JsonResponse({'message': 'exceed living expenses'})
        else:
            # 생활비 예산에서
            budget.living_expenses -= recipt.amount
            recipt.save()
            budget.save()
            return JsonResponse({'message': 'good~ job~'})

    if request.method == 'GET':
        device_id = request.GET.get('device_id')
        # year = request.GET.get('year')
        # month = request.GET.get('month')
        print("device_id : ", device_id)
        # recepts = Recipt.objects.filter(device_id=device_id, year=year, month=month)
        recepts = Recipt.objects.filter(device_id=device_id)
        recept_json = []
        # recept_sum = 0
        for r in recepts:
            print(r.list)
            recept_json.append({
                "store": r.store,
                # "category": r.category.name,
                "address": r.address,
                #"list": json.dumps(r.objects.all()),
                "amount": r.amount,
                # "year": r.year,
                # "month": r.month,
            })
        return JsonResponse({"result": recept_json})


def parse_category(data):
    # print(data)
    category_name = data["category"]
    # print(category_name)
    category = Category.objects.get(name=category_name)
    return category

def parse_list(recipt, product_list):
    new_list = []
    for i in range(len(product_list)):
        product = product_list[i]
        new_list.append(Product.objects.create(recipt=recipt, **product))
    return new_list
