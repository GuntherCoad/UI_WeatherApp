from flask import Flask, render_template
        
def create_app(test_config=None):

    app = Flask(__name__)


    @app.route("/")
    def home():
        return render_template("index.html")

    import weather
    app.register_blueprint(weather.bp)

    return app
