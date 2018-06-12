from xlwt import Workbook


def list2xls(li, xls_name):
    workbook = Workbook()
    sheet = workbook.add_sheet('sheet1')
    row = 0
    for lines in li:
        cols = 0
        for i in lines:
            sheet.write(row, cols, i)
            cols += 1
        row += 1
    workbook.save(r'{}.xls'.format(xls_name))


def main():
    li = [["id", "name", "aas"], ["001", "张三"]]
    list2xls(li)


if __name__ == '__main__':
    main()
