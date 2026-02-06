from flask import Flask, render_template

from academics.routes import academics_bp
from analytics.routes import analytics_bp
from logistics.routes import logistics_bp
from stores.routes import stores_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(academics_bp, url_prefix="/academics")
    app.register_blueprint(analytics_bp, url_prefix="/analytics")
    app.register_blueprint(logistics_bp, url_prefix="/logistics")
    app.register_blueprint(stores_bp, url_prefix="/stores")

    @app.route("/")
    def home():
        return render_template("home.html")

    return app

if __name__ == "__main__":
    create_app().run(debug=True)