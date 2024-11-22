function settingToggleDropdown(event) {
  event.preventDefault();

  const dropdownItems = Array.from(document.querySelectorAll('.dropdown-setting li'));
  const isVisible = dropdownItems[0].style.visibility === 'visible';

  if (isVisible) {
    dropdownItems.forEach(item => {
      item.style.visibility = 'hidden';
    });
  } else {
    dropdownItems.reverse().forEach((item, index) => {
      setTimeout(() => {
        item.style.visibility = 'visible';
      }, index * 20);
    });
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

document.querySelectorAll('.nav-item').forEach(item => {
  const button = item.querySelector('button');
  const dropdown = item.querySelector('.dropdown');

  // 버튼 클릭 시 드롭다운 표시
  button.addEventListener('click', (event) => {
    event.stopPropagation(); // 이벤트 버블링 방지

    // 다른 드롭다운을 모두 닫고 현재 드롭다운만 토글
    document.querySelectorAll('.dropdown').forEach(d => {
      d.style.display = 'none';
    });
    dropdown.style.display = 'block';
  });

  // 다른 nav-item을 호버할 때 드롭다운 닫기
  item.addEventListener('mouseenter', () => {
    document.querySelectorAll('.dropdown').forEach(d => {
      d.style.display = 'none';
    });
    dropdown.style.display = 'block'; // 현재 드롭다운만 표시
  });
});

// 문서의 다른 곳을 클릭 시 드롭다운 숨김
document.addEventListener('click', (event) => {
  document.querySelectorAll('.dropdown').forEach(d => {
    d.style.display = 'none';
  });
});










document.querySelectorAll('.nav-item').forEach(item => {
  const button = item.querySelector('button');
  const dropdown = item.querySelector('.dropdown-nav');
  let hideTimeout;

  // 마우스가 들어왔을 때 드롭다운 표시
  item.addEventListener('mouseenter', () => {
    clearTimeout(hideTimeout); // hideTimeout 초기화
    dropdown.style.display = 'block';
  });

  // 마우스가 떠날 때 2초 후에 드롭다운 숨기기
  item.addEventListener('mouseleave', () => {
    hideTimeout = setTimeout(() => {
      dropdown.style.display = 'none';
    }, 2000); // 2초 후 드롭다운 숨김
  });

  // 드롭다운 항목 클릭 시 이벤트 버블링 방지
  dropdown.addEventListener('click', (event) => {
    event.stopPropagation();
  });
});

// 문서의 다른 부분을 클릭 시 모든 드롭다운 숨김
document.addEventListener('click', () => {
  document.querySelectorAll('.dropdown-nav').forEach(d => {
    d.style.display = 'none';
  });
});

function settingToggleDropdown(event) {
  const bubble = document.getElementById('bubble');

  // `display` 속성이 'none'인지 확인하고 토글
  if (bubble.style.display === 'none' || bubble.style.display === '') {
    bubble.style.display = 'block'; // 보이기
  } else {
    bubble.style.display = 'none'; // 숨기기
  }
}
