'''12. Xuất file output trên 1 dòng từ chuỗi input bất kỳ nhập vào từ nhiều dòng'''

with open('.\\bt-coban\\input_bt10.inp','r',encoding='utf8') as fileInp:
    data = fileInp.readline()
    stringJoin = ' '.join(data).replace('/n', '')

fileOut = open(".\\bt-coban\\output_bt11,out", 'wb')
fileOut.write(stringJoin.encode('utf8'))