
# Tvärsumma 2


def tvarsumman2(n):
    summa = 0
    while n > 0:
        summa += n % 10
        n //= 10
    return summa

print(tvarsumman2(14591))