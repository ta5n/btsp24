def is11Divisible(sayi):
    sum = 0
    while sayi > 0:
        n = sayi % 10;
        if n // 2 == 0:
            sum += int(sayi[n])
        else:
            sum -= int(sayi[n])
        n -= 1
    if sum == 0 or sum % 11 == 0:
        print("True")
    else:
        print("False")

is11Divisible(837419)