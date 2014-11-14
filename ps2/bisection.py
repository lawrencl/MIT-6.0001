#!/usr/bin/python

# Problem Set 2, bisection.py
# Name: Lawrence Lam
# Collaborators: none
# Time spent: 2:34

from bisection_lib import draw_interval

#### This helper function is for Bisection Search Part a #########
def get_final_balance(balance, interest_rate, payment):
    """
    balance (float): the initial balance
    interest_rate (float): the MONTHLY interest rate
    payment (float): the monthly payment. Must be a whole number.

    Returns the final balance. If the balance is paid off before a year has passed,
    return the balance amount at the point the balance is paid off.
    """
    finalBal = balance
    for i in range(1, 13):
        if finalBal < 0:
            break
        else:
            finalBal = finalBal*(1 + (interest_rate/12))
            finalBal = finalBal - payment
        print str(i)+' and Resulting Balance:'+str(finalBal)
    return finalBal

#### Some steps to guide you for Bisection Search Part b #########

# 1) Fetch user inputs
initial_balance = float(raw_input('Enter the outstanding balance on your credit card:'))
annual_interest_rate = float(raw_input('Enter the annual credit card interest rate as a decimal:'))

# 2) Set monthly payment rate, lower bound, upper bound
lower_bound = round(initial_balance / 12)
#upper_bound = round((initial_balance * (1 + (annual_interest_rate/12))**12) / 12)
upper_bound = round((initial_balance * ((1 + (annual_interest_rate/12)) ** 12)) / 12)
midpoint = round(0.5 * (upper_bound + lower_bound))

# 3) Keep halving the interval until upper and lower bound are $1 apart. You may find the get_final_balance 
#    helper function useful here.
# 4) Once upper and lower bound are only $1 apart, test lower bound to see if it pays off the balance. 
#    If it doesn't, use the upper bound instead.   
final_balance = get_final_balance(initial_balance, annual_interest_rate, midpoint)

original_upper_bound = upper_bound
draw_interval(lower_bound, midpoint, upper_bound, original_upper_bound)

while (upper_bound - lower_bound) > 1:
    if final_balance > 0:
        lower_bound = midpoint
    else:
        orininal_upper_bound = upper_bound
        upper_bound = midpoint
    midpoint = round(0.5 * (upper_bound + lower_bound))
    final_balance = get_final_balance(initial_balance, annual_interest_rate, midpoint)
    draw_interval(lower_bound, midpoint, upper_bound, original_upper_bound)

# 5) Print the results
print 'RESULT'
print 'Monthly payment to pay off debt in 1 year:'+ str(midpoint)
print 'Balance:'+ str(round(final_balance,2))