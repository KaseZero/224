import xlrd
class Table():
     def uio(self,filename,sheetname):
         wb=xlrd.open_workbook(filename)
         sheet=wb.sheet_by_name(sheetname)
         List=[]
         for i in range(1,sheet.nrows):
             a=sheet.row_values(0)
             b=sheet.row_values(i)
             List.append(dict(zip(a,b)))
         return List
     def tyu(self,ab,url):
         for data in ab:
             if url == data['url']:
                 return data
if __name__=='__main__':
    web=Table()
    q=web.uio('tar.xlsx', 'Sheet1')
    print(q)
    print(web.tyu(q, '192.168.55.2'))