#################### usage of map in list using function ##############################

price_list = {875,225,550,650}

def disc(price):
    discount = (price * 10)/100
    discount_price = price -discount
    return discount_price

disc_list = list(map(disc ,price_list ))

print(disc_list)