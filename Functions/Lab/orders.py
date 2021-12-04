user_input = input()
quantity = int(input())
price = 0


def order(price, quantity):
    result = None
    if user_input == "coffee":
        price = 1.50
        result = (f'{price * quantity:.2f}')
    elif user_input == "water":
        price = 1
        result = (f'{price * quantity:.2f}')
    elif user_input == "coke":
        price = 1.40
        result = (f'{price * quantity:.2f}')
    elif user_input == "snacks":
        price = 2
        result = (f'{price * quantity:.2f}')
    return result


print(order(price, quantity))
