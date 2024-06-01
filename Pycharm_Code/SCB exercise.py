acct_num =int(input("Enter the account Number"))

cust_name =input("Enter the customer name")

acct_type =input('please confirm whether your account is current or Savings')

investment_type =input("please choose the investment type")

amt_to_deposit =int(input('Please enter the amount to deposit'))

if investment_type == 'FD':
    tenure = int(input('Please enter the number of months you opt for fixed deposit'))
    tenure_in_years = tenure/12
    profit = amt_to_deposit *(6.5/100)*tenure_in_years  # simple interest formula
    print('profit for the fixed deposit is : ', profit)


elif investment_type == 'RD' :
    citizenship_type = input('Please enter the citizenship type(citizen/senior citizen')
    tenure = int(input('Please enter the number of months you opt for recurring deposit'))
    tenure_in_years = tenure / 12
    if citizenship_type == 'citizen' :
        if tenure == 3 or tenure == 6 or tenure == 9 :
            profit = amt_to_deposit * (3.5 / 100) * tenure_in_years
        if tenure == 12:
            profit = amt_to_deposit * (6.5 / 100) * tenure_in_years
        if tenure == 18 or tenure == 24 :
            profit = amt_to_deposit * (6.7 / 100) * tenure_in_years
    if citizenship_type == 'senior citizen':
        if tenure == 3 or tenure == 6 or tenure == 9:
            profit = amt_to_deposit * (3.5 / 100) * tenure_in_years
        if tenure == 12:
            profit = amt_to_deposit * (6.7 / 100) * tenure_in_years
        if tenure == 18 or tenure == 24:
            profit = amt_to_deposit * (7.1 / 100) * tenure_in_years
    print('profit for the recurring deposit is : ' ,profit )







