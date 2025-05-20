import tkinter as tk
from tkinter import messagebox
import uuid

# --- Simulated backend data ---
users = {
    "user1": {"balance": 100.0},
    "user2": {"balance": 50.0}
}

transactions = []

def create_transaction(sender, receiver, amount):
    tx_id = str(uuid.uuid4())
    tx = {
        "id": tx_id,
        "sender": sender,
        "receiver": receiver,
        "amount": amount
    }
    transactions.append(tx)
    return tx

def make_payment(sender, receiver, amount):
    if sender not in users or receiver not in users:
        return "Invalid user"
    if users[sender]["balance"] < amount:
        return "Insufficient funds"

    users[sender]["balance"] -= amount
    users[receiver]["balance"] += amount
    create_transaction(sender, receiver, amount)
    return "Success"

# --- Tkinter UI ---
class PaymentApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Payment App")

        self.label = tk.Label(master, text="Welcome to the Payment App")
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.view_bal_btn = tk.Button(master, text="View Balances", command=self.show_balances)
        self.view_bal_btn.grid(row=1, column=0, pady=5)

        self.view_tx_btn = tk.Button(master, text="View Transactions", command=self.show_transactions)
        self.view_tx_btn.grid(row=1, column=1, pady=5)

        self.pay_label = tk.Label(master, text="Make a Payment")
        self.pay_label.grid(row=2, column=0, columnspan=2, pady=10)

        self.sender_var = tk.StringVar(master)
        self.receiver_var = tk.StringVar(master)
        self.amount_var = tk.StringVar()

        self.sender_menu = tk.OptionMenu(master, self.sender_var, *users.keys())
        self.receiver_menu = tk.OptionMenu(master, self.receiver_var, *users.keys())

        tk.Label(master, text="Sender:").grid(row=3, column=0)
        self.sender_menu.grid(row=3, column=1)

        tk.Label(master, text="Receiver:").grid(row=4, column=0)
        self.receiver_menu.grid(row=4, column=1)

        tk.Label(master, text="Amount:").grid(row=5, column=0)
        tk.Entry(master, textvariable=self.amount_var).grid(row=5, column=1)

        self.pay_btn = tk.Button(master, text="Send Payment", command=self.handle_payment)
        self.pay_btn.grid(row=6, column=0, columnspan=2, pady=10)

    def show_balances(self):
        msg = "\n".join([f"{user}: ${data['balance']:.2f}" for user, data in users.items()])
        messagebox.showinfo("User Balances", msg)

    def show_transactions(self):
        if not transactions:
            messagebox.showinfo("Transactions", "No transactions yet.")
            return
        msg = "\n".join([f"{tx['sender']} → {tx['receiver']}: ${tx['amount']:.2f}" for tx in transactions])
        messagebox.showinfo("Transaction History", msg)

    def handle_payment(self):
        sender = self.sender_var.get()
        receiver = self.receiver_var.get()
        try:
            amount = float(self.amount_var.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")
            return

        if sender == receiver:
            messagebox.showerror("Error", "Sender and receiver cannot be the same")
            return

        result = make_payment(sender, receiver, amount)
        if result == "Success":
            messagebox.showinfo("Success", "Payment completed successfully")
        else:
            messagebox.showerror("Error", result)

        self.amount_var.set("")

# Run the app
root = tk.Tk()
app = PaymentApp(root)
root.mainloop()

