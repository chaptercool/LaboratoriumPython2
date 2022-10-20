# Napisz skrypt działający jak prosty kalkulator, który potrafi dodawać, odejmować, mnożyć,
# dzielić oraz obliczać potęgę.
# Przykład: Jaką operację chcesz wykonać?
# 1) dodawanie
# 2) odejmowanie
# 3) mnożenie
# 4) dzielenie
# 5) potęgowanie
# Wpisz numer operacji: 2
# Podaj argument 1: 34
# Podaj argument 2: 5
# Wynik: 29

print("Jaką operację chcesz wykonać?")
print("1) dodawanie")
print("2) odejmowanie")
print("3) mnożenie")
print("4 dzielenie")
print("5) potęgowanie")

option = int(input("Podaj operacje:"))
a = int(input("Podaj argument 1: "))
b = int(input("Podaj argument 2:"))
if option == 1:
    wynik = a + b

elif option == 2:
    wynik =  a - b

elif option == 3:
    wynik = a * b

elif option == 4:
    if b == 0:
        print("Nie dziel przez 0!!!")
        exit()
    wynik =  a / b

elif option == 5:
    wynik =  a ** b

else:
    print("Podaj poprawna operacje!!!")
    exit()

print("Wynik: ", wynik)