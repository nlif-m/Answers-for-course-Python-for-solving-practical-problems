"""
Васю назначили завхозом в туристической группе и он подошёл к
подготовке ответственно, составив справочник продуктов с указанием
калорийности на 100 грамм, а также содержание белков, жиров и
углеводов на 100 грамм продукта. Ему не удалось найти всю информацию,
поэтому некоторые ячейки остались незаполненными (можно считать их
значение равным нулю). Также он использовал какой-то странный офисный
пакет и разделял целую и дробную часть чисел запятой. Таблица доступна
по ссылке
https://stepik.org/media/attachments/lesson/245290/trekking3.xlsx

Вася составил раскладку по продуктам на весь поход (она на листе
"Раскладка") с указанием номера дня, названия продукта и его
количества в граммах. Для каждого дня посчитайте 4 числа: суммарную
калорийность и граммы белков, жиров и углеводов. Числа округлите до
целых вниз и введите через пробел. Информация о каждом дне должна
выводиться в отдельной строке.
"""

from urllib.request import urlretrieve
import pathlib
from math import floor
from dataclasses import dataclass


import xlrd


@dataclass
class ProductInfo:
    kilocalorie: float = 0
    proteins: float = 0
    fats: float = 0
    carbs: float = 0

    def __str__(self):
        return (
            f"{floor(self.kilocalorie)} {floor(self.proteins)} "
            f"{floor(self.fats)} {floor(self.carbs)}"
        )

    def __mul__(self, other):
        if isinstance(other, float):
            return ProductInfo(
                self.kilocalorie * other,
                self.proteins * other,
                self.fats * other,
                self.carbs * other,
            )
        elif isinstance(other, int):
            return self.__mul__(float(other))
        raise TypeError

    def __add__(self, other):
        if isinstance(other, ProductInfo):
            return ProductInfo(
                self.kilocalorie + other.kilocalorie,
                self.proteins + other.proteins,
                self.fats + other.fats,
                self.carbs + other.carbs,
            )
        raise TypeError


file_name = "trekking3.xlsx"

url = f"https://stepik.org/media/attachments/lesson/245290/{file_name}"

if not pathlib.Path(file_name).is_file():
    urlretrieve(url, file_name)

wb = xlrd.open_workbook(file_name)
reference = wb.sheet_by_name("Справочник")

guide: dict[str, ProductInfo] = dict()

info = [reference.row_values(i) for i in range(1, reference.nrows)]

for i in info:
    for index, j in enumerate(i):
        if j == "":
            i[index] = 0

for i in info:
    guide[i[0]] = ProductInfo(*i[1:])

summaries = ProductInfo(0, 0, 0, 0)

layout = wb.sheet_by_name("Раскладка")

days: dict[float, ProductInfo] = dict()

info = [layout.row_values(i) for i in range(1, layout.nrows)]
for row in info:
    day, product, weight = row
    if day not in days:
        days[day] = guide[product] * (weight / 100)
    else:
        days[day] += guide[product] * (weight / 100)


days = sorted(list(days.items()))
for day in days:
    print(day[1])
