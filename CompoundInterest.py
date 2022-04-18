# Coding Challenge 1, compound_interest_np03cs4s210070.py


# Compound Interest Calculator


# TODO: Write your code here!
print('Welcome to the Wolving compound interest calculator')
print('This program calculates your potential returns when you invest with us\nIt displays the year,period,interest paid and the current balance in a tabular format')


#==============USER INPUTS===============================================
principle_amt = float(input("Enter the Principle?"))
rate = float(input("Enter the rate?(in percentage)"))
n_of_years = int(input("Enter the number of years?"))
annual_interest = int(input("Enter the number of times the interestis compounded per year?"))
new_principle = float(principle_amt)

#=============INITIALIZERS===============================================
new_balance = 0
i = 1


#===============TABLE YEAR==================================================
print('{:20s}{:20s}{:20s}{:20s}{:20s}'.format("Year","Period","Old Balance","Interest","New Balance"))
           
print("--------------------------------------------------------------------------------------------------\n")

#==============TABLE ROWS====================================================
j = 1
temp = annual_interest
c = 1

#=================PRINTS THE YEAR=========================================
while i <= n_of_years:

#=============PRINTS THE PERIOD========================================
    while j <= temp:
    
#===========PRINTS THE INTEREST======================================
        final_value_formula = ((principle_amt * rate)/100)/(annual_interest)

#============NEW BALANCE===========================================
        new_balance = principle_amt + final_value_formula

#=============USING IF ELSE LOOPS==================================
        if (j == c): 
            print('{:20s}{:20s}{:20s}{:20s}{:20s}'.format(str(i), str(j), str(round(principle_amt, 2)),str(round(final_value_formula, 2)),str(round(new_balance, 2))))
            
        else:
            print('{:20s}{:20s}{:20s}{:20s}{:20s}'.format("", str(j), str(round(principle_amt, 2)),str(round(final_value_formula, 2)),str(round(new_balance, 2))))

#================CHANGING PRINCIPLE AMOUNT=========================
        principle_amt = new_balance
        f_new_balance = "{:.2f}".format(new_balance)
        j = j + 1
    temp = temp+4     
    c = c+4 
    i = i + 1
print(new_principle,'invested at',rate,'% for',n_of_years,'years compounded',annual_interest,'times per year is:',f_new_balance)
