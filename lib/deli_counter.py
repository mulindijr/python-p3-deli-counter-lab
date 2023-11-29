def line(katz_deli):
    pass
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        callout = "The line is currently:"
        for index, name in enumerate(katz_deli):
            callout += f" {index + 1}. {name}"
        print(callout)

def take_a_number(katz_deli, new_customer):
    katz_deli.append(new_customer)
    position = len(katz_deli)
    print(f"Welcome, {new_customer}. You are number {position} in line.")


def now_serving(katz_deli):
    if not katz_deli:
        print(f"There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        katz_deli.pop(0)