def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Parameters:
    - price (float): The original price of the item.
    - discount_percent (float): The discount percentage to be applied.

    Returns:
    - float: The final price after applying the discount if the discount is 20% or higher.
             Otherwise, returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user to enter the original price and the discount percentage
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price using the calculate_discount function
    final_price = calculate_discount(original_price, discount_percent)

    # Print the final price
    print(f"The final price after applying the discount is: {final_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for the price and discount percentage.")
