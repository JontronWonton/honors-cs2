# Jonathan Klein
# 11/16/18
# Dictionary3.py


def line():
    print('='*50)


def addToCart(itemName, itemAmount):
    global grandTotal
    global totalItems
    for i in groceryStore:
        if groceryStore[i]['itemName'] == itemName:
            itemFound = i
            if itemAmount > groceryStore[itemFound]['itemQuant']:
                print('Not enough of item in stock.')
                break
            else:
                totalItems += itemAmount
                shoppingCart.append(groceryStore[itemFound]['itemName'])
                groceryStore[itemFound]['itemQuant'] -= itemAmount
                print('Added {} {}s to cart'.format(itemAmount, itemName))
                grandTotal += itemAmount*groceryStore[itemFound]['itemPrice']
                break
    else:
        print('Item not found in shop.')


def checkOut():
    a = 0
    print('You bought:')
    for i in shoppingCart:
        a += 1
        if a == len(shoppingCart):
            print(i)
        else:
            print(i, end=', ')
    print(f'Total: ${grandTotal}')


groceryStore = \
    {
    1:
    {
'itemName' : 'apple',
'itemPrice' : 1,
'itemQuant' : 10
    },
    2:
    {
'itemName' : 'banana',
'itemPrice' : 2,
'itemQuant' : 15
    },
    3:
    {
'itemName' : 'watermelon',
'itemPrice' : 4,
'itemQuant' : 5
    },
    4:
    {
'itemName' : 'kiwi',
'itemPrice' : 2,
'itemQuant' : 15
    },
    5:
    {
'itemName' : 'coconut',
'itemPrice' : 3,
'itemQuant' : 10
    }
}

grandTotal = 0
totalItems = 0
shoppingCart = []

print('Inventory:\n')
for key in groceryStore:
    print(f"{str(groceryStore[key]['itemName']).capitalize()}")
    print(f"Price: ${str(groceryStore[key]['itemPrice']).capitalize()}")
    print(f"Quantity: {str(groceryStore[key]['itemQuant']).capitalize()}\n")

print('Type "checkout" to finish at any time.\n')

while True:
    item = input('What would you like?\n')
    if item == 'checkout':
        line()
        checkOut()
        line()
        break
    else:
        amt = int(input('How many would you like?\n'))
        addToCart(item, amt)
        line()
