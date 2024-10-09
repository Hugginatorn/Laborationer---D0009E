
# Tvärsumma 1

def tvarsumman(n):
    if n >= 10:
        r = n%10
        n = (n - r )//10
        sum = r + tvarsumman(n)
        return sum
    else:

        return n
        
print(tvarsumman(14591))