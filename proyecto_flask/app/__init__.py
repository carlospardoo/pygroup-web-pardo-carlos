from flask import Flask

app = Flask(__name__)

#from app.products import views
#from app.products import products

if __name__ == '__main__':
    app.run(debug=True)
