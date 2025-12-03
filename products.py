class Product:
    entire_stock = 850

    def __init__(self, name, price, quantity):
        try:
            if name is None:
                raise TypeError(f'You entered a value of None, only strings are allowed')
            elif name == '':
                raise ValueError(f'You entered an empty string, only strings with characters are allowed.')
            else:
                self.name = str(name)

            if not isinstance(price, (int, float)):
                raise TypeError(f'Price must be a real numeric, not of type None or alphabetic')
            elif price < 0:
                raise ValueError(f'No negative prices possible')
            else:
                self.price = float(price)

            if not isinstance(quantity, int):
                raise TypeError(f'Quantity must be a real numeric, not of type None or alphabetic')
            elif quantity < 0:
                raise ValueError(f'No negative stock possible')
            else:
                self.quantity = int(quantity)

            self.active = True

        except TypeError as v:
            print(f'Error: Wrong type was entered. {v}')
        except ValueError as e:
            print(f'Error: Unauthorized value was entered. {e}')

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True
        if self.active:
            print(f'Successfully activated {self.name}')


    def deactivate(self):
        self.active = False
        if not self.active:
            print(f'Successfully deactivated {self.name}')

    def show(self):
        print(f'{self.name}, Price: {self.price}, Stock: {self.quantity}')

    def buy(self, quantity):
        if quantity < 0:
            raise Exception(f'You can not buy negative amounts like {quantity} of {self.name}')
        elif self.quantity < quantity:
            raise Exception(f'Not enough {self.name} in stock (Stock: {self.quantity}), choose a lower amount.')

        self.quantity -= quantity
        if self.quantity <= 0:
            self.deactivate()

        total_price = self.price * quantity
        return total_price