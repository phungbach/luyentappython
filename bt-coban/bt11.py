'''11. Nhập từ file input {tên}, {tuổi hiện tại} và xuất ra file output theo mẫu (Có xử lý định dạng đầu vào)'''
'''sử dụng encode = utf8 để đọc và viết tiếng việt'''
'''FileNotFoundError trong trường hợp không tìm thấy file'''

try:
    with open('.\\bt-coban\\input_bt10.inp','r',encoding='utf8') as fileInp:
        ten = fileInp.readline().rstrip("\n")
        tuoi = int(fileInp.readline().rstrip("\n"))

    with open('.\\bt-coban\\output_bt10.out','w') as fileOut:
        stringsave = ('20 nam nua, tuoi cua {} se la {}'.format(ten, tuoi + 20))
        fileOut.write(stringsave.encode('utf8'))
except FileNotFoundError:
    print('không tìm thấy file')
except FileExistsError:
    print('file lỗi')
except:
    print('lỗi')