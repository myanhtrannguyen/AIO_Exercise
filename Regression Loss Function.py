import math
import random
check_integer = True
def MAE (y_true, y_pred):
    return math.fabs(y_true - y_pred)
def MSE (y_true, y_pred):
    return (y_true - y_pred) ** 2
def RMSE (y_true, y_pred):
    return MSE(y_true, y_pred) #Loi de bai?
def func_check_integer(num_samples):
    global check_integer
    check_integer = num_samples.isnumeric()
    if check_integer == False:
        print("number of samples must be an integer number")
    return check_integer
def func_generate_data(num_samples):
    targets = []
    for i in range (1, int(num_samples) + 1):
        targets.append(random.uniform(0,10))
    predicts = []
    for i in range (1, int(num_samples) + 1):
        predicts.append(random.uniform(0,10))
    return targets, predicts
def print_output(loss_name, num_samples):
    print("loss name: " + loss_name)
    if loss_name == "MAE":
        sum_res = 0
        targets, predicts = func_generate_data(num_samples)
        for i in range (int(num_samples)):
            res = MAE(targets[i], predicts[i])
            sum_res = sum_res + res
            print("sample: {}, pred: {}, target: {}, loss: {}".format(i, predicts[i], targets[i], res))
        mean = sum_res/int(num_samples)
        print("final MAE: {}".format(mean))
    elif loss_name == "MSE":
        sum_res = 0
        targets, predicts = func_generate_data(num_samples)
        for i in range(int(num_samples)):
            res = MSE(targets[i], predicts[i])
            sum_res = sum_res + res
            print("sample: {}, pred: {}, target: {}, loss: {}".format(i, predicts[i], targets[i], res))
        mean = sum_res / int(num_samples)
        print("final MSE: {}".format(mean))
    else:
        sum_res = 0
        targets, predicts = func_generate_data(num_samples)
        for i in range(int(num_samples)):
            res = RMSE(targets[i], predicts[i])
            sum_res = sum_res + res
            print("sample: {}, pred: {}, target: {}, loss: {}".format(i, predicts[i], targets[i], res))
        mean = sum_res / int(num_samples)
        print("final RMSE: {}".format(mean))
if __name__ == "__main__":
    num_samples = input("Input number of samples (integer number) which are generated: ")
    func_check_integer(num_samples)
    if check_integer == True:
        loss_name = input("Loss name: ")
        print_output(loss_name, num_samples)

