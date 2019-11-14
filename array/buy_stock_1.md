#  Best Time to Buy and Sell Stock
Na wejściu otrzymujesz listę liczb, gdzie i-ty element reprezentuje cenę akcji i-tego dnia.

Jeśli pozwolono Ci przeprowadzić co najwyżej jedną transakcję (tj. kupić jedną i sprzedać jedną akcję), zaprojektuj algorytm, aby znaleźć maksymalny zysk.

Należy pamiętać, że nie można sprzedać akcji przed ich zakupem.

## Przykład 1
Dane wejściowe: [7,1,5,3,6,4]

Wyjście: 5

Wyjaśnienie: Kup w 2. dniu (cena = 1) i sprzedaj w 5. dniu (cena = 6), zysk = 6-1 = 5.

             Nie 7-1 = 6, ponieważ cena sprzedaży musi być większa niż cena kupna.
             

## Przykład 2
Dane wejściowe: [7,6,4,3,1]

Wyjście: 0

Wyjaśnienie: W tym przypadku nie jest przeprowadzana żadna transakcja, tzn. maksymalny zysk = 0.


## Rozwiązanie
Musimy znaleźć maksymalną różnicę (która będzie maksymalnym zyskiem) pomiędzy dwiema liczbami w danej tablicy. Ponadto druga liczba (cena sprzedaży) musi być większa niż pierwsza (cena kupna).

Formalnie, musimy znaleźć max(prices[j] - prices[i]), dla każdego *i* i *j* takie, że j>i.


### Sposób 1: Brute force
```python
from typing import List
def max_profit(prices: List[int]) -> int:
    best_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > best_profit:
                best_profit = profit

    return best_profit
```


### Sposób 2: One pass
Interesujące są szczyty i doliny na danym wykresie. Musimy znaleźć największy szczyt po najmniejszej dolinie. Możemy utrzymać dwie zmienne - cenę minimalną i maxprofit odpowiadające najmniejszej dolinie oraz maksymalny zysk (maksymalna różnica pomiędzy ceną sprzedaży i ceną minimalną), które uzyskaliśmy do tej pory.

```python
from typing import List


def max_profit(prices: List[int]) -> int:
    best_profit = 0
    min_price = 999

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > best_profit:
            best_profit = prices[i] - min_price
    return best_profit
```
