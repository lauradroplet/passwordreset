
password = 'a123456'
i = 1
while i <= 3:
    pw = input('请输入密码：')
    if pw == password:
        print('登入成功')
        break
    else:
        if i == 3:
            print('密码错误')
        else:
            print('密码错误！还有',3-i,'次机会')

    i = i+1

