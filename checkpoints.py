def myfunc(str):
    text = ""
    i = 0
    while i < len(str):
        if i % 2 == 0:
            text += str[i].lower()
        else:
            text += str[i].upper()
        i += 1
    return text


print(myfunc("Anthromorphism"))


def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
