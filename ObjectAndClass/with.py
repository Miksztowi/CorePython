# -*- encoding:utf-8 -*-
# __author__=='Gan'
from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection(object):
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already Connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None
        # return True
        # if return True ,any exception will be hide.


if __name__ == '__main__':
    from functools import partial
    conn = LazyConnection(('www.python.org', 80))
    with conn as s:
        # with conn as b:
        #     print(b)
        # second connection will raise exception
        # conn.__enter__() executes: connection open
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))
        print(resp)
        # conn.__exit__() executes: connection closed
#不管 with 代码块中发生什么，上面的控制流都会执行完，就算代码块中发生了异常也是一样的。
# 事实上，__exit__() 方法的第三个参数包含了异常类型、异常值和追溯信息(如果有的话)。
# __exit__() 方法能自己决定怎样利用这个异常信息，或者忽略它并返回一个None值。
#  如果 __exit__() 返回 True ，那么异常会被清空，就好像什么都没发生一样， with 语句后面的程序继续在正常执行。


