import functools as ft

def credit_check(param):
    account_identifier = [int(x) for x in param]
    
    for x in range(0, len(account_identifier), 2):  # for every other number in the list, multiply it by 2
        account_identifier[x]*=2

    two_times_every_other_digit = [str(x) for x in account_identifier]   # converts each number into a string

    temp = []

    # Checks if a number is double digits. If so, take the sum of their digits
    for n in two_times_every_other_digit:
        if(len(n)>1):
            a = int(n[0]) + int(n[1])
            temp.append(a)
        else:
            temp.append(n)

    summed_digits_over_ten = [int(x) for x in temp] # convert each num_str into an integer

    sum = ft.reduce(lambda agg, num : agg + num, summed_digits_over_ten)    # take the sum of all the numbers in the list

    if(sum%10 == 0):
        return ("The number is valid!") 
    else:
        return("The number is invalid!")

# print(credit_check('5541808923795240'))
# print(credit_check("4024007136512380"))
# print(credit_check("6011797668867828"))
# print(credit_check("5541801923795240"))
# print(credit_check("4024007106512380"))
# print(credit_check("6011797668868728"))