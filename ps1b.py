# Problem Set 1B
# Name: Lawrence Lam
# Collaborators: 
# Time Spent: 1:45
# Late Days Used: N/A Listener

# Gathering user inputs
initial_balance = float(raw_input('Enter the outstanding balance on your credit card:'))
annual_interest_rate = float(raw_input('Enter the annual credit card interest rate as a decimal:'))

# Initializing 
minimum_monthly_payment         = 0.0
outstanding_balance             = initial_balance

# Outer loop to reset outstanding_balance and add $10 to minimum_monthly_payment
while outstanding_balance > 0:
    minimum_monthly_payment     = minimum_monthly_payment + 10.0
    outstanding_balance         = initial_balance #reset outstanding_balance

    # Iterating each month while it's less than a year AND the debt is not paid
    for month in range(1,13):
        outstanding_balance     = outstanding_balance * (1 + annual_interest_rate / 12 ) - minimum_monthly_payment
        #print 'Month: '+str(month)
        #print 'Remaining balance: '+str(outstanding_balance)

        # Break For loop if outstanding_balance less than 0 before payment 12
        if outstanding_balance < 0:
            break
        
# Calculate and print the results over the year
print 'RESULT'
print 'Monthly payment to pay off debt in one year:'+ str(int(minimum_monthly_payment))
print 'Number of months needed:'+ str(month)
print 'Remaining balance:'+ str(round(outstanding_balance,2))
