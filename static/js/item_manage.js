//submit_item_result에서 데이터 받아오기
window.onload = function() {

    const contentName2 = localStorage.getItem("movedName");
    const contentCategory2 = localStorage.getItem("movedCategory");
    const contentPrice2 = localStorage.getItem("movedPrice");
    const contentImage2 = localStorage.getItem("movedImage");

    if (contentName2 && contentCategory2 && contentPrice2 && contentImage2) {
        document.getElementById("item-test").style.display = "block";
        document.getElementById("received-name").textContent = contentName2;
        document.getElementById("received-category").textContent = contentCategory2;
        document.getElementById("received-price").textContent = contentPrice2;
        document.getElementById("received-img").src = contentImage2;
    }
}


//상품 삭제
document.addEventListener("click", function (event) {
    
    if (event.target.classList.contains("delete-btn")) {
      const historyItem = event.target.closest(".history-item");
  
      const popup1 = document.getElementById("purchase-popup1");
      popup1.style.display = "block";
  
      document.getElementById("confirm-purchase").onclick = function () {
        if (historyItem) {
          historyItem.remove();
        }
        popup1.style.display = "none";
  
        const popup2 = document.getElementById("purchase-popup2");
        popup2.style.display = "block";
        setTimeout(function () {
          popup2.style.display = "none";
        }, 2000);
      };

      document.getElementById("cancel-purchase").onclick = function () {
        popup1.style.display = "none";
      };
    }
  });
