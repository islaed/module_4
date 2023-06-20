def palindrom(stroke):
    if stroke == stroke[::-1]:
        return True
    else:
        return False


print(palindrom('абввба'))
