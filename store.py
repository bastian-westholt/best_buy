from products import Product

# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]

class Store:
    def __init__(self, products_list):
        if not isinstance(product_list, list):
            raise TypeError(f'invalid value type, it seems you did not pass a list!')
        for item in product_list:
            if not isinstance(item, Product):
                raise TypeError(f'all items must be Product objects, got {type(item).__name__}')
        self.products = products_list

    def add_product(self, product_to_add):
        if not isinstance(product_to_add, Product):
            raise TypeError(f'product must be a Product object!')
        if product_to_add in self.products:
            raise ValueError(f'Product already exists in store!')
        self.products.append(product_to_add)
        print('Product was successfully added.')

    def remove_product(self, product_to_del):
        if product_to_del in self.products:
            self.products.remove(product_to_del)
            print('Product was successfully removed.')
        else:
            print('Product do not exist.')

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.products:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self):
        active_products = []
        for product in self.products:
            if product.active:
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        order_total = 0
        for product, amount in shopping_list:
            print(f'{product.name}......{product.price:.2f} € per unit --> ({amount})')
            order_total += product.buy(amount)
        return order_total

'''macbook_air_m4 = Product("Macbook Air M4", 1250, 500)
edifier_w820nb_plus  = Product("Edifier W820NB Plus", 89, 775)'''