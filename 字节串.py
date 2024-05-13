b1 = bytes()
b2 = b''
b3 = b'https://c.baicheng.net/python/'
print("b3:",b3)
print(b3[3])
print(b3[7:22])
b4 = bytes('中国共产党成立100周年了‘, encoding='UTF-8')
print("b4:", b4)
b5 = "坚决拥护中国共产党的领导".encode('UTF-8')
print("b5:", b5)