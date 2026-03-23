a = 0b1100
b = 0b1010

print(a & b)
print(bin(a & b))

info = 0b1111_1111_1111_0000

data1 = 0b1100_0011_1010_0001
data2 = 0b1100_0011_1010_0010
data3 = 0b1100_0011_1010_1011
data4 = 0b1100_0011_1010_1100

print(bin(info&data1))
print(bin(info&data2))
print(bin(info&data3))
print(bin(info&data4))
print(bin(info))