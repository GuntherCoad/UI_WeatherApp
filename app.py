from flask import Flask, render_template
        
def create_app(test_config=None):

    app = Flask(__name__)


    @app.route("/")
    def home():
        return render_template("index.html")
    
    @app.route("/temp")
    def temp():
        return render_template("tempPage.html")

    @app.route("/test")
    def test():
        return render_template("test.html")

    import weather
    app.register_blueprint(weather.bp)

    return app
