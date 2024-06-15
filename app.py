from flask import Flask, render_template
from product import product_bp
from wishlist import wishlist_bp
from cart import cart_bp

app = Flask(__name__)

# Register blueprint for the product microservice
app.register_blueprint(product_bp, url_prefix='/products')
app.register_blueprint(wishlist_bp, url_prefix='/wishlist')
app.register_blueprint(cart_bp, url_prefix='/cart')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

