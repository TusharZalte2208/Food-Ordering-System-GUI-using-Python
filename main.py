import tkinter as tk
from tkinter import messagebox

# Menu dictionary with item names and prices
menu = {
    "Pizza": 299,
    "Burger": 99,
    "Pasta": 169,
    "Coffee": 80,
    "Eggs": 110,
    "Sausage": 111,
    "Salad": 112,
    "Chai": 113,
}

class FoodOrderingApp:
    def __init__(self, root):
        """Initialize the GUI application"""
        self.root = root
        self.root.title("IMPERIAL CAFE - Order System")
        self.root.geometry("400x500")

        # Heading
        tk.Label(root, text="WELCOME TO IMPERIAL CAFE", font=("Arial", 14, "bold")).pack(pady=10)

        # Instruction label
        tk.Label(root, text="Select items from the menu:", font=("Arial", 12)).pack()

        # Dictionary to store selected items
        self.selected_items = {}

        # Creating Checkbuttons for each menu item
        self.item_vars = {}  # Stores IntVar() for each item
        for item, price in menu.items():
            var = tk.IntVar()  # Variable to store selection (0 or 1)
            self.item_vars[item] = var
            tk.Checkbutton(root, text=f"{item} - Rs.{price}", variable=var, font=("Arial", 11)).pack(anchor="w", padx=20)

        # Order button
        tk.Button(root, text="Place Order", command=self.place_order, font=("Arial", 12, "bold"), bg="green", fg="white").pack(pady=10)

        # Label to display total bill
        self.bill_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="blue")
        self.bill_label.pack(pady=10)

    def place_order(self):
        """Calculate total bill and display selected items"""
        total_bill = 0
        self.selected_items.clear()

        # Loop through the menu and check which items were selected
        for item, var in self.item_vars.items():
            if var.get() == 1:  # If item is selected
                self.selected_items[item] = menu[item]
                total_bill += menu[item]

        if not self.selected_items:
            messagebox.showwarning("No Selection", "Please select at least one item!")
            return

        # Display the total bill
        order_summary = "\n".join([f"{item} - Rs.{price}" for item, price in self.selected_items.items()])
        self.bill_label.config(text=f"Your Order:\n{order_summary}\n\nTotal Bill: Rs.{total_bill}")
        messagebox.showinfo("Order Confirmed", f"Thank you for ordering!\nTotal Bill: Rs.{total_bill}")

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = FoodOrderingApp(root)
    root.mainloop()
