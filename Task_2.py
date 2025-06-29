# Задача 8 — Решение


# а)
print("а)")
a = 30
c = 7
d = a // c + 1      # Цяло деление, както в C++
b = a + a % c
print("d =", d)
print("b =", b)
print("----------------")


# б) Операции с деление и остатък
print("б)")
a = 40
b = 5
c = 3
print("a // b % c =", a // b % c)
print("a // (b % c) =", a // (b % c))
print("----------------")


# в) Работа с инкременти
print("в)")
a = 2
c = 11


b = c + a

print("b =", b)
print("a =", a)

b = c + a
c += 1
print("b =", b)
print("c =", c)
print("----------------")


# г) Работа със символи и ASCII кодове
print("г)")
a = '8'
b = 3
b = ord(a) - b
print("b =", b)
a = chr(b)
print("a =", a)
