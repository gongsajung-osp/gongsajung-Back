from flask import Flask, render_template, request
from database import DBhandler
import sys

application = Flask(__name__)

DB = DBhandler

@application.route("/")
def start():
    return render_template("reg_items.html")

@application.route("/landing")
def view_landing():
    return render_template("landing.html")

@application.route("/base")
def view_base():
    return render_template("base.html")

@application.route("/index")
def view_index():
    return render_template("index.html")

@application.route("/login")
def view_login():
    return render_template("login.html")

@application.route("/item")
def view_item():
    return render_template("item.html")

@application.route("/signup")
def view_signup():
    return render_template("signup.html")

@application.route("/review")
def view_review():
    return render_template("review.html")

@application.route("/reg_items")
def reg_item():
    return render_template("reg_items.html")

@application.route("/reg_reviews")
def reg_review():
    return render_template("reg_reviews.html")

@application.route("/history")
def view_history():
    return render_template("history.html")

@application.route("/submit_item")
def reg_item_submit():
    name=request.args.get("name")
    seller=request.args.get("seller")
    addr=request.args.get("addr")
    email=request.args.get("email")
    category=request.args.get("category")
    card=request.args.get("card")
    status=request.args.get("status")
    phone=request.args.get("phone")
    print(name,seller,addr,email,category,card,status,phone)
    #return render_template("reg_item.html")    
#main/sub category, price 추가로 넘겨야 함

@application.route("/submit_item_post", methods=['POST'])
def reg_item_submit_post():
    image_file=request.files["file"]
    image_file.save("static/images/{}".format(image_file.filename))
    data=request.form
    DB.inset_item(data['name'], data, image_file.filename)
    
    return render_template("submit_item_result.html", data=data, img_path="static/images/{}".format(image_file.filename))

if __name__=="__main__":
    application.run(host='0.0.0.0',debug=True)