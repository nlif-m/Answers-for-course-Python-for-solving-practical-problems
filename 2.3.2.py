from urllib.request import urlretrieve
import xlrd

url = "https://stepik.org/media/attachments/lesson/245290/trekking1.xlsx"

urlretrieve(url, "trekking1.xlsx")
wb = xlrd.open_workbook("trekking1.xlsx")
sheet_names = wb.sheet_names()

sh = wb.sheet_by_name(sheet_names[0])

vals = [sh.row_values(row) for row in range(1, sh.nrows)]


results = [(val[0], val[1]) for val in vals]

results = sorted(results, key=lambda x: (-x[1], x[0]))
# results = [i[0] for i in results]

# pp = pprint.PrettyPrinter()
# pp.pprint(results)
print("\n".join([i[0] for i in results]))
