from flask import Flask, render_template, request
import requests

posts = requests.get(
    "https://gist.githubusercontent.com/gellowg/389b1e4d6ff8effac71badff67e4d388/raw/fc31e41f8e1a6b713eafb9859f3f7e335939d518/data.json").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        return receive_data()
    else:
        return get_contact_page()


@app.route("/post/<int:pg_id>")
def post(pg_id):
    return render_template("post.html", post_det=posts[pg_id])


@app.post("/contact")
def receive_data():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    print(f"{name}\n{email}\n{phone}\n{message}")
    return render_template("contact.html", pg_type=2)


@app.get("/contact")
def get_contact_page():
    return render_template("contact.html", pg_type=1)


if __name__ == "__main__":
    app.run(debug=True)
