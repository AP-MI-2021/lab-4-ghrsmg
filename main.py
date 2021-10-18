def citire():
    l = []
    givenString = input("Dati lista, cu elementele separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l


def eliminare_duplicate(l):
    '''functia foloseste doua for-uri pentru a compara pe rand fiecare elemenet cu toate elementele din lista
     daca sunt egale il elimina din lista
     apoi returneaza lista noua'''
    rezultat = []
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] == l[j]:
                rezultat.append(l[i])
    return rezultat


def test_eliminare_duplicate():
    assert eliminare_duplicate([15, 15, 10, 11, 12]) == [15, 10, 11, 12]
    assert eliminare_duplicate([1, 1, 1, 2, 2, 3, 4, 5, 5]) == [1, 2, 3, 4, 5]


def suma_primelor_n_pozitive(l, n):
    '''functia calculeaza in s suma numerelor pozitive si for-ul se opreste atunci cand n are valoarea 0'''
    s = 0
    for x in l:
        if x >= 0 and n != 0:
            s = s + x
            n = n - 1
    return s


def test_suma_primelor_n_pozitive():
    assert suma_primelor_n_pozitive([1, -1, 2, -2, 3, 4], 3) == 6


def verif_pozitive_cresc(l):
    '''functia salveaza in cl numerele pozitive in ordine
       apoi verifica daca numerele din cl sunt crescatoare returnand True/False'''
    cl = []
    for x in l:
        if x >= 0:
            cl.append(x)
    for i in range(1, len(cl), 1):
        if l[i] > l[i + 1]:
            return False
        return True
def test_verif_pozitive_cresc():
    assert verif_pozitive_cresc([1, 2, 1]) is False
    assert verif_pozitive_cresc([1, -1, 2 , 3]) is True





def main():
    test_verif_pozitive_cresc()
    test_suma_primelor_n_pozitive()
    while True:
        print("1. Citire lista")
        print("2. Afisare lista dupa eliminarea duplicatelor")
        print("3. Afisarea sumei primelor n numere pozitive din lista")
        print("4. Sa se afiseze daca toate numerele pozitive sunt ordonate crescator")
        print("5. Sa se afiseze lista obtinuta dupa procesare")
        print("x. Iesire")
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citire()
        elif optiune == "2":
            print(eliminare_duplicate(l))
        elif optiune == "3":
            n = int(input("Dati un nr: "))
            print(suma_primelor_n_pozitive(l, n))
        elif optiune == "4":
            if verif_pozitive_cresc(l):
                print("DA")
            else: print("NU")
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")


main()
