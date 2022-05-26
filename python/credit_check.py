import functools as ft

def credit_check(param):
    account_identifier = [int(x) for x in param]  # for every character in the string, convert to and int and append to new list
   
    for x in range(0, len(account_identifier), 2):  # for every other number in the list, multiply it by 2
        account_identifier[x]*=2

    str_ls = [str(y) for y in account_identifier]   # converts each number into a string

    final_ls = []

    # Checks if a number is double digits. If so, take the sum of their digits
    for z in str_ls:
        if(len(z) > 1):
            a = int(z[0]) + int(z[1])
            final_ls.append(a)
        else:
            final_ls.append(z)
            
    final_final_ls = [int(a) for a in final_ls] # convert each num_str into an integer

    sum = ft.reduce(lambda agg, num : agg + num, final_final_ls)    # take the sum of all the numbers in the list

    if(sum%10 == 0):
        return ("The number is valid!") 
    else:
        return("The number is invalid!")
            


# print(credit_check('5541808923795240'))