from statistics import median, mean as avg
import xlrd

wb = xlrd.open_workbook("salaries.xlsx")
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])

max_median = (None, None)
rows = []
for i in range(1, 9):
    row = sh.row_values(i)
    rows.append(row)
    city, salaries = row[0], row[1:]
    medianed = median(salaries)
    if not max_median[1]:
        max_median = (city, medianed)
    elif max_median[1] < medianed:
        max_median = (city, medianed)

print(max_median[0], end=" ")
averages = dict()
for i in range(1, 7):
    jobs = sh.col_values(i)
    averages[jobs[0]] = avg(jobs[1:])

averaged = max(averages.values())
for k, v in averages.items():
    if v == averaged:
        print(k)
        break
