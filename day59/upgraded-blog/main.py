from flask import Flask, render_template
import requests

app = Flask(__name__)
API_ENDPOINT = "https://api.npoint.io/ba2dda467100b9824e65"
blog = requests.get(API_ENDPOINT).json()


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=blog)


@app.route('/about.html')
def about_post():
    return render_template("about.html")


@app.route('/contact.html')
def contact_post():
    return render_template("contact.html")


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in blog:
        if blog_post["id"] == index:
            requested_post = blog_post

    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
