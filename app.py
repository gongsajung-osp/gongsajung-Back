from flask import Flask, render_template, request, flash, redirect, url_for, session
from database import DBhandler
import hashlib
import sys

application = Flask(__name__)
application.config["SECRET_KEY"] = "helloosp"

DB = DBhandler()


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


@application.route("/login_confirm", methods=["POST"])
def login_user():
    id_ = request.form["user_id"]
    pw = request.form["password"]
    pw_hash = hashlib.sha256(pw.encode("utf-8")).hexdigest()

    if DB.find_user(id_, pw_hash):
        session["user_id"] = id_
        return redirect(url_for("view_index"))
    else:
        flash("Wrong ID or PW!")
        return render_template("login.html")


@application.route("/logout")
def logout_user():
    session.clear()
    return redirect(url_for("view_landing"))


@application.route("/item")
def view_item():
    return render_template("item.html")


@application.route("/signup")
def view_signup():
    return render_template("signup.html")


@application.route("/signup_post", methods=["POST"])
def register_user():
    data = request.form.to_dict()  # HTML 폼 데이터를 딕셔너리로 변환
    data["phone"] = (
        f"{data['phone-prefix']}-{data['phone-middle']}-{data['phone-suffix']}"  # 전화번호 병합
    )
    del (
        data["phone-prefix"],
        data["phone-middle"],
        data["phone-suffix"],
    )  # 병합 후 불필요한 키 삭제
    del data["confirm_password"]  # confirm_password는 서버에 저장할 필요 없음

    pw_hash = hashlib.sha256(data["password"].encode("utf-8")).hexdigest()
    data["password"] = pw_hash  # 비밀번호를 해시로 변환

    if DB.insert_user(data):  # 데이터베이스에 사용자 정보 저장
        return render_template("login.html")
    else:
        flash("user id already exists!")
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

@application.route("/profile")
def view_profile():
    return render_template("profile.html")

@application.route("/item_manage")
def manage_item():
    return render_template("item_manage.html")

@application.route("/submit_item")
def reg_item_submit():
    name = request.args.get("name")
    seller = request.args.get("seller")
    addr = request.args.get("addr")
    email = request.args.get("email")
    category = request.args.get("category")
    card = request.args.get("card")
    status = request.args.get("status")
    phone = request.args.get("phone")
    print(name, seller, addr, email, category, card, status, phone)
    # return render_template("reg_item.html")


# main/sub category, price 추가로 넘겨야 함


@application.route("/submit_item_post", methods=["POST"])
def reg_item_submit_post():
    image_file = request.files["file"]
    image_file.save("static/images/{}".format(image_file.filename))
    data = request.form
    DB.inset_item(data["product_name"], data, image_file.filename)

    return render_template(
        "submit_item_result.html",
        data=data,
        img_path="static/images/{}".format(image_file.filename),
    )



if __name__ == "__main__":
    application.run(host="0.0.0.0", debug=True)
