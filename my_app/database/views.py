from decimal import Decimal
from flask import request, jsonify, Blueprint
from my_app.database.models import Product

database = Blueprint('database', __name__)

@database.route('/')
@database.route('/home')
def home():
    return "Welcome to the database home"

@database.route('/product/<key>')
def product(key):
    product = Product.objects(key=key).get_or_404()
    return 'Product - %s, $%s' % (product.name, product.price)

@database.route('/products')
def products():
    products = Product.objects.all()
    res = {}
    for product in products:
        res[product.key] = {
            'name': product.name,
            'price': str(product.price)
        }
    return jsonify(res)

@database.route('/product-create', methods=['POST',])
def create_product():
    name = request.form.get('name')
    key = request.form.get('key')
    price = request.form.get('price')
        
    product = Product(name=name,key=key,price=Decimal(price))
    
    product.save()
    return 'Product created'