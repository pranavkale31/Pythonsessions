# Create a Product Class and create relevant methods inside the class. 
# Create accessor & mutator methods
# The class should store information like name, price, discount etc.

# class Product:
#     def __init__(self, name, price, discount=0):
#         self._name = name          
#         self._price = price        
#         self._discount = discount   

    
#     def get_name(self):
#         return self._name

#     def get_price(self):
#         return self._price

#     def get_discount(self):
#         return self._discount

#     def get_final_price(self):
#         """Calculate final price after discount."""
#         return self._price * (1 - self._discount / 100)

   
#     def set_name(self, name):
#         self._name = name

#     def set_price(self, price):
#         self._price = price

#     def set_discount(self, discount):
#         if 0 <= discount <= 100:
#             self._discount = discount
#         else:
#             raise ValueError("Discount must be between 0 and 100.")


# if __name__ == "__main__":
   
#     product = Product("Laptop", 1200, 10)


#     print("Product Name:", product.get_name())
#     print("Original Price:", product.get_price())
#     print("Discount:", product.get_discount(), "%")
#     print("Final Price after Discount:", product.get_final_price())

#     product.set_discount(15)
#     print("Updated Discount:", product.get_discount(), "%")
#     print("Final Price after Discount:", product.get_final_price())


#Create a Shopping Cart Class which takes products to be added inside the cart. 
# Class should contain methods to add/remove items and checkout. 

# class ShoppingCart:
#     def __init__(self):
#         self.cart = {}
    
#     def add_item(self, product_name, price, quantity=1):
       
#         if product_name in self.cart:
#             self.cart[product_name]['quantity'] += quantity
#         else:
#             self.cart[product_name] = {'price': price, 'quantity': quantity}
#         print(f"Added {quantity} of {product_name} to the cart.")
    
#     def remove_item(self, product_name, quantity=1):
        
#         if product_name in self.cart:
#             if self.cart[product_name]['quantity'] > quantity:
#                 self.cart[product_name]['quantity'] -= quantity
#                 print(f"Removed {quantity} of {product_name} from the cart.")
#             elif self.cart[product_name]['quantity'] == quantity:
#                 del self.cart[product_name]
#                 print(f"Removed all of {product_name} from the cart.")
#             else:
#                 print(f"Cannot remove {quantity} of {product_name}; only {self.cart[product_name]['quantity']} in the cart.")
#         else:
#             print(f"{product_name} is not in the cart.")
    
#     def checkout(self):
#         """Calculate the total cost and empty the cart."""
#         total = sum(item['price'] * item['quantity'] for item in self.cart.values())
#         print(f"Total cost: {total:.2f}")
#         self.cart.clear()  
#         print("Checkout complete. Your cart is now empty.")

#     def view_cart(self):
#         """Display the items in the cart."""
#         if not self.cart:
#             print("Your cart is empty.")
#             return
#         print("Items in your cart:")
#         for product_name, details in self.cart.items():
#             print(f"{product_name}: {details['price']} x {details['quantity']}")


# if __name__ == "__main__":
#     cart = ShoppingCart()
#     cart.add_item("Apple", 200, 3)
#     cart.add_item("Banana", 100 , 5)
#     cart.view_cart()
#     cart.remove_item("Apple", 1)
#     cart.view_cart()
#     cart.checkout()

