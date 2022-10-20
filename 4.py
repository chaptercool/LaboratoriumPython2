# Napisz skrypt, która zamienia wprowadzoną literę na przeciwną (co do wielkości) i wypisuje ją na ekranie
litera = input("Podaj literę zeby zamienic na przeciwną: ")
roznica = ord('a') - ord('A')
 if 'a' <= litera <= 'z' :
     print(chr(ord(litera) - roznica))
 elif 'A' <= litera <= 'Z' :
     nowa = ord(litera) + roznica
     znak = chr(nowa)
     print(znak)
else:
    print("to nie jest litera")