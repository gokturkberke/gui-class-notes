from openpyxl import load_workbook

# Load the workbook from an Excel file
wb = load_workbook("student_list.xlsx")

# Get the reference of the active (first) worksheet
ws1 = wb.active

# "A2:C5" aralığındaki hücreleri alır. Bu, A2'den C5'e kadar olan hücreleri içerir.
output = "" # Hücre değerlerini depolamak için bir çıktı değişkeni
data = ws1["A2:C5"]
for row in data:
    for cell in row:
        output += str(cell.value) + "\t" # Hücre değerini string'e çevirip `output` stringine ekler. Tab karakteriyle (`\t`) hücreler arasına boşluk bırakır.
    output += "\n" #her satir sonunda yeni bir satir karakteri ekler

print(output)
