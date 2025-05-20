from flask import Flask, request, jsonify, render_template, redirect, url_for
import uuid

app = Flask(__name__)

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

@app.route('/')
def home():
    return render_template('index.html', users=users)

@app.route('/pay', methods=['GET', 'POST'])
def pay():
    if request.method == 'POST':
        sender = request.form['sender']
        receiver = request.form['receiver']
        amount = float(request.form['amount'])

        if sender not in users or receiver not in users:
            return "Invalid user", 400
        if users[sender]['balance'] < amount:
            return "Insufficient funds", 400

        users[sender]['balance'] -= amount
        users[receiver]['balance'] += amount
        create_transaction(sender, receiver, amount)

        return redirect(url_for('home'))

    return render_template('pay.html', users=users)

@app.route('/balance/<username>')
def balance(username):
    if username not in users:
        return "User not found", 404
    return render_template('balance.html', username=username, balance=users[username]['balance'])

@app.route('/transactions')
def list_transactions():
    return render_template('transactions.html', transactions=transactions)

if __name__ == '__main__':
    app.run(debug=True)

