import numpy as np

def calculate(list):

    #Error messages if list not 9
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
   
    #Convert list into 3x3 numpy array
    num_arr = np.array(list).reshape(3,3)

    #Calculate the mean, variance, std deviation, max, min and sum 
    mean_val = [np.mean(num_arr, axis= 0).tolist() , np.mean(num_arr, axis=1).tolist(), np.mean(num_arr.flatten()).tolist()]
    variance_val = [np.var(num_arr, axis= 0).tolist(), np.var(num_arr, axis=1).tolist() , np.var(num_arr.flatten()).tolist()]
    std_dev_val = [np.std(num_arr, axis= 0).tolist(), np.std(num_arr, axis=1).tolist(), np.std(num_arr.flatten()).tolist()]
    max_val = [np.max(num_arr, axis= 0).tolist(), np.max(num_arr, axis=1).tolist(), np.max(num_arr.flatten()).tolist()]
    min_val = [np.min(num_arr, axis= 0).tolist(), np.min(num_arr, axis=1).tolist(), np.min(num_arr.flatten()).tolist()]
    sum_val = [np.sum(num_arr, axis= 0).tolist(), np.sum(num_arr, axis=1).tolist(), np.sum(num_arr.flatten()).tolist()]

    #Lists of keys and value to create dictionary 
    keys_num = ['mean','variance','standard deviation','max','min','sum']
    values_num = [mean_val, variance_val , std_dev_val, max_val, min_val, sum_val]

    #Creating dictionary
    calculations = {keys_num[i]: values_num[i] for i in range(len(keys_num))}

    return calculations