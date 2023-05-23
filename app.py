from config import Config
from app import app

if __name__ == '__main__':
    app.secret_key=Config.SECRET_KEY
    app.run(debug=Config.DEBUG)