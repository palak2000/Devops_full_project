from flask import Flask, Blueprint, render_template

product_bp = Blueprint('product', __name__)

@product_bp.route('/')
def product_home():
    return render_template('product_home.html')

@product_bp.route('/1')
def product_details(product_id):
    product = {
        'product_id': product_id,
        'product_name': 'Product Name',
        'price': 100.0,
        'description': 'Product Description'
    }
    return render_template('product_details.html', **product)

app = Flask(__name__)
app.register_blueprint(product_bp)

@app.route('/')
def home():
    return redirect(url_for('product.product_home'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)


