'''Tính tổng hai số nguyên bất kỳ (Có xử lý ngoại lệ đầu vào).'''


try:
    n = int(input("Nhập n: "))
    m = int(input("Nhập m: "))
    print("Tổng 2 số là: ",n+m)
except:
    print("sai định dạng")