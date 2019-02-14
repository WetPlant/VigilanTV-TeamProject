# -*- coding: utf-8 -*-
import pytesseract
import PIL
import pandas as pd

capture_path = "C:/Users/Elite/Desktop/2차/"


for i in range(70,88):
    #img파일
    img_path = capture_path + "second (" + str(i) + ").jpg"
    fp = open(img_path, "rb")
    img = PIL.Image.open(fp)
    #박스 생성하기
    txt = pytesseract.image_to_boxes(img, lang="52font+1499")
    print("ocr 결과 : " + txt)
    print('index' + str(i))
    f = open(capture_path + 'second ('+ str(i) + ').box', 'w', encoding='utf-8')
    f.write(txt+ '\n')

f.close()