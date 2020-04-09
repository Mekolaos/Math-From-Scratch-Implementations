

def mean(num_array):
    array_len = len(num_array)
    num = 0
    for i in num_array:
        num += i
    return int(num/array_len)

def variance(num_array, array_len):
    mean_ = mean(num_array)
    num = 0
    for i in num_array:
        num += (i - mean_)**2
    return int(num/array_len)

def standard_deviation(num_array, sample):
    if not sample:
        return int(variance(num_array, len(num_array)) **0.5)
    else:
        return int(variance(num_array, len(num_array)-1) **0.5)
        
