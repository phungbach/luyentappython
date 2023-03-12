'''05. Nhập số bất kỳ ở hệ thập phân và hiển thị ra ở hệ bát phân.(Có xử lý ngoại lệ đầu vào)'''

giaTri = input()

try:
   soThapPhan = int(giaTri)

   print('So thap phan %d trong he bat phan la %o' % (soThapPhan, soThapPhan))

except:
   print("Dinh dang dau vao khong hop le!")