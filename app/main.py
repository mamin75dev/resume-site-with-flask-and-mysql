from flask import Flask
from controllers.blog_controller import BlogController
from controllers.main_controller import MainController
from controllers.portfolio_controller import PortfolioController

app = Flask(__name__)


@app.route("/")
def main():
    return MainController.main()


@app.route('/blog-single')
def bolg_single():
    return BlogController.blog_single()


@app.route('/portfolio-details')
def portfolio_details():
    return PortfolioController.portfolio_details()


if __name__ == "__main__":
    app.run("0.0.0.0", 5050, debug=True)
