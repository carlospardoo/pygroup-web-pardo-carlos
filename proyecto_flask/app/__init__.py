from flask import Flask
from products.views import prods

app = Flask(__name__)
app.register_blueprint(prods)

if __name__ == '__main__':
    app.run(debug=True)
