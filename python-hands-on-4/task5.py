"""
Task 5: Online Shopping Cart
Two friends, Daniella and Godiya, walk into a mall and pick up just one cart to shop with.
Once inside, they split up and go to different wings of the mall, 
but since they share the same cart, everything either of them adds goes into the same cart.

cart = {}
godiya = ???
daniella = ???

During shopping:
- Daniella finds and adds "Shoes" (2 quantity).
- Godiya picks up "Watch" (1 quantity).
- Daniella later changes her mind and removes "Shoes" from the cart.
- Godiya also adds a "Bag" (1 quantity), then later removes it.

At checkout:
- The store takes a snapshot of the final order as an order summary for records.
- The shared cart is then emptied to prepare it for the next customer.
"""


# print(godiya)
# print(daniella)
# print(godiya == daniella) # should return true
# print(summary_of_cart)
# print(cart)
cart = {}
godiya = daniella = cart
godiya = cart.copy()
daniella = cart.copy()
godiya.update({'watch':1})
print(godiya)
daniella.update({'shoe':2})
print(daniella)
daniella.popitem()
print(daniella)
godiya.popitem()
print(godiya)
print(godiya == daniella )
New = cart.copy()
print(New)
cart.clear()
print(cart)
print("godiya and daniella those not return home with anything")


