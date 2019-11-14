# Remove Duplicates from Sorted Array
Otrzymując na wejściu posortowaną tablicę liczb *values*, usuń z niej duplikaty *in-place* tak aby każdy element pojawił się tylko raz i zwróć długość tak otrzymanej tablicy.

W miejscu (in-place) znaczy, że nie można tworzyć nowej listy ani żadnej innej strukury danych tylko zmodyfikować listę w miejscu w celu uzyskania stałej złożoności pamięciowej O(1)

## Przykład 1
Mając na wejściu values = [1, 1, 2]

Twoja funkcja powinna zwracać długość = 2, przy czym pierwsze dwa elementy przetworzonej listy to odpowiednio 1 i 2.

## Przykład 2
Mając na wejściu values = [0,0,1,1,1,2,2,3,3,4]

Twoja funkcja powinna zwracać długość = 5, przy czym pierwszych pięć elementów przetworzonej listy powino wynosić odpowiednio na 0, 1, 2, 3 i 4.

## Rozwiązanie
### Sposób 1: Dwa wskaźniki
Wiedząc, że lista jest posortowana utwórzmy dwa wskaźniki *i* oraz *j* gdzie pierwszy z nich będzie szybki a drugi wolny. Tak długo jak wartość *i-tego* elementu będzie równa wartości *j-tego* elementu będziemy zwiększać wartość *f* o jeden, żeby przeskoczyć duplikat.

Kiedy dotrzemy do miejsca w którym *j-ty* element nie równa się *i-temu* to znaczy, że dotarliśmy do miejsca w którym przeskoczyliśmy wszystkie duplikaty więc musimy zwiększyć wartość *i* oraz przenieść jego wartość *j-tego* elementu na *i-ty* indeks.

```python
from typing import List


def remove_duplicates(values: List[int]) -> int:
    if not values:
        return 0

    i = 0
    j = 1

    while j < len(values):
        if values[j] != values[i]:
            i += 1
            values[i] = values[j]

        j += 1

    return i + 1


if __name__ == '__main__':
    print(remove_duplicates([1, 1, 1, 1, 2, 2, 2, 3]))
```
