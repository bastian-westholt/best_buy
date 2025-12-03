from products import Product

class Store:
    def __init__(self, products_list):
        self.products = products_list

    def add_product(self, product):
        self.products.append(product)
        print('Product was successfully added.')

    def remove_product(self, product_to_del):
        self.products.remove(product_to_del)
        print('Product was successfully removed.')

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