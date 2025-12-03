import store
import products

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

def start(store):
    print(f'-------# WELCOME TO BEST BUY #--------')
    print(f'------# your electronics-store #------', end='\n\n')
    print(f'1. List all products in store')
    print(f'2. Show total amount in store')
    print(f'3. Make an order')
    print(f'4. Quit', end='\n\n')
    user_menu_selection = input('Please choose a number: ')

def main():
    start(best_buy)

if __name__ == '__main__':
    main()