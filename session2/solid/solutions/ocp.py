

"""

This is an example where we violate the OCP

"""

def calculate_total_price_violating(price, discount_type):
    if discount_type == "percentage":
        return price * 0.9
    elif discount_type == "fixed":
        return price - 20
    else:
        raise ValueError("Unknown discount type")


"""

This is how we could fix this.
Your task is to add another class that allows for fixed discounts.

"""

from abc import ABC, abstractmethod


class Discount(ABC):
    @abstractmethod
    def apply(self, price):
        pass


class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply(self, price):
        return price * (1 - self.percentage / 100)


# TODO new class goes here
class FlatDiscount(Discount):
    def __init__(self, discount_amount):
        self.discount_amount = discount_amount

    def apply(self, price):
        return price - self.discount_amount

def calculate_total_price(price, discount: Discount):
    return discount.apply(price)



price = 100
percentage_discount = PercentageDiscount(10)
fixed_discount = FlatDiscount(20) # TODO change me and give a discount of 20 moneys

print(calculate_total_price(price, percentage_discount))
print(fixed_discount_result := calculate_total_price(price, fixed_discount))

assert fixed_discount_result == 80