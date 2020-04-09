

def mean(num_array):
    num = 0
    for i in num_array:
        num += i
    return int(num/len(num_array))

def variance(num_array):
    mean_ = mean(num_array)
    num = 0
    for i in num_array:
        num += (i - mean_)**2
    return int(num/len(num_array))

def standard_deviation(num_array):
    return int(variance(num_array) **0.5)
