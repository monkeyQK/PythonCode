import socket

socket.setdefaulttimeout(0.5)

remote_ip = "192.168.1.234"

try:
    port_list = [21, 445]
    for port in port_list:
        s = socket.socket()
        res = s.connect_ex((remote_ip, port))
        if res == 0:
            try:
                s.send('123456'.encode())
                banner = s.recv(1024).decode()
                s.close()
                pass
            except Exception as e:
                print("port {}".format(port))
                print(e)
            else:
                print("Port in {} Banner: {}".format(port, banner))
except Exception as e:
    print("2")
    print(e)


# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.settimeout(2)

# s.connect(("192.168.1.234", 21))
# s.send("banner".encode())
# banner = s.recv(1024).decode()

# print(banner)
