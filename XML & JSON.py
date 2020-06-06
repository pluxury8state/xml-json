import json

from collections import Counter


def sort_and_conclusion(ob):
    p = 10

    new_mas = (Counter(ob))             # подсчитываем слова

    sorted_mas = list(dict(new_mas).items())

    sorted_mas.sort(key = lambda x: x[1],reverse=True)   #сортируем по значениям

    p = 10

    for items in sorted_mas:
        if p != 0:
            print(items)
            p -= 1
        else:
            break


def import_file_and_checking(file):#функция добавляет каждое слово в массив, разделяя
                                # их запятыми и проверяет их на длину не больше чем 6 символов
    mas = []

    #заполнение массива

    for descr in file['rss']['channel']['items']:

        mas.append(descr['description'].split(' '))   #получился массив в массиве

    return  mas


def check_for_XML(mas):
    mas2 = []


    for temp in mas:

        if len(temp) > 6:
            mas2.append(temp.lower())

    return mas2



def check_for_JSON(mas):

    mas2 = []
    for massive in mas:

        for temp in massive:

            if len(temp) > 6:
                mas2.append(temp.lower())

    return mas2



#begin XML
import xml.etree.ElementTree as ET
parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
describe = []
root = tree.getroot()


xml_items = root.findall("channel/item")

for item in xml_items:
   des = item.find("description")
   describe += des.text.split(" ")

sort_and_conclusion(check_for_XML(describe))



# Здравствуйте - проблема связана с тем, что он почему-то
# красным подчеркивает посленюю строчку кода,пожалуйста объясните в ответном письме, что не так

#begin JSON

with open('newsafr.json','r',encoding='utf-8') as f:


    file = json.load(f)

print("JSON:")
sort_and_conclusion(check_for_JSON((import_file_and_checking(file)))