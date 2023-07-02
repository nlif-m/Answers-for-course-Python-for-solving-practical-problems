"""
Главный бухгалтер компании "Рога и копыта" случайно удалил ведомость с начисленной зарплатой. К счастью, у него сохранились расчётные листки всех сотрудников. Помогите по этим расчётным листкам восстановить зарплатную ведомость. Архив с расчётными листками доступен по ссылке https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip (вы можете скачать и распаковать его вручную или самостоятельно научиться делать это с помощью скрипта на Питоне).

Ведомость должна содержать 1000 строк, в каждой строке должно быть указано ФИО сотрудника и, через пробел, его зарплата. Сотрудники должны быть упорядочены по алфавиту.
"""

from pathlib import Path
from urllib.request import urlretrieve
from zipfile import ZipFile

import xlrd


class Employee:
    def __init__(self, xlsx_path: Path):
        wb = xlrd.open_workbook(xlsx_path)
        sh = wb.sheet_by_name(wb.sheet_names()[0])
        _, name, _, salary = sh.row_values(1)
        self.name: str = str(name)
        self.salary: int = int(salary)


result_file_name = "2.4.2_result.txt"
file_name = "rogaikopyta.zip"
url = f"https://stepik.org/media/attachments/lesson/245299/{file_name}"

path = Path(file_name)
if not path.exists():
    urlretrieve(url, file_name)

folder_name = "payslips"
folder_path = Path(folder_name)
if not folder_path.exists():
    with ZipFile(path) as f:
        f.extractall(folder_name)

payslips = Path(folder_name)


workers = sorted(
    [Employee(f.absolute()) for f in payslips.iterdir()], key=lambda worker: worker.name
)

statement = "\n".join(f"{worker.name} {worker.salary}" for worker in workers)

with open(result_file_name, "w") as f:
    f.write(statement)
