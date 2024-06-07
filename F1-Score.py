greater_than_zero = True
integer = True
def Precision (TP, FP):
    P = int(TP)/(int(TP)+int(FP))
    return P
def Recall (TP, FN):
    R = int(TP)/(int(TP)+int(FN))
    return R
def F1_score (P, R):
    return 2 * P * R/(P + R)
def check_integer(x):
    try:
        int_x = int(x)
        return True
    except ValueError:
        return False
def print_check_integer(TP, FP, FN):
    global integer
    error = []
    if check_integer(TP) == False:
        error.append("TP")
    if check_integer(FP) == False:
        error.append("FP")
    if check_integer(FN) == False:
        error.append("FN")
    if len(error) > 0:
        integer = False
    if len(error) == 1:
        print(f"{error[0]} must be int")
    elif len(error) == 2:
        print(f"{error[0]} and {error[1]} must be int")
    elif len(error) == 3:
        print(f"{error[0]} and {error[1]} and {error[2]} must be int")
    return integer
def print_check_greater_than_zero(TP, FP, FN):
    global greater_than_zero
    if int(TP) <= 0 or int(FP) <= 0 or int(FN) <= 0:
        greater_than_zero = False
        print("TP and FP and FN must be greater than zero")
    return greater_than_zero
def print_result(TP, FP, FN):
    print_check_integer(TP, FP, FN)
    if integer == True:
        print_check_greater_than_zero(TP, FP, FN)
        if greater_than_zero == True:
            P = Precision(TP, FP)
            R = Recall(TP, FN)
            print(P)
            print(R)
            print(F1_score(P, R))
if __name__ == "__main__":
    TP = input()
    FP = input()
    FN = input()
    print_result(TP, FP, FN)
