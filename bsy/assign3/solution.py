
def rank(numbers):
    # Kodunuzu bu satirdan itibaren yaziniz, verilen satirlari silmeden istediginiz kadar satir kullanabilirsiniz:
    result = 0
    for curr_ind in range(len(numbers)):
        distance = 0
        for cons_ind in range(len(numbers)):
            if numbers[curr_ind] + 1 == numbers[cons_ind]:
                distance = abs(curr_ind - cons_ind)
                result += distance
    return result


### Asagidaki satirlari kodunuzu test etmek icin kullanabilirsiniz. 
i = 0
numbers = [
    [21, 4, 13, 5, 8, 17, 23, 6, 22],
    [21, 4, 13, 5, 8, 17, 22, 6, 23],
    [5, 6, 7, 8],
    [1, 3, 5, 2, 4, 6],
    [0, 3, 4, 1, 5, 7, 2],
]
for number in numbers:
    print("Girdi", i, ":", number)
    print("Cikti", i, ":", rank(number))
    i += 1
