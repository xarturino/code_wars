# DESCRIPTION:
# There's a "3 for 2" (or "2+1" if you like) offer on mangoes. For a given quantity and price (per mango), calculate the total cost of the mangoes.

# Examples
# mango(2, 3) ==> 6    # 2 mangoes for $3 per unit = $6; no mango for free
# mango(3, 3) ==> 6    # 2 mangoes for $3 per unit = $6; +1 mango for free
# mango(5, 3) ==> 12   # 4 mangoes for $3 per unit = $12; +1 mango for free
# mango(9, 5) ==> 30   # 6 mangoes for $5 per unit = $30; +3 mangoes for free

def mango(quantity, price):
    for i in range(1, quantity+1):
        if i % 3 == 0:
            quantity-=1
    return quantity*price


# checking
print(mango(2, 3))
print(mango(3, 3))
print(mango(5, 3))
print(mango(9, 5))

#best practice
def mango(quantity, price):
    return (quantity - quantity // 3) * price