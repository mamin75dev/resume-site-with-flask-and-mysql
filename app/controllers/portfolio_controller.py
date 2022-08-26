from flask import render_template


class PortfolioController:
    def portfolio_details():
        return render_template("portfolio-details.html")
