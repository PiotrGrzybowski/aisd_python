def delivery_presents_iterative(houses):
    for house in houses:
        print(f"Delivered to {house}'s house")


def delivery_presents_recurrent(houses):
    if len(houses) == 1:
        print(f"Delivered to {houses[0]}'s house")
    else:
        middle_index = len(houses) // 2
        first_half = houses[:middle_index]
        second_half = houses[middle_index:]

        delivery_presents_recurrent(first_half)
        delivery_presents_recurrent(second_half)


def harmonic_series_sum(n):
    result = 0
    for i in range(1, n + 1):
        result += 1 / i
    return result


def harmonic_series_sum_rec(n):
    if n == 1:
        return 1
    else:
        return 1 / n + harmonic_series_sum_rec(n - 1)


def recursive_list_sum(data_list):
    total = 0
    for element in data_list:
        if type(element) == list:
            total = total + recursive_list_sum(element)
        else:
            total = total + element
    return total


def sum_of_nested_lists(data_list):
    if len(data_list) == 0:
        return 0
    elif type(data_list[0]) == int:
        return data_list[0] + sum_of_nested_lists(data_list[1:])
    else:
        return sum_of_nested_lists(data_list[0]) + sum_of_nested_lists(data_list[1:])


def flatten(data_list):
    if len(data_list) == 0:
        return []
    elif type(data_list[0]) == int:
        return [data_list[0]] + flatten(data_list[1:])
    else:
        return flatten(data_list[0]) + flatten(data_list[1:])


if __name__ == '__main__':
    # houses = ['Piotr', 'Ania', 'Ewa', 'Tomek']
    # delivery_presents_iterative(houses)
    print(harmonic_series_sum(4))
    print(harmonic_series_sum_rec(4))

    print(rc([1, [2, 1], [[[3]]]]))
