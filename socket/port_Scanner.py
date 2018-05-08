import socket
import threading

lock = threading.Lock()
openNum = 0
closeNum = 0
threads = []
port_open = []


def port_Scanner(ip, port):
    global openNum
    global closeNum
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        if result == 0:
            lock.acquire()
            openNum += 1
            # print("[+]{} open".format(port))
            port_open.append(port)
            lock.release()
        else:
            closeNum += 1
            # print("[-]{} close".format(port))
        s.close()
    except Exception as e:
        print(e)


def main():
    socket.setdefaulttimeout(10)
    target_host = "192.168.33.8"
    port_list = [i for i in range(1, 1000)]
    # port_list = [445, 80, 3389]
    for i in port_list:
        t = threading.Thread(target=port_Scanner, args=(target_host, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("[*] 扫描完成!")
    # print("[*] A total of %d open port" % (openNum))
    # print("[*] A total of %d close port" % (closeNum))
    print("{}该主机开放的端口是：{}".format(target_host, port_open))


if __name__ == '__main__':
    main()
