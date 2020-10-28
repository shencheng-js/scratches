import xlwt
import yaojian
from time import sleep
book = xlwt.Workbook()
sheet = book.add_sheet("化妆品信息")
index = 1

# for index1 in range(1,10,5):
    # sleep()
all_data_list=yaojian.getdata(1)
for i in all_data_list:
    sheet.write(index, 0, i['businessLicenseNumber'])
    sheet.write(index, 1, i['businessPerson'])
    sheet.write(index, 2, i['certStr'])
    sheet.write(index, 3, i['epsAddress'])
    sheet.write(index, 4, i['epsName'])
    sheet.write(index, 5, i['legalPerson'])
    index += 1

    # print(i)
book.save("test.xls")