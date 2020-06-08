def reverse(x):
    y, res = abs(x), 0
    boundry = (1<<31) - 1 if x>0 else 1<<31
    while y != 0:
        res = res*10 + y%10
        if res > boundry:
            return 0
        y //=10
    return res if x >0 else -res


if __name__ == "__main__":
    reverse(231)
