'''09. Nhập & tính tổng dãy số nguyên bất kỳ cách nhau bởi khoảng trắng (Có xử lý ngoại lệ đầu vào).'''

try:
    day = input()
    daygiatri = day.split()
    danhsachso = map(int, daygiatri)
    tongdayso = sum(danhsachso)
    print("Tong cua danh so:", tongdayso)
except:
    pass
