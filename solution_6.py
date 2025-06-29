# Задача 17 — Решение в Python

# Въвеждане на петцифрено число
n_text = input("Въведете петцифрено число: ")

# Подточка а) Брой на нечетните цифри
broi_nechetnite = 0

for cifra in n_text:
    if int(cifra) % 2 != 0:
        broi_nechetnite += 1

print("Брой на нечетните цифри:", broi_nechetnite)


# Подточка б) Сума на четните цифри
suma_chetnite = 0

for cifra in n_text:
    if int(cifra) % 2 == 0:
        suma_chetnite += int(cifra)

print("Сума на четните цифри:", suma_chetnite)
