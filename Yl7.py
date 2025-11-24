# yl7
# Kirjuta programm, mis ütleb, kas kasutaja poolt etteantud täisarv on paarisarv või mitte. (paarisarvu mõiste - odd/even)

n = int(input("Sisesta täisarv: "))

if n % 2 == 0:
    print("Sinu arv on paarisarv:", n)
else:
    print("Sinu arv on paarituarv:", n)