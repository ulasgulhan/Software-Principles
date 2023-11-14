lst = [12, 11, 19, 2, 99]
lst_1 = []

# Here, there are two responsibilities: performing operations and adding to the list, and checking whether the number is odd or even

def tek_cift_mi(sayi: int) -> str:
    if sayi % 2 == 0:
        lst_1.append(sayi * 2)
    else:
        lst_1.append(sayi * 3)
     




def main():
    for i in lst:
        tek_cift_mi(i)
    print(lst_1)

main()