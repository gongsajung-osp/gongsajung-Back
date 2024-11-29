document.getElementById("submit-btn").onclick = function () {
    const contentName2 = document.getElementById("moveName").textContent;
    localStorage.setItem("movedName", contentName2);
  
    const contentCategory2 = document.getElementById("moveCategory").textContent;
    localStorage.setItem("movedCategory", contentCategory2);
  
    const contentPrice2 = document.getElementById("movePrice").textContent;
    localStorage.setItem("movedPrice", contentPrice2);
  
    const contentImage2 = document.querySelector(".product-image img").src;
    localStorage.setItem("movedImage", contentImage2);

}