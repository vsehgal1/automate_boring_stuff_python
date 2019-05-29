# comma_code.py
# automatetheboringstuff.com Chapter 4
# Vikram Sehgal

def list_inspect (lst):
    length = len(lst)
    strn = ""
    if (length == 0):
        return strn

    elif (length == 1):
        strn = strn + lst[0]
        return strn

    for i in range(length):
        if i == length-1:
            strn = strn + "and " + lst[i]
        else:
            strn = strn + lst[i] + ", "
    return strn


if __name__ == "__main__":
    print(list_inspect(['apples', 'bad', 'dank']))