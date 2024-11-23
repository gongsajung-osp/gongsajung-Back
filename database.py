import pyrebase
import json


class DBhandler:
    def __init__(self):
        with open("./authentication/firebase_auth.json") as f:
            config = json.load(f)

        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()
        self.storage = firebase.storage()

    def insert_item(self, name, data, img_path):
    # 데이터 삽입
        item_info = {
            "product_category": data.get("product_category", ""),
            "event_name": data.get("event_name", ""),
            "product_explain": data.get("product_explain", ""),
            "product_price": data.get("product_price", 0),
            "delivery_methods": data.get("delivery_methods", ["직거래"]),  # 이미 리스트 형태로 처리됨
            "seller_phone": data.get("seller_phone", ""),
            "seller_nickname": data.get("seller_nickname", "unknown"),
            "img_path": img_path,
        }
        self.db.child("item").child(name).set(item_info)
        print(item_info)
        return True


    def insert_user(self, data):
        if self.user_duplicate_check(data["user_id"]):  # 중복 확인
            user_info = {
                "user_id": data["user_id"],
                "password": data["password"],
                "email": data["email"],
                "phone": data["phone"],
                "verification_code": data["verification_code"],
            }
            self.db.child("user").push(user_info)  # Firebase에 데이터 저장
            print(user_info)
            return True
        else:
            return False

    def user_duplicate_check(self, id_string):
        users = self.db.child("user").get()

        print("users###", users.val())
        if str(users.val()) == "None":  # first registration
            return True
        else:
            for res in users.each():
                value = res.val()

                if value["user_id"] == id_string:
                    return False
            return True

    def find_user(self, id_, pw_):
        users = self.db.child("user").get()
        target_value = []
        for res in users.each():
            value = res.val()

            if value["user_id"] == id_ and value["password"] == pw_:
                return True

        return False

    def get_items(self):
        items = self.db.child("item").get()  # Firebase에서 아이템 가져오기
        if items.val() is None:
            return []  # 빈 리스트 반환
        else:
            return items.val()  # Firebase에서 가져온 데이터를 그대로 반환

    
    def get_item_byname(self, name):
        items = self.db.child("item").get()
        target_value = ""
        print("###########", name)
        for res in items.each():
            key_value = res.key()

            if key_value == name:
                target_value = res.val()
        return target_value
    
    def insert_review(self, item_name, review_data):
        #특정 상품에 리뷰 추가
        self.db.child("reviews").child(item_name).push(review_data)
        return True
    
    def get_reviews_by_item(self, item_name):
        #특정 상품의 리뷰 가져오기
        reviews=self.db.child("reviews").child(item_name).get()
        if reviews.val() is None:
            return []
        return [review.val() for review in reviews.each()]