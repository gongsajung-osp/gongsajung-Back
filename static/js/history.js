window.onload = function () {
    var DeliStatus = document.getElementsByClassName('deli-status');
    var ReviewBtn = document.getElementsByClassName('review-write-btn');

    for (var i = 0; i < DeliStatus.length; i++) {
        if (DeliStatus[i].textContent.trim() == '배송 완료') {
            ReviewBtn[i].style.display = 'inline-block';
            DeliStatus[i].style.color = '#fea84d';
        } else {
            ReviewBtn[i].style.display = 'none';
        }
    }
}

// 구매 데이터 받기
window.onload = function() {

    const contentName = localStorage.getItem("movedName");
    const contentCategory = localStorage.getItem("movedCategory");
    const contentPrice = localStorage.getItem("movedPrice");

    if (contentName && contentCategory && contentPrice) {
        document.getElementById("item-test").style.display = "block";
        document.getElementById("received-name").textContent = contentName;
        document.getElementById("received-category").textContent = contentCategory;
        document.getElementById("received-price").textContent = contentPrice;
    }
}
