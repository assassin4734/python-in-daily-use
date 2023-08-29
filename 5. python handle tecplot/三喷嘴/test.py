import xlwings as xw    
app = xw.App(visible=True, add_book=False)
wb = app.books.add()
sht = wb.sheets.active
sht[0,0].value = 0