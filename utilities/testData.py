from faker import Faker
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
fake = Faker()

print(fake.name())
# 'Lucy Cechtelar'

print(fake.address())

for i in range(1, 11):
    ws.cell(row=i, column=1).value = fake.name()

wb.save("testData.xlsx")
