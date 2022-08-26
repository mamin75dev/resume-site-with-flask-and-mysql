from flask import render_template


class BlogController:
    @staticmethod
    def blog_single():
        return render_template("blog-single.html")
