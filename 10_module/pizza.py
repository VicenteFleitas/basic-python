def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

def client_list(list):
    """Clients list"""
    for client in list:
        print(f"Hello {client}, Wellcome to Pizza Sky!")