# utils.py

def calculate_discount(original_price, discount_percentage):
    try:
            original_price = float(original_price)
                    discount_percentage = float(discount_percentage)
                            
                                    if original_price < 0 or discount_percentage < 0 or discount_percentage > 100:
                                                return "Error: Invalid input. Prices and discount percentages should be non-negative, and discount percentage should be <= 100."
                                                        
                                                                discounted_price = original_price - (original_price * discount_percentage / 100)
                                                                        return discounted_price
                                                                            
                                                                                except ValueError:
                                                                                        return "Error: Invalid input. Please ensure both original price and discount percentage are numbers."