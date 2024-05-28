# WRITE YOUR SOLUTION HERE:
# Please write a function named products_in_shopping_list(shopping_list, amount: int) which takes a ShoppingList object and an integer value as its arguments. The function returns a list of product names. The list should include only the products with at least the number of items specified by the amount parameter.

class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.products):
            product = self.products[self.n]
            self.n += 1
            return product
        else:
            raise StopIteration

def products_in_shopping_list(shopping_list, amount: int):
    return [p[0] for p in shopping_list if p[1]>=amount]
        


my_list = ShoppingList()
my_list.add("bananas", 10)
my_list.add("apples", 5)
my_list.add("alcohol free beer", 24)
my_list.add("pineapple", 1)

print("the shopping list contains at least 8 of the following items:")
for product in products_in_shopping_list(my_list, 8):
    print(product)
