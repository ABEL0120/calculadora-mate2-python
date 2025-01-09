from flask import Flask
def create_app():
    app = Flask(__name__)
    # Registro de rutas
    from .routes import main_bp
    app.register_blueprint(main_bp)
    return app