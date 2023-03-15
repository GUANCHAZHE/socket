import  socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM)  as  s:
    s.bind(("0.0.0.0" ,1234))
    s.listen()
    c, addr = s.accept()
    with c:
        print('Connected by' , addr)
        while  True:
            #能接受的最大长度1024个
            data = c.recv(1024)
            if  not data:
                break
            c.sendall(data)


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
