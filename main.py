from curses.ascii import isdigit

import store
import products

best_buy = store.Store(store.product_list)


def enter_to_continue():
    """Helper function to pause and wait for user input"""
    print()
    input('Press enter to continue')


def list_all_products():
    """Display all active products in the store"""
    for product in best_buy.get_all_products():
        product.show()
    enter_to_continue()


def show_total_amount():
    """Display the total quantity of all products in stock"""
    print(f'The entire stock contains {best_buy.get_total_quantity()} products')
    enter_to_continue()


def make_order():
    """Handle the order process - select products and quantities"""
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

        # Empty inputs break the loop
        if not product_choice and not amount_choice:
            break

        # Validate inputs
        if not product_choice.isdigit():
            raise ValueError(f'product input is not a numeric, please enter the index of your product!')
        elif not amount_choice.isdigit():
            raise ValueError(f'amount input is not a numeric, please enter your desired amount of the product!')
        else:
            product_choice = int(product_choice)
            amount_choice = int(amount_choice)

        # Validate ranges
        if product_choice < 1 or product_choice > len(best_buy.get_all_products()):
            raise IndexError(f'product list do no contain this count of products, choose a number between 1-{len(best_buy.get_all_products())}!')
        elif amount_choice < 0:
            raise ValueError(f'negative amount values are not allowed!')

        shopping_cart.append((best_buy.get_all_products()[(int(product_choice) - 1)], int(amount_choice)))

    # Process order if cart is not empty
    if shopping_cart:
        print(f'------------------------------------------------------')
        print('')
        price = best_buy.order(shopping_cart)
        print('')
        print(f'Total: {price:.2f} €', end='\n')
        enter_to_continue()


def quit_program():
    """Exit the program with a farewell message"""
    print('Thank you for choosing BEST BYE! 😉')
    return "quit"


def display_menu():
    """Display the main menu"""
    print(f'-------# WELCOME TO BEST BUY #--------')
    print(f'------# your electronics-store #------', end='\n\n')
    print(f'1. List all products in store')
    print(f'2. Show total amount in store')
    print(f'3. Make an order')
    print(f'4. Quit', end='\n\n')


def main():
    # Function pointer dictionary mapping menu choices to functions
    menu_options = {
        1: list_all_products,
        2: show_total_amount,
        3: make_order,
        4: quit_program
    }

    try:
        while True:
            try:
                display_menu()
                user_menu_selection = input('Please choose a number: ')
                print(f'')

                # Validate input
                if not user_menu_selection.isdigit():
                    raise ValueError(f'Only digits between 1-4 are allowed!')

                user_menu_selection = int(user_menu_selection)

                # Execute the selected function using function pointer
                if user_menu_selection in menu_options:
                    result = menu_options[user_menu_selection]()
                    # Check if quit was selected
                    if result == "quit":
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
            except Exception as e:
                # Catch all other exceptions (e.g., from buy() method when stock is insufficient)
                print(f'\nError: {e}\n')

    except KeyboardInterrupt:
        print('\n\nProgram interrupted. Thank you for choosing Best Bye! 👋')


if __name__ == '__main__':
    main()
