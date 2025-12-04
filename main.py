from curses.ascii import isdigit

import store
import products

best_buy = store.Store(store.product_list)

def enter_to_continue():
    while True:
        print()
        user_input = input('Press enter to continue')
        break

def main():

    try:
        while True:
            try:
                print(f'-------# WELCOME TO BEST BUY #--------')
                print(f'------# your electronics-store #------', end='\n\n')
                print(f'1. List all products in store')
                print(f'2. Show total amount in store')
                print(f'3. Make an order')
                print(f'4. Quit', end='\n\n')
                user_menu_selection = input('Please choose a number: ')
                print(f'')

                if not user_menu_selection.isdigit():
                    raise ValueError(f'Only digits between 1-4 are allowed!')
                else:
                    user_menu_selection = int(user_menu_selection)

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

                        if not product_choice.isdigit():
                            raise ValueError(f'product input is not a numeric, please enter the index of your product!')
                        elif not amount_choice.isdigit():
                            raise ValueError(f'amount input is not a numeric, please enter your desired amount of the product!')
                        else:
                            product_choice = int(product_choice)
                            amount_choice = int(amount_choice)

                        if product_choice < 1 or product_choice > len(best_buy.get_all_products()):
                            raise IndexError(f'product list do no contain this count of products, choose a number between 1-{len(best_buy.get_all_products())}!')
                        elif amount_choice < 0:
                            raise ValueError(f'negative amount values are not allowed!')

                        shopping_cart.append((best_buy.get_all_products()[(int(product_choice) - 1)], int(amount_choice)))
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
                    print(f'Only digits between 1-4 are allowed!')
                    enter_to_continue()

            except TypeError as e:
                print(f'\nTypeError: {e}\n')
            except ValueError as e:
                print(f'\nValueError: {e}\n')
            except IndexError as e:
                print(f'\nIndexError: {e}\n')

    except KeyboardInterrupt:
        print('\n\nProgram interrupted. Thank you for choosing Best Bye! 👋')



if __name__ == '__main__':
    main()