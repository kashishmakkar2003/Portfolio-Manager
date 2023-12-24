print("Hello, this is your investment tracker!")
# List of investments with prices, risk, and return included
portfolio = [
    {"name": "Stock A", "quantity": 10, "price": 50, "risk": "low", "return": 8},
    {"name": "Stock B", "quantity": 5, "price": 30, "risk": "medium", "return": 6},
    {"name": "Fund C", "quantity": 2, "price": 100, "risk": "high", "return": 10},
    {"name": "ETF D", "quantity": 8, "price": 40, "risk": "medium", "return": 7}
]
print(portfolio)
#let's calculate Total Value"price": 50 
total_value = 0 #Initial value
# Loop through each investment in the portfolio
for investment in portfolio:
    # Add the product of quantity and price to the total value
    total_value += investment["quantity"] * investment["price"]

# Print the total value
print(total_value)

# Display more detailed information for each investment
for investment in portfolio:
    name = investment["name"]
    quantity = investment["quantity"]
    price = investment["price"]
    individual_value = quantity * price

    print "You have %d shares of %s, each worth $%d. So, the total value for %s is $%d." % (quantity, name, price, name, individual_value)

# User Menu
print("Menu:")
print("1. See the total portfolio value.")
print("2. See details for each investment, including risk and return.")

# Get user choice
user_choice = raw_input("Enter your choice (1 or 2): ")

# Process user choice
if user_choice == "1":
    print("Total Portfolio Value:", total_value)
elif user_choice == "2":
    # Display more detailed information for each investment
    for investment in portfolio:
        name = investment["name"]
        quantity = investment["quantity"]
        price = investment["price"]
        risk = investment["risk"]
        return_rate = investment["return"]
        individual_value = quantity * price

        print("You have {} shares of {}, each worth ${}.".format(quantity, name, price))
        print("Risk: {} | Expected Return: {}%".format(risk.capitalize(), return_rate))
        print("So, the total value for {} is ${}.".format(name, individual_value))
        print("-" * 30)
else:
    print("Invalid choice. Please enter 1 or 2.")
# Calculate total value with exception handling
total_value = 0
for investment in portfolio:
    try:
        total_value += investment["quantity"] * investment["price"]
    except KeyError:
        print("Error: Missing quantity or price information for an investment.")
        total_value = None
        break

# Display total portfolio value
if total_value is not None:
    print("Total Portfolio Value:", total_value)
# Ask for confirmation before quitting
confirm_quit = raw_input("Are you sure you want to quit? (yes/no): ")
if confirm_quit.lower() == "yes":
    print("Goodbye!")
else:
    print("Continuing with the program.")
import Tkinter as tk

# Placeholder data for investments
investments = [
    {"name": "Stock A", "quantity": 10, "price": 100},
    {"name": "Fund B", "quantity": 5, "price": 200},
    {"name": "ETF C", "quantity": 2, "price": 50},
    {"name": "ETF D", "quantity": 8, "price": 80}
]

def calculate_total_value():
    # Calculate total value based on the quantities and prices of each investment
    total_value = sum(investment["quantity"] * investment["price"] for investment in portfolio)
    print("Calculated Total Value:", total_value)  # Add this line for debugging
    result_label.config(text="Total Portfolio Value: ${:.2f}".format(total_value))

def show_investment_details():
    # Placeholder function to show details for each investment
    # Replace this with your actual investment details
    details = ""
    for investment in portfolio:
        name = investment["name"]
        quantity = investment["quantity"]
        price = investment["price"]

        # Check if "risk" and "return" keys are available
        risk = investment.get("risk", "N/A")
        return_rate = investment.get("return", "N/A")

        individual_value = quantity * price

        details += "{}:\n".format(name)
        details += "  Quantity: {}\n".format(quantity)
        details += "  Price per unit: ${}\n".format(price)
        details += "  Total value: ${}\n".format(individual_value)
        details += "  Risk: {}\n".format(risk.capitalize())
        details += "  Expected Return: {}%\n\n".format(return_rate)

    # Display details in the result_label
    result_label.config(text=details)


# Create the main application window
app = tk.Tk()
app.title("Portfolio Management App")
app.geometry("400x300")

# Add a label
label = tk.Label(app, text="Welcome to the Portfolio Management App!")
label.pack()

# Add a button for calculating total portfolio value
calculate_button = tk.Button(app, text="Total Portfolio Value", command=calculate_total_value)
calculate_button.pack()

# Add a second button for showing investment details
second_button = tk.Button(app, text="Show Investment Details", command=show_investment_details)
second_button.pack() # Create a label to display the result
result_label = tk.Label(app, text="")
result_label.pack()

# Run the Tkinter event loop
app.mainloop()

