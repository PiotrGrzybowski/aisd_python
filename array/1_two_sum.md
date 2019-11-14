# Two sum
Napisz funkcję, która przyjmuje jako wejście listę liczb całkowitych oraz liczbę będącą celem, a zwraca indeksy takich dwóch liczb z listy, które sumują się one do podanej konkretnej wartości.

Możesz założyć, że każde wejście będzie miało dokładnie jedno rozwiązanie i nie możesz używać tego samego elementu dwa razy.

## Przykład
Podane: values = [2, 7, 11, 15], target = 13,

Ponieważ values[0] + values[2] = 2 + 11 = 13,
funkcja powinna zwrócić [0, 1].

## Rozwiązanie
### Sposób 1: Brute force
Podejście brute-force jest proste. Przejdź przez każdy element *x* i znajdź, czy istnieje inna wartość, która równa się *target - x*

**Złożoność obliczeniowa**: O(n^2). Dla każdego elementu próbujemy znaleźć próbujemy znaleźć odpowienią wartość przechodząc do końća całą tablicę co ma złożoność O(n), więc końcową złożonością jest kwadratowa.
**Złożoność pamięciowa**: O(1)

```python
def two_sum_1(values: List[int], target: int) -> Tuple[int, int]:
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[j] == target - values[i]:
                return i, j

    return -1, -1


print(two_sum_1([2, 7, 11, 15], 13))
```

### Sposób 2: Two pass Hash Table
Aby Usprawnić nasz algorytm, potrzebujemy bardziej efektywnego sposobu sprawdzania czy uzupełnienie dla konkretnej liczby istnieje na liście.
Jeżeli uzupełnienie istnieje, to musimy odnaleźć jej indeks. Jaki jest najlepszy sposób na utrzymanie mapowania każdego elementu tablicy do jej indeksu? tablica Hashująca.

Możemy zredukować czas wyszukiwania uzupenienia z O(n) do O(1) wymieniając pamięć za szybkość. Jak już wiemy tablica hashująca umożliwia nam odczyt wartości w czasie stałym.

Algorytm będzie następujący: 
 - W pierwszej iteracji zbuduj tablicę hashującą gdzie klucze będa wartościamiznajdującymi się na liście liczb a kluczami będą ich indeksy.
 - W drugiej pętli dla każdej liczby z listy sprawdzamy czy uzupełnienie występuje w tablicy hashującej (target - values[i]). Nalezy jednak sprawdzić warunek tej samej wartości!
 
 ```python
def two_sum_2(values: List[int], target: int) -> Tuple[int, int]:
    mapping = {value: i for i, value in enumerate(values)}

    for i, value in enumerate(values):
        complement = target - value
        if complement in mapping and mapping[complement] != i:
            return i, mapping[complement]

    return -1, -1


print(two_sum_1([2, 7, 11, 15], 13))
```

**Złożoność obliczeniowa**: O(n). Dwukrotnie przechodzimy tablicę n razy więc złożoność liniowa.
**Złożoność pamięciowa**: O(n) potrzebujemy dodatkowej pamięci na słownik mapujący wartości do indeksów.

### Sposób 3: One pass Hash Table
Możemy jeszcze bardziej usprawnić poprzednie podejście poprzez jednokrotne przejście przez listę liczb i budowanie tablicy hashującej w trakcie przechodzenia.
 ```python
def two_sum_3(values: List[int], target: int) -> Tuple[int, int]:
    mapping = {}

    for i, value in enumerate(values):
        complement = target - value
        if complement in mapping and mapping[complement] != i:
            return mapping[complement], i
        mapping[value] = i

    return -1, -1


print(two_sum_1([2, 7, 11, 15], 13))
```

**Złożoność obliczeniowa**: O(n). Dwukrotnie przechodzimy tablicę n razy więc złożoność liniowa.
**Złożoność pamięciowa**: O(n) potrzebujemy dodatkowej pamięci na słownik mapujący wartości do indeksów.

