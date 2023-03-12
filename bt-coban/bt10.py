'''10. Nhập từ file input {tên}, {tuổi hiện tại} và xuất ra file output theo mẫu'''

'''Vao 20 nam nua, tuoi cua John se la 30'''

'''rstrip loại bỏ ký tự xuống dòng'''

with open('.\\bt-coban\\input_bt10.inp','r') as fileInp:
    ten = fileInp.readline().rstrip("\n")
    tuoi = int(fileInp.readline().rstrip("\n"))

with open('.\\bt-coban\\output_bt10.out','w') as fileOut:
    fileOut.write('20 nam nua, tuoi cua {} se la {}'.format(ten, tuoi + 20))