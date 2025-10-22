#Importação do Flask
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)   
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'  # Configuração do banco de dados SQLite


db = SQLAlchemy(app)  # Inicialização do SQLAlchemy com a aplicação Flask

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
        product = Product(name=data['name'], price=data['price'], descripition=data.get('descripition'))
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



# Definir uma rota para a página inicial e uma função que será executada ao requisitar
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)  # Executa o servidor Flask em modo de depuração

