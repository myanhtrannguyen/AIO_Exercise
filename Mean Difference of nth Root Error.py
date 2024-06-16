def MD_nRE(y, y_hat, n, p):
    return((y ** (1 / n)) - (y_hat ** (1/n))) ** p
if __name__ == "__main__":
    y = float(input())
    y_hat = float(input())
    n = float(input())
    p = float(input())
    print(MD_nRE(y, y_hat, n, p))