import pyrebase
import json


class DBhandler:
    def __init__(self):
        with open("./authentication/firebase_auth.json") as f:
            config = json.load(f)

        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    def insert_item(self, name, data, img_path):
        # 키 값, 속성들, 대표 사진
        item_info = {
            "product_category": data["product_category"],
            "event_name": data["event_name"],
            "product_explain": data["product_explain"],
            "product_price": data["product_price"],
            "delivery_methods": (
                data["delivery_methods"]
                if isinstance(data["delivery_methods"], list)
                else [data["delivery_methods"]]
            ),
            "seller_phone": data["seller_phone"],
            "seller_nickname": data["seller_nickname"],
            "img_path": img_path,
        }
        self.db.child("item").child(name).set(item_info)
        # 테이블이름.키값.속성들
        print(data, img_path)
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
        items = self.db.child("item").get().val()
        return items

    def get_item_byname(self, name):
        items = self.db.child("item").get()
        target_value = ""
        print("###########", name)
        for res in items.each():
            key_value = res.key()

            if key_value == name:
                target_value = res.val()
        return target_value
