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
    reviews = DB.db.child("review").get().val()
    return render_template("review.html",reviews=reviews)


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
    
    return render_template("reg_item.html")


# main/sub category, price 추가로 넘겨야 함


@application.route("/submit_item_post", methods=["POST"])
def reg_item_submit_post():
    # 상품 이미지 처리
    image_file = request.files.get("product_image")
    if image_file:
        image_file.save(f"static/images/{image_file.filename}")
        img_path = f"static/images/{image_file.filename}"
    else:
        img_path = None  # 이미지 업로드가 선택 사항이라면 None 처리

    # 폼 데이터 복사 및 수정 가능하게 변환
    data = request.form.to_dict()  # ImmutableMultiDict를 일반 딕셔너리로 변환
    data["delivery_methods"] = request.form.getlist("delivery_methods[]") or ["직거래"]  # 기본값 설정

    # 데이터베이스 삽입
    DB.insert_item(data["product_name"], data, img_path)

    # 결과 페이지 렌더링
    return render_template(
        "submit_item_result.html",
        data=data,
        img_path=img_path,
    )




if __name__ == "__main__":
    application.run(host="0.0.0.0", debug=True)


@application.route("/submit_review", methods=["POST"])
def submit_review():
    # 폼 데이터 가져오기
    order_id = request.form.get("order_id")
    item_name = request.form.get("item_name")
    rating = request.form.get("rating")
    review_text = request.form.get("review_text")
    review_image = request.files.get("review_image")

    if review_image:
        from werkzeug.utils import secure_filename
        image_filename = secure_filename(review_image.filename)
        image_path = f"static/images/reviews/{image_filename}"
        review_image.save(image_path)
    else:
        image_path = None

    review_data = {
        "user_id": session.get("user_id"),
        "item_name": item_name,
        "rating": int(rating),
        "review_text": review_text,
        "review_image": image_path,
    }
    DB.db.child("reviews").push(review_data)

    # 주문 상태 업데이트
    DB.db.child("orders").child(order_id).update({"is_reviewed": True})

    flash("리뷰가 성공적으로 등록되었습니다!")
    return redirect(url_for("view_history"))


@application.route("/write_review/<order_id>")
def write_review(order_id):
    # 주문 정보 가져오기
    order_data = DB.db.child("orders").child(order_id).get().val()

    if not order_data:
        flash("주문 정보를 찾을 수 없습니다.")
        return redirect(url_for("view_history"))

    return render_template("reg_reviews.html", order=order_data)
