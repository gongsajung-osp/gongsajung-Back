document.getElementById("submit-btn").onclick = function () {
    // event.preventDefault();
    
    const contentName2 = document.getElementById("moveName2").textContent;
    localStorage.setItem("movedName2", contentName2);
  
    const contentCategory2 = document.getElementById("moveCategory2").textContent;
    localStorage.setItem("movedCategory2", contentCategory2);
  
    const contentPrice2 = document.getElementById("movePrice2").textContent;
    localStorage.setItem("movedPrice2", contentPrice2);
  
    const contentImage2 = document.querySelector(".product-image2 img").src;
    localStorage.setItem("movedImage2", contentImage2);
    
    // window.location.href = "/index";
}