import functools as ft

def credit_check(param):
    # convert string into a list of integers
    account_identifier = [int(x) for x in param]    
    
    # for every other number in the list, multiply it by 2
    for x in range(0, len(account_identifier), 2):  
        account_identifier[x]*=2

    # converts each number into a string
    two_times_every_other_digit = [str(x) for x in account_identifier]   

    # Sums digits of double digit numbers and appends to a temp list
    summed_digits_over_ten = []
    for n in two_times_every_other_digit:
        if(len(n)>1):
            a = int(n[0]) + int(n[1])
            summed_digits_over_ten.append(int(a))
        else:
            summed_digits_over_ten.append(int(n))

    # take the sum of all the numbers in the list
    results_sum = ft.reduce(lambda agg, num : agg + num, summed_digits_over_ten)    

    # Return results
    if(results_sum%10 == 0):
        return ("The number is valid!") 
    else:
        return("The number is invalid!")