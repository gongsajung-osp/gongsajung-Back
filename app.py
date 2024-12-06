from flask import Flask, render_template, request, flash, redirect, url_for, session, jsonify
from database import DBhandler
import hashlib
import sys

application = Flask(__name__)
application.config["SECRET_KEY"] = "helloosp"

DB = DBhandler()


@application.route("/")
def start():
    return render_template('landing.html')

@application.route("/landing")
def view_landing():
    return render_template("landing.html")


@application.route("/base")
def view_base():
    return render_template("base.html")


@application.route("/index")
def view_index():
    items = DB.get_items() # DB 에서 모든 상품 조회
    return render_template("index.html",items=items)

@application.route("/index_sticker")
def view_sticker():
    return render_template("index_sticker.html")

@application.route("/index_stationery")
def view_stationery():
    return render_template("index_stationery.html")

@application.route("/index_postcard")
def view_postcard():
    return render_template("index_postcard.html")

@application.route("/index_ceramic")
def view_ceramic():
    return render_template("index_ceramic.html")

@application.route("/index_life")
def view_life():
    return render_template("index_life.html")

@application.route("/index_food")
def view_food():
    return render_template("index_food.html")

@application.route("/index_poster")
def view_poster():
    return render_template("index_poster.html")

@application.route("/index_glass")
def view_glass():
    return render_template("index_glass.html")

@application.route("/index_beads")
def view_beads():
    return render_template("index_beads.html")

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

@application.route("/review_tomato")
def view_review_tomato():
    return render_template("review_tomato.html")

@application.route("/reg_reviews_tomato")
def view_reg_reviews_tomato():
    return render_template("reg_reviews_tomato.html")

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


@application.route("/review/<product_name>")
def review(product_name):
    # 데이터베이스에서 상품 정보 가져오기
    product_details = DB.get_item_byname(product_name)
    
    if not product_details:
        # 상품이 없으면 오류 처리
        flash(f"상품 '{product_name}'을(를) 찾을 수 없습니다.")
        return redirect(url_for("view_index"))
    
    #reviews = DB.get_item_byname(product_name)
    reviews = DB.get_reviews_by_item(product_name)



    # review.html에 상품 데이터 전달
    return render_template(
        "review.html",
        name=product_name,
        price=product_details.get("product_price", "가격 미정"),
        img_path=product_details.get("img_path", "images/default.jpg"),
        product_explain=product_details.get("product_explain", "상세 설명이 없습니다."),
        shipping_cost=product_details.get("shipping_cost", "무료"),
        product_category=product_details.get("product_category", "카테고리 없음"),
        event_name=product_details.get("event_name", "행사 미정"),
        reviews=reviews, #추가한코드
        item_name=product_name #좋아요기능 추가코드
    )




@application.route("/reg_items")
def reg_item():
    return render_template("reg_items.html")


@application.route("/reg_reviews")
def reg_review():
    return render_template("reg_reviews.html")


@application.route("/history")
def view_history():
    # 로그인 여부 확인
    user_id = session.get("user_id")
    
    if not user_id:
        flash("로그인이 필요합니다.")  # 로그인 요구 메시지
        return redirect(url_for("view_login"))  # 로그인 페이지로 리디렉션
    
    # 로그인된 경우 Firebase에서 상품 데이터 가져오기
    items = DB.get_items()

    for item in items.values():
        # 'images/items/' 경로를 제거하고 파일명만 남기기
        item['img_path'] = item['img_path'].split('/')[-1]
    
    
    return render_template("history.html", items=items)


@application.route("/profile")
def view_profile():
    return render_template("profile.html")

@application.route("/item_manage")
def manage_item():
     # 로그인 여부 확인
    user_id = session.get("user_id")
    
    if not user_id:
        flash("로그인이 필요합니다.")  # 로그인 요구 메시지
        return redirect(url_for("view_login"))  # 로그인 페이지로 리디렉션
    
    # 로그인된 경우 Firebase에서 상품 데이터 가져오기
    items = DB.get_items()
    return render_template("item_manage.html", items=items)

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




@application.route("/delete_item")
def delete_item():
    item_name = request.args.get("item_name")  # 삭제 요청으로 전달받은 아이템 이름
    
    if not item_name:
        return jsonify({"success": False, "message": "아이템 이름이 제공되지 않았습니다."}), 400
    
    # Firebase에서 아이템 삭제
    success = DB.delete_item(item_name)
    if success:
        return jsonify({"success": True, "message": f"{item_name} 삭제 완료!"})
    else:
        return jsonify({"success": False, "message": "해당 아이템을 찾을 수 없습니다."}), 404




@application.route("/submit_item_post", methods=["POST"])
def reg_item_submit_post():
    # 상품 이미지 처리
    image_file = request.files.get("product_image")
    if image_file:
        image_file.save(f"static/images/{image_file.filename}")
        img_path = f"images/{image_file.filename}"
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
        "rating": rating,
        "review_text": review_text,
        "review_image": image_path,
    }

    DB.insert_review(item_name, review_data)

    flash("리뷰가 성공적으로 등록되었습니다!")
    return redirect(url_for("review",product_name=item_name))


@application.route("/write_review/<item_name>")
def write_review(item_name):
    db_handler = DBhandler()  # Firebase DB 핸들러 인스턴스 생성
    item_data = db_handler.get_item_byname(item_name)

    print("item_data", item_data)

    if not item_data:
        # 상품이 없을 경우
        flash("상품을 찾을 수 없습니다.")
        return redirect(url_for("view_history"))

    # `order` 객체 생성 (템플릿에서 사용하는 데이터)
    order_data = {
        "item_name": item_name,
        "item_image": item_data.get("img_path"),
        "order_date": "2024-11-24",  # 테스트용 데이터
        "delivery_date": "2024-11-26",  # 테스트용 데이터
        "item_options": "기본 옵션",  # 예시 데이터
        "order_id": "12345"  # 테스트 데이터
    }

    # `reg_reviews.html` 렌더링
    return render_template("reg_reviews.html", order=order_data)



def get_item_byname(self, name):
    items = self.db.child("item").get()  # Firebase `item` 노드 가져오기
    for res in items.each():
        if res.key() == name:  # 상품 이름과 키 비교
            return res.val()
    return None  # 데이터가 없을 경우 None 반환



@application.route("/buy_item", methods=["POST"])
def buy_item():
    #클라이언트로부터 전달받은 상품 ID 
    product_id = request.form.get("product_id")
    user_id = session.get("user_id") #현재 로그인된 사용자

    if not user_id:
        flash("로그인이 필요합니다.")
        return redirect(url_for("view_login"))
    
    purchase_data={
        "user_id": user_id,
        "product_id": product_id,
        "purchase_data": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "delivery_status":"배송 중",
    }

    try:
        DB.child("purchases").push(purchase_data)

        flash("구매가 완료되었습니다.")
        return redirect(url_for("view_history"))

    except Exception as e:
        # 에러 처리
        flash(f"구매 처리 중 문제가 발생했습니다: {str(e)}")
        return redirect(url_for("view_product", product_id=product_id))
    
#좋아요 기능
@application.route('/show_heart/<name>/', methods=['GET'])
def show_heart(name):
    print(f"Received name in show_heart: {name}") #디버깅
    my_heart = DB.get_heart_byname(session['user_id'],name) 
    return jsonify({'my_heart': my_heart})

@application.route('/like/<name>/', methods=['POST'])
def like(name):
    my_heart = DB.update_heart(session['user_id'],'Y',name)
    return jsonify({'msg': '좋아요 완료!'})

@application.route('/unlike/<name>/', methods=['POST'])
def unlike(name):
    my_heart = DB.update_heart(session['user_id'],'N',name) 
    return jsonify({'msg': '좋아요 취소 완료!'})
    

