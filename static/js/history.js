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