// 댓글창 보이게
document.querySelectorAll(".react-comment").forEach((commentButton, index) => {
  commentButton.addEventListener("click", function () {
    const viewComment = document.querySelectorAll(".view-comment")[index];

    if (viewComment) {
      if (viewComment.style.display === "none" || !viewComment.style.display) {
        viewComment.style.display = "block";
      } else {
        viewComment.style.display = "none";
      }
    }
  });
});

//tab 전환
const tabs = document.querySelectorAll(".tab");

tabs.forEach((tab) => {
  tab.addEventListener("click", function () {
    tabs.forEach((t) => t.classList.remove("tab-active"));
    this.classList.add("tab-active");
  });
});

function showTab(tabId, event) {
  const contents = document.querySelectorAll(".tab-content");
  contents.forEach((content) => {
    content.style.display = "none";
  });

  const activeTab = document.getElementById(tabId);
  if (activeTab) {
    activeTab.style.display = "block";
  }
}

//연관상품
const relativeProduct = document.querySelector(".relative-product");

function updateRightValue() {
  const windowWidth = window.innerWidth;

  if (windowWidth > 1024) {
    relativeProduct.style.right = "210px";
  } else if (windowWidth > 768) {
    relativeProduct.style.right = "50px";
  } else {
    relativeProduct.style.right = "50px";
  }
}

updateRightValue();

window.addEventListener("resize", updateRightValue);

//구매 팝업
document.getElementById("purchase-btn").onclick = function () {
  document.getElementById("purchase-popup1").style.display = "block";
};

//구매 확정 - 구매 아이템 데이터 전송
document.getElementById("confirm-purchase").onclick = function () {
  const contentName = document.getElementById("moveName").textContent;
  localStorage.setItem("movedName", contentName);

  const contentCategory = document.getElementById("moveCategory").textContent;
  localStorage.setItem("movedCategory", contentCategory);

  const contentPrice = document.getElementById("movePrice").textContent;
  localStorage.setItem("movedPrice", contentPrice);

  const contentImage = document.querySelector(".product-image img").src;
  localStorage.setItem("movedImage", contentImage);

  document.getElementById("purchase-popup1").style.display = "none";
  document.getElementById("purchase-popup2").style.display = "block";
  setTimeout(function () {
    document.getElementById("purchase-popup2").style.display = "none";
  }, 2000);
  confirmPurchase();
};

document.getElementById("cancel-purchase").onclick = function () {
  document.getElementById("purchase-popup1").style.display = "none";
};

//좋아요

function showHeart() {
  const name = $("#heart").data("name"); //추가코드

  $.ajax({
    type: "GET",
    url: "/show_heart/" + encodeURIComponent(name) + "/",
    data: {},
    success: function (response) {
      let my_heart = response["my_heart"];
      if (my_heart["interested"] == "Y") {
        $("#heart").css("color", "red");
        $("#heart").attr("onclick", "unlike()");
      } else {
        $("#heart").css("color", "grey");
        $("#heart").attr("onclick", "like()");
      }
      //alert("showheart!")
    },
  });
}
function like() {
  const name = $("#heart").data("name"); //추가

  $("#heart").css("color", "red"); //추가
  $("#heart").off("click").on("click", unlike);

  $.ajax({
    type: "POST",
    url: "/like/" + encodeURIComponent(name) + "/",
    data: {
      interested: "Y",
    },
    success: function (response) {
      alert(response["msg"]);
      window.location.reload();
    },
  });
}
function unlike() {
  const name = $("#heart").data("name");

  $("#heart").css("color", "grey");
  $("#heart").off("click").on("click", like);

  $.ajax({
    type: "POST",
    url: "/unlike/" + encodeURIComponent(name) + "/",
    data: {
      interested: "N",
    },
    success: function (response) {
      alert(response["msg"]);
      window.location.reload();
    },
  });
}
$(document).ready(function () {
  showHeart();
});
