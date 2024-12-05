function settingToggleDropdown(event) {
  event.preventDefault();

  const bubbleImg = document.getElementById('bubble');
  const dropdownItems = Array.from(document.querySelectorAll('.dropdown-setting li'));
  const isVisible = dropdownItems[0].style.visibility === 'visible';

  if (isVisible) {
    dropdownItems.forEach(item => {
      item.style.visibility = 'hidden';
    });
    bubbleImg.style.visibility = 'hidden';
  } else {
    dropdownItems.reverse().forEach((item, index) => {
      setTimeout(() => {
        item.style.visibility = 'visible';
      }, index * 20);
    });
    bubbleImg.style.visibility = 'visible';
  }
}

window.addEventListener('click', function (e) {
  const dropdownMenu = document.querySelector('.dropdown-menu');
  if (!e.target.closest('.setting')) {
    const dropdownItems = dropdownMenu.querySelectorAll('li');
    dropdownItems.forEach(item => {
      item.style.visibility = 'hidden';
    });
  }
});

// const navs = document.querySelectorAll(".nav");

// navs.forEach((nav) => {
//   nav.addEventListener("click", function () {
//     navs.forEach((t) => t.classList.remove("nav-active"));
//     this.classList.add("nav-active");
//   });
// });