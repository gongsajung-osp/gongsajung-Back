window.onload = function() {
  const contentName2 = localStorage.getItem("movedName2");
  const contentCategory2 = localStorage.getItem("movedCategory2");
  const contentPrice2 = localStorage.getItem("movedPrice2");
  const contentImage2 = localStorage.getItem("movedImage2");

  if (contentName2 && contentCategory2 && contentPrice2 && contentImage2) {
      document.getElementById("item-test").style.display = "block";
      document.getElementById("received-name").textContent = contentName2;
      document.getElementById("received-category").textContent = contentCategory2;
      document.getElementById("received-price").textContent = contentPrice2;
      document.getElementById("received-img").src = contentImage2;
  }
}

// document.addEventListener("DOMContentLoaded", function () {
//     const contentName2 = localStorage.getItem("movedName2");
//     const contentCategory2 = localStorage.getItem("movedCategory2");
//     const contentPrice2 = localStorage.getItem("movedPrice2");
//     const contentImage2 = localStorage.getItem("movedImage2");
  
//     if (contentName2 && contentCategory2 && contentPrice2 && contentImage2) {
//         document.getElementById("item-test").style.display = "block";
//         document.getElementById("received-name").textContent = contentName2;
//         document.getElementById("received-category").textContent = contentCategory2;
//         document.getElementById("received-price").textContent = contentPrice2;
//         document.getElementById("received-img").src = contentImage2;
//     }
//   });
  

document.querySelectorAll('.delete-btn').forEach(button => {
button.addEventListener('click', function () {
    const itemElement = this.closest('.history-item');
    const itemName = itemElement.querySelector('.purchased-name').textContent;

    if (confirm(`${itemName}을(를) 삭제하시겠습니까?`)) {
        fetch(`/delete_item?item_name=${encodeURIComponent(itemName)}`, {
            method: 'GET', // GET 요청
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert(data.message);
                    // 화면에서 삭제
                    itemElement.remove();
                } else {
                    alert(data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('삭제 요청 중 오류가 발생했습니다.');
            });
    }
});
});
