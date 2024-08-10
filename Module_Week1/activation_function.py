import math
alpha = 0.01
check_number = True
check_name = True
def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
    return True
def sigmoid(x):
    return 1 / (1 + math.exp(-x))
def ReLU(x):
    if x <= 0:
        return 0
    else:
        return x
def ELU(x):
    if x <= 0:
        return alpha * (math.e - 1)
    else:
        return x
def func_check_name(name):
    global check_name
    if name not in ["sigmoid", "ReLU", "ELU"]:
        check_name = False
        print ("{f} is not supported".format(f=name))
    return check_name
def func_check_number(x):
    global check_number
    if is_number(x) == False:
        check_number = False
        print ("x must be a number")
    return check_number
def print_result(x, name):
    func_check_number(x)
    if check_number == True:
        func_check_name(name)
        if check_name == True:
            s = sigmoid(float(x))
            r = ReLU(float(x))
            e = ELU(float(x))
            if name == "sigmoid":
                print("f({f1}) = {f2}".format(f1 = x, f2 = s))
            elif name == "ReLU":
                print("f({f1}) = {f2}".format(f1 = x, f2 = r))
            else:
                print("f({f1}) = {f2}".format(f1 = x, f2 = e))
if __name__ == "__main__":
    x = input("x = ")
    name = input("activation function (sigmoid|relu|elu): ")
    print_result(x, name)
