from openpyxl import load_workbook #Bu fonksiyon, mevcut bir Excel dosyasını yüklemek için kullanılır.


# Load the workbook from an Excel file
wb = load_workbook("student_list.xlsx")

# Get the reference of the active (first) worksheet
ws1 = wb.active

# Get the entire column (Column A)
col = ws1["A"]
for cell in col:
    # Her hücrenin değerini (içeriğini) yazdırır
    print(cell.value)

# Get the entire row (Row 1)
row = ws1["1"]
for cell in row:
    print(cell.value)
