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


url = "https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx"

file_name = "trekking2.xlsx"
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

summary = ProductInfo(0, 0, 0, 0)

layout = wb.sheet_by_name("Раскладка")

info = [layout.row_values(i) for i in range(1, layout.nrows)]
product_need: dict[str, float] = dict()


# Dealing with duplicates
for item in info:
    if item[0] in product_need:
        product_need[item[0]] += item[1] / 100
    else:
        product_need[item[0]] = item[1] / 100

answer = [guide[k] * v for k, v in product_need.items()]

for info in answer:
    summary += info
print(summary)
