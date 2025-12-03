import store
import products

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

def enter_to_continue():
    while True:
        print()
        user_input = input('Press enter to continue')
        break

def start(store):
    while True:
        print(f'-------# WELCOME TO BEST BUY #--------')
        print(f'------# your electronics-store #------', end='\n\n')
        print(f'1. List all products in store')
        print(f'2. Show total amount in store')
        print(f'3. Make an order')
        print(f'4. Quit', end='\n\n')
        user_menu_selection = int(input('Please choose a number: '))
        print(f'')

        if user_menu_selection == 1:
            for product in best_buy.get_all_products():
                product.show()
            enter_to_continue()

        elif user_menu_selection == 2:
            print(f'The entire stock contains {best_buy.get_total_quantity()} products')
            enter_to_continue()

        elif user_menu_selection == 3:
            shopping_cart = []
            while True:
                print(f'------------------------------------------------------')
                for i, product in enumerate(best_buy.get_all_products()):
                    print(f'{i + 1}.', end=' ')
                    product.show()
                print(f'------------------------------------------------------')
                product_choice = input('Which product do you want to buy: ')
                print(f'------------------------------------------------------')
                amount_choice = input('Which amount of the product do you prefer: ')

                if not product_choice and not amount_choice:
                    break
                shopping_cart.append((product_list[(int(product_choice) - 1)], int(amount_choice)))
            print(f'------------------------------------------------------')
            print('')
            price = best_buy.order(shopping_cart)
            print('')
            print(f'Total: {price:.2f} €', end='\n')
            enter_to_continue()

        elif user_menu_selection == 4:
            print('Thank you for choosing BEST BYE! 😉')
            break
        else:
            print(f'Invalid value.')
            enter_to_continue()

def main():
    start(best_buy)

if __name__ == '__main__':
    main()