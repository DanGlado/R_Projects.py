def Factr(n, f=1): # Перестановки без повторений
    for i in range(1, n+1):
        f *= i
    return f

# print(Factr(5))

def Chislkomb(n, k): # Сочетания бп
    return Factr(n)/(Factr(k)*Factr(n-k))


def Chislkomba(n, k): # Сочетания сп
    return Factr(n+k-1)/(Factr(k)*Factr(n-1))


def Perest(n, k): # Размещения бп
    return Factr(n)/Factr(n-k)


def Peresta(n, k): # Размещения сп
    return n**k


def Multinom(n, *groups): # Перестановки бп
    znamenatel = 1
    for group in groups:
        znamenatel *= Factr(group)
    return Factr(n)/znamenatel

# Решение задач 19-21
print("Выберите формулу расчета, введите номер:")
print("1) Сочетания без повторений\n"
      "(выбираются из n-различных элементов"
      "по k-элементов и отличаются "
      "друг от друга хотя бы одним элементом)")
print("2) Сочетания с повторениями\n"
      "(выбираются из n-различных элементов по k-элементов "
      "и отличаются друг от друга хотя бы одним элементом"
      "или числом вхождений одного и того-же элемента)")
print("3) Размещения без повторений\n"
      "(выбираются из n-различных элементов по k-элементов "
      "и отличаются друг от "
      "друга порядком или составом элементов)")
print("4) Размещения с повторениями\n"
      "(выбираются из n-повторяющихся элементов по k-элементов "
      "и отличаются друг от "
      "друга порядком или составом элементов)")
print("5) Перестановки без повторений\n"
      "(составленны из n=k -различных элементов и отличаются "
      "друг от друга порядком размещения)")
print("6) Перестановки с повторениями\n"
      "(составленны из n=k -частично повторяющихся элементов и отличаются "
      "друг от друга порядком размещения)")

number = input()
while number != 0:
    if number == '1':
        n = int(input("Введите n: "))
        k = int(input("Введите k: "))
        print(Chislkomb(n, k))
        break
    elif number == '2':
        n = int(input("Введите n: "))
        k = int(input("Введите k: "))
        print(Chislkomba(n, k))
        break
    elif number == '3':
        n = int(input("Введите n: "))
        k = int(input("Введите k: "))
        print(Perest(n, k))
        break
    elif number == '4':
        n = int(input("Введите n: "))
        k = int(input("Введите k: "))
        print(Peresta(n, k))
        break
    elif number == '5':
        n = int(input("Введите n: "))
        print(Factr(n, f=1))
        break
    elif number == '6':
        n = int(input("Введите n: "))
        print("Введите группы, в конце -1")
        g = int(input())
        groups = []
        while g != -1:
            groups.append(g)
            g = int(input())
        print(Multinom(n, *groups))
        break
    else:
        print("Выбор не является корректным, повторите попытку")
        number = input()
input()