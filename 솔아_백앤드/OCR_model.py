import pytesseract
import cv2
import matplotlib.pyplot as plt
import subprocess

path = f'image4.jpg'
output_file_path = "output.txt"
image_sample = cv2.imread(path)
image_gray = cv2.cvtColor(image_sample, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(image_gray, lang='kor+eng')
with open(output_file_path, "w", encoding="utf-8") as file:
    file.write(text)