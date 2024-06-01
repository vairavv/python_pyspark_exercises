######################## discout for a customer based on a type ####################
def student(price):
    stu_disc = (price * 10)/100
    return stu_disc

def regular(price):
    reg_disc = (price * 5)/100
    return reg_disc

price =int(input('Enter the total price'))
cust_type = input('Enter the customer type')

if cust_type =='student':
    stu_disc=student(price)
    reg_disc=regular(price)
    net_price = price-stu_disc-reg_disc
    print('net price after discount is',net_price)

else :
    reg_disc=regular(price)
    net_price = price - reg_disc
    print("net price after discout is",net_price)
