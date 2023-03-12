--------------------- kiến thức cơ bản -------------------------------

01. sử dụng encode = utf8 để đọc và viết tiếng việt

02. các trường hợp except:

        'FileNotFoundError' trong trường hợp không tìm thấy file
        'FileExistsError' file lỗi

03. 'with open' để mở file

        with open('.\\bt-coban\\input_bt10.inp','r',encoding='utf8') as fileInp:
            ten = fileInp.readline().rstrip("\n")
            tuoi = int(fileInp.readline().rstrip("\n"))
    
    'r' đọc file
    'w' ghi file
    'wb' ghi file encode

04. 'round' dùng để làm tròn số

        a = float(input('A = '))
        b = int(input('B = '))
        print(round(a, b))

05. 'split' dùng để cắt chuỗi, 'replace('/n', '')' là để thay thế chuỗi


06. có thể tạo 1 biến để open file:

        fileOut = open(".\\bt-coban\\output_bt11,out", 'wb')
        fileOut.write(stringJoin.encode('utf8'))

07. file output có thể được tạo ra bằng w hoặc wb


