'''07. Làm tròn số thập phân A đến B chữ số sau dấu phẩy (Có xử lý ngoại lệ đầu vào).'''

try:
    a = float(input('A = '))
    b = int(input('B = '))
    print(round(a, b))
except:
    pass