'''08. Nhập & tính tổng dãy số nguyên bất kỳ cách nhau bởi khoảng trắng.'''

day = input()
daygiatri = day.split()
danhsachso = map(int, daygiatri)
tongdayso = sum(danhsachso)
print("Tong cua danh so:", tongdayso)