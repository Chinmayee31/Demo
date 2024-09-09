
# Define a class named `Product`
class Product:
    def __init__(self, name, price):
        self.name = name   # Name of the product
        self.price = price # Price of the product

# Define a class named `ShoppingCart`
class ShoppingCart:
    def __init__(self):
        self.items = [] # List to store added products

    # Method to add a product to the cart
    def add_product(self, product):
        self.items.append(product)
        print(f"Added {product.name} to the cart.")

    # Method to calculate the total price of products in the cart
    def total_price(self):
        total = sum(item.price for item in self.items) # Summing up prices of all items
        return total

    # Method to display the items in the cart
    def show_cart(self):
        if not self.items:
            print("The cart is empty.")
        else:
            print("Shopping Cart:")
            for item in self.items:
                print(f"- {item.name}: ${item.price:.2f}")
            print(f"Total: ${self.total_price():.2f}")

# Create instances of Product
apple = Product(name="Apple", price=0.50)
banana = Product(name="Banana", price=0.30)
milk = Product(name="Milk", price=1.20)

# Create an instance of ShoppingCart
cart = ShoppingCart()

# Add products to the cart
cart.add_product(apple)
cart.add_product(banana)
cart.add_product(milk)

# Display the items in the cart and the total price
cart.show_cart()
