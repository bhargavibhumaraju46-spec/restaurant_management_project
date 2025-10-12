# models.py

from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
        base_price = models.FloatField()
            discount_percentage = models.FloatField(default=0.0)  # discount percentage field

                def calculate_final_price(self):
                        """
                                Calculate the final price of the menu item considering the discount.
                                        """
                                                discount_amount = (self.discount_percentage / 100) * self.base_price
                                                        final_price = self.base_price - discount_amount
                                                                return max(final_price, 0.0)  # ensure price doesn't go negative

                                                                    def __str__(self):
                                                                            return self.name

                                                                            # Example usage:
                                                                            if __name__ == "__main__":
                                                                                # Create an instance of MenuItem
                                                                                    item = MenuItem(name="Pizza", base_price=200.0, discount_percentage=10.0)
                                                                                        
                                                                                            # Calculate and print the final price
                                                                                                final_price = item.calculate_final_price()
                                                                                                    print(f"Final price of {item.name}: ₹{final_price}")
