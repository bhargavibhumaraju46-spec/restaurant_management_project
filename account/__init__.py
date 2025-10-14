def calculate_order_discount(order_total, discount_percentage):
    if not isinstance(order_total, (int, float)) or not isinstance(discount_percentage, (int, float)):
        raise TypeError("Both order_total and discount_percentage must be numeric values")
       if order_total < 0 or discount_percantage < 0:
        raise ValueError("order_total and discount_percentage must not be negative")
        discount_amount = order_total * (discount_percantage / 100)
        return discount_amount
if __name__ == "__main__":
    order_total = 1000
    discount_percantage = 10
    discount_amount = calculate_order_discount(order_total, discount_percantage)
    print(f"Discount Amount: {discount_amount}")                       