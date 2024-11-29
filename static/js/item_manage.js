
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
  