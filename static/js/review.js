// 댓글창 보이게
document.querySelectorAll('.react-comment').forEach((commentButton, index) => {
  commentButton.addEventListener('click', function () {
    const viewComment = document.querySelectorAll('.view-comment')[index];

    if (viewComment) {
      if (viewComment.style.display === 'none' || !viewComment.style.display) {
        viewComment.style.display = 'block';
      } else {
        viewComment.style.display = 'none';
      }
    }
  });
});


//tab 전환
const tabs = document.querySelectorAll('.tab');

tabs.forEach(tab => {
  tab.addEventListener('click', function () {
    tabs.forEach(t => t.classList.remove('tab-active'));
    this.classList.add('tab-active');
  })
});

function showTab(tabId, event) {
  const contents = document.querySelectorAll('.tab-content')
  contents.forEach(content => {
    content.style.display = 'none';
  });

  const activeTab = document.getElementById(tabId);
  if (activeTab) {
    activeTab.style.display = 'block';
  }

  const tabs = document.querySelectorAll('.tab');
  tabs.forEach(tab => {
    tab.classList.remove('active');
  });

  if (event) {
    event.currentTarget.classList.add('active');
  }
}


//연관상품
const relativeProduct = document.querySelector('.relative-product');

function updateRightValue() {
  const windowWidth = window.innerWidth;

  if (windowWidth > 1024) {
    relativeProduct.style.right = '210px';
  } else if (windowWidth > 768) {
    relativeProduct.style.right = '50px';
  } else {
    relativeProduct.style.right = '50px';
  }
}

updateRightValue();

window.addEventListener('resize', updateRightValue);