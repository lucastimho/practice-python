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
