<div align="center">
<pre>
 ____  _____ ____ _____   ____  _   ___   __
| __ )| ____/ ___|_   _| | __ )| | | \ \ / /
|  _ \|  _| \___ \ | |   |  _ \| | | |\ V /
| |_) | |___ ___) || |   | |_) | |_| | | |
|____/|_____|____/ |_|   |____/ \___/  |_|

--- Y O U R   S H O W C A S E   S T O R E ---
</pre>
</div>

---

A shop backend I developed during my Masterschool training. The focus was on error handling and OOP patterns.

## What does this project do?

A simple e-commerce system for an electronics store. CLI-based, no UI - just backend logic. The project started with intentionally included bugs, which I then systematically identified and fixed.

## Setup

```bash
git clone <repo-url>
cd best_buy
python3 main.py
```

No dependencies required, runs with standard Python.

## How it works

### Product Class
Manages individual products. Name, price, and quantity are validated before being accepted. When stock reaches 0, the product is automatically deactivated. The `buy()` method checks stock availability before purchase.

### Store Class
Manages the product collection. The constructor ensures that only Product objects are added. When adding products, it checks if the product already exists. The `order()` method enables purchasing multiple products.

### Main Program
CLI with 4 options: list products, show total stock, place order, quit. Input validation is implemented throughout - invalid inputs display meaningful error messages instead of crashing.

## What I learned

### The Range-Check Bug
The most subtle error was `if x < len() or x > len()` - looks correct at first glance, but is logically wrong. With `or`, the condition is almost always true. Correct would be `if x < 1 or x > len()`. This experience showed me how important it is to carefully check Boolean logic.

### Exception Handling Strategy
Business logic (products.py, store.py) raises exceptions when rules are violated. Presentation layer (main.py) catches these and shows the user understandable messages. No print() statements in business logic, try-except blocks only where they belong.

### Type Checks before Value Checks
Check the type first, then validate the value. Otherwise `if not price` can incorrectly throw an error at 0, even though 0 can be a valid price.

```python
# Correct order
if not isinstance(price, (int, float)):
    raise TypeError('Price must be numeric')
if price < 0:
    raise ValueError('Price cannot be negative')
```

### 0 is not "empty"
For strings, `""` is empty. For numbers, `None` is empty. But `0` is a valid value, not empty. An important distinction to keep in mind.

## Project Status

All CRITICAL (7/7) and HIGH Priority (7/7) bugs are fixed. Out of 20 identified issues, 14 are resolved. The remaining 6 are edge cases that rarely occur in practice (e.g., product names consisting only of whitespace).

The code is production-ready. There are no known bugs that can crash the program.

## Testing

Tested scenarios:
- Text input when numeric values are expected
- Negative numbers
- Product number 0 or outside valid range
- Order quantity exceeds stock
- Attempting to buy 0 items
- Adding duplicate products
- Ctrl+C during program execution

All cases are cleanly handled with meaningful error messages.

## Technical

- Python 3.x (tested with 3.13)
- No external dependencies
- SOLID Principles, Design by Contract
- Exception types: TypeError, ValueError, IndexError, KeyboardInterrupt

## Best "Bye" Easter Egg

The exit message says "Thank you for choosing BEST BYE!" - the typo is intentional. 😉

---

**Masterschool E-Commerce Backend** | December 2025 | Bastian
