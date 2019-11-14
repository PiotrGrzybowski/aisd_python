# Remove Element 
Otrzymując na wejściu posortowaną tablicę liczb values oraz wartość val zwróć długość tablicy, kiedy usunęlibyśmy z niej wszyskie elementy o wartości val. Algorytm ion-place.

W miejscu (in-place) znaczy, że nie można tworzyć nowej listy ani żadnej innej strukury danych tylko zmodyfikować listę w miejscu w celu uzyskania stałej złożoności pamięciowej O(1)

## Przykład 1:
Wejście: values = [3,2,2,3], val = 3,
Wyjście: 2

## Przykład 2:
Wejście: values = [0,1,2,2,3,0,4,2], val = 2,
Wyjście: 2

## Rozwiazanie
Wykorzystamy metodę dwóch wskaźników, pierwszy będzie wolnym, drugi szybkim. Ustawmy na początku obydwa na 0. 
Iterujmy drugim od zera do długości podanej listy, jeżeli values[i] != values[j] wtedy przypisz values[j] do values[i] i zwiększ wartość i o 1.

```python
from typing import List


def remove_duplicates(values: List[int], val: int) -> int:
    i = 0
    for j in range(len(values)):
        if values[j] != val:
            values[i] = values[j]
            i += 1
    return i


print(remove_duplicates([4, 3, 7, 3, 2, 3], 3))

```
