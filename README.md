# Laborator 2, săptămâna 2

Predați rezolvările în săptămâna 2 într-un fișier `main.py` comis în repository-ul vostru de pe github. 

Fiecare student primește 2 probleme. 

Scrieți doar funcțiile aferente problemelor pe care le rezolvați. 

**Funcțiile trebuie să aibă denumirile date în enunț și să fie specificate.**

Trebuie să aveți o interfață cu utilizatorul care permite introducerea datelor până la introducerea unei comenzi care oprește aplicația. Aplicația nu se va opri decât atunci când utilizatorul dorește acest lucru. Nu este necesar să validați datele citite de la utilizator.

Scrieți un program care:

1. Găsește ultimul număr prim mai mic decât un număr dat.
    - Funcția principală: `get_largest_prime_below(n)`
    - Funcția de test: `test_get_largest_prime_below()`

2. Se dă data nașterii în formatul `DD/MM/YYYY`. Determinați vârsta persoanei în zile.
    - Funcția principală: `get_age_in_days(birthday) -> int`
    - Funcția de test: `test_get_age_in_days()`
     
3. Dându-se numărul natural `n`, determină numerele prime `p1` si `p2` astfel încât `n = p1 + p2` (verificarea conjecturii lui Goldbach), `p1` minim și `p2` maxim. Pentru ce fel de `n` există soluție? 
    - Funcția principală: `get_goldbach(n) -> Optional[(int, int)]`
    - Funcția de test: `test_get_goldbach()`
     
4. Execută un număr dat de pași pentru a calcula radicalul unui număr dat folosind metoda lui Newton cu `x0=2` și afișează aproximarea obținută.
    - Funcția principală: `get_newton_sqrt(n, steps) -> float`
    - Funcția de test: `test_get_newton_sqrt()`
    
5. Determină dacă un număr dat este palindrom.
    - Funcția principală: `is_palindrome(n) -> bool`
    - Funcția de test: `test_is_palindrome()`

6. Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime. De exemplu, `233` este superprim, deoarece `2`, `23` și `233` sunt toate prime, dar `237` nu este superprim, deoarece `237` nu este prim. 
    - Funcția principală: `is_superprime(n) -> bool`
    - Funcția de test: `test_is_superprime()`

	
7. Determină dacă un număr este antipalindrom: un număr este antipalindrom dacă oricare două cifre egal depărtate de extremități sunt diferite (excepție făcând cifra din mijloc dacă avem un număr impar de cifre). De exemplu: `2783` este antipalindrom, iar `2773` nu este.
    - Funcția principală: `is_antipalindrome(n) -> bool`
    - Funcția de test: `test_is_antipalindrome()`

8. Transformă un număr dat din baza `10` în baza `2`. Numărul se dă în baza `10`.
    - Funcția principală: `get_base_2(n: str) -> str`
    - Funcția de test: `test_get_base_2()`

9. Transformă un număr dat din baza `2` în baza `16`. Numărul se dă în baza `2`.
    - Funcția principală: `get_base_16_from_2(n: str) -> str`
    - Funcția de test: `test_get_base_16_from_2()`

10. Calculează combinări de `n` luate câte `k` (`n` și `k` date).
    - Funcția principală: `get_n_choose_k(n: int, k: int) -> int`
    - Funcția de test: `test_get_n_choose_k()`

11. Afișează toți anii bisecți între doi ani dați (inclusiv anii dați).
    - Funcția principală: `get_leap_years(start: int, end: int) -> list[int]`
    - Funcția de test: `test_get_leap_years()`


12. Afișează toate pătratele perfecte dintr-un interval închis dat.
    - Funcția principală: `get_perfect_squares(start: int, end: int) -> list[int]`
    - Funcția de test: `test_get_perfect_squares()`

13. Transformă o temperatură dată într-o scară dată (`K`, `F` sau `C`) într-o altă scară dată. De exemplu: `300 K C` -> `26.85`.
    - Funcția principală: `get_temp(temp: float, from: str, to: str) -> float`
    - Funcția de test: `test_get_temp()`

14. Calculează CMMMC al `n` numere date.
    - Funcția principală: `get_cmmmc(numbers: list[int]) -> int`
    - Funcția de test: `test_get_cmmmc()`
