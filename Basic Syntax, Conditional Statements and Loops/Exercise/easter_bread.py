budget = float(input())  ##total budget
flour_price = float(input())  ##Price for 1kg of flour
eggs_pack_price = flour_price - (flour_price * 0.25)  ##Price for 1pack of eggs
milk_price = flour_price * 1.25  ##Milk price
money_needed = flour_price + eggs_pack_price + (milk_price / 4)  ##Money needed for 1 bread
money_left = budget - money_needed
number_of_breads = 0
color_eggs = 0
budget_spent = False

while budget_spent is False:
    if money_needed >= money_left:
        budget_spent = True
        break
    else:
        number_of_breads = number_of_breads + 1
        color_eggs = color_eggs + 3
        money_left = budget - money_needed
        budget -= money_needed
    if number_of_breads % 3 == 0:
        color_eggs = color_eggs - (number_of_breads - 2)
        budget_spent = False
        continue

print(f'You made {number_of_breads} loaves of Easter bread! Now you have {color_eggs} eggs and {money_left:.2f}BGN left.')