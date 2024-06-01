family = ['velikandan','lakshmi','muthu','mari','kali','padma']

#print(family)

for x in range(0,6):
    print(family[x])

bio={
    'name':'muthu',
    'age': 27 ,
    'weight':70
}

print(bio.get('weight'))

print('muthu' in bio)

if 'muthu' in bio:
    print('value check')
else:
    print('no value check')

    price_list = {875, 225, 550, 650}


    def disc(price):
        discount = (price * 10) / 100
        discount_price = price - discount
        return discount_price

    disc_list = list(map(disc, price_list))

    print(disc_list)

