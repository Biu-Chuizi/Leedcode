def make_pizza(*toppings):
# """概述要制作的比萨"""
    print("\nMaking a pizza with the following toppings:") 
    for topping in toppings:
        print("- " + topping)
if __name__ == "__main__":
    make_pizza('pepperoni')
    make_pizza('mushrooms', 'green peppers', 'extra cheese')


