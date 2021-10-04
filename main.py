def get_base_2(n: str) -> str:
    '''
    Transforma un numar dat din baza 10 in baza 2.
    :param n: numar in baza 10
    :return: x=numarul in baza 2
    '''
    resturi_n=[]
    x=0
    while n != 0:
        resturi_n.append(n % 2)
        n=n//2
    lungime=len(resturi_n)
    for i in range (lungime-1, -1, -1):
        x = x*10 + resturi_n[i]
    return x
def test_get_base_2():
    assert get_base_2(123) == 1111011
    assert get_base_2(75) == 1001011

def is_antipalindrome(n) -> bool:
    '''
    Determina daca un numar este antipalindrom
    :param n: numarul intreg
    :return: Returneaza True daca numarul este antipalindrom si False daca nu.
    '''
    cifren = []
    n1 = n
    while n > 0:
        cifren.append(n % 10)
        n = n // 10
    l = len(cifren)
    for i in range(0, l // 2):
        if cifren[i] == cifren[l - 1 - i]:
            return False
    return True

def test_is_antipalindrome():
    assert is_antipalindrome(1111) is False
    assert is_antipalindrome(15754) is False
    assert is_antipalindrome(5) is True

def main():
    while True:
        print("7. Determină dacă un număr este antipalindrom: un număr este antipalindrom dacă oricare două cifre egal depărtate de extremități sunt diferite (excepție făcând cifra din mijloc dacă avem un număr impar de cifre). De exemplu: 2783 este antipalindrom, iar 2773 nu este.")
        print("8. Transformă un număr dat din baza 10 în baza 2. Numărul se dă în baza 10.")
        print("x. Iesire din program - exit.")
        optiune = input("Alege optiunea: ")
        if optiune == "7":
            n = int(input("Cititi numarul: "))
            print(is_antipalindrome(n))
        elif optiune == "8":
            n = int(input("Cititi numarul: "))
            print(get_base_2(n))
        elif optiune == "x":
            break
        else:
            print("Optiune invalida.")

test_is_antipalindrome()
test_get_base_2()
main()



