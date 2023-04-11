from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:PostgreSQL%40123@localhost/twitter'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



from app.posts.routes import posts_bp
from app.weather import weather

app.register_blueprint(weather)
app.register_blueprint(posts_bp)

if __name__ == '__main__':
    app.run(debug = True)