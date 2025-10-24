#Importação do Flask
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import UserMixin

app = Flask(__name__)   
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'  # Configuração do banco de dados SQLite


db = SQLAlchemy(app)  # Inicialização do SQLAlchemy com a aplicação Flask
CORS(app)  # Habilitar CORS para a aplicação Flask

# Modelagem de exemplo para um usuário
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Modelagem de exemplo para um produto
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    descripition = db.Column(db.Text, nullable=True)

@app.route('/api/products/add', methods=["POST"])
def add_product():
    data = request.json
    if 'name' in data and 'price' in data:
        product = Product(name=data['name'], price=data['price'], descripition=data.get('description'))
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Product Added Sucessufol"}), 201
    return jsonify({"message": "Invalid data"}), 400


@app.route('/api/products/delete/<int:product_id>', methods=["DELETE"])
def delete_product(product_id):
    product = Product.query.get(product_id) #Recuperar o Produto pelo ID
    if product: #Verificar se o produto existe
        db.session.delete(product) #Deletar o produto do banco de dados
        db.session.commit() #Confirmar a transação
        return jsonify({"message": "Product Deleted Successfully"}), 200 
    return jsonify({"message": "Product Not Found"}), 404

@app.route('/api/products/<int:product_id>', methods=["GET"])
def get_product_details(product_id):
    product = Product.query.get(product_id)  # Recuperar o produto pelo ID
    if product:  # Verificar se o produto existe
        product_data = {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "descripition": product.descripition
        }
        return jsonify(product_data), 200
    return jsonify({"message": "Product Not Found"}), 404


@app.route('/api/products/update/<int:product_id>', methods=["PUT"])
def update_product(prodcut_id):
    product = Product.query.get(product_id)  # Recuperar o produto pelo ID
    if not product:  # Verificar se o produto existe
        return jsonify({"message": "Product Not Found"}), 404
    
    data = request.json
    if 'name' in data:
        product.name = data['name']

    if 'price' in data:
        product.price = data['price']

    if 'description' in data:
        product.descripition = data['description']

    db.session.commit()  # Confirmar a transação

    return jsonify({"message": "Product Updated Successfully"})


@app.route('/api/products', methods=["GET"])
def get_products():
    products = Product.query.all()  # Recuperar todos os produtos
    products_list = []
    for product in products:
        products_list.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
        })
    return jsonify(products_list), 200


# Definir uma rota para a página inicial e uma função que será executada ao requisitar
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)  # Executa o servidor Flask em modo de depuração

