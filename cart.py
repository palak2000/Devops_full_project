from flask import Flask, Blueprint, render_template, redirect, url_for

cart_bp = Blueprint('cart', __name__)

cart_items = []

@cart_bp.route('/')
def view_cart():
    return render_template('cart.html', cart_items=cart_items)

@cart_bp.route('/cart/add/<product_id>')
def add_to_cart(product_id):
    cart_items.append(product_id)
    return redirect(f'/products/{product_id}')

app = Flask(__name__)
app.register_blueprint(cart_bp)

@app.route('/')
def home():
    return redirect(url_for('cart.view_cart'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)

