lst = [12, 11, 19, 2, 99]
lst_1 = []


def tek_cift_mi(sayi: int) -> str: # Here, the first function checks whether the number is odd or even
    if sayi % 2 == 0:
        return 'çift'
    else:
        return 'tek'


# The second function performs operations based on whether the number is odd or even, and adds it to the list.
def append_list(result: str, counter: int) -> None:
    if result == 'çift':
        lst_1.append(counter * 2)
    else:
        lst_1.append(counter * 3)

    print(lst_1)


def main():
    for i in lst:
        result = tek_cift_mi(i)
        append_list(result, i)


main()