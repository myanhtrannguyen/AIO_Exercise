def max_kernel(num_list, k):
    result = []
    for i in range(len(num_list) - k + 1):
        result.append(max(num_list[i:i+k]))
    return result