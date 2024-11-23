function modify_self_introduction() {
  // 기본 프로필 카드 숨기기
  const basicCard = document.querySelector('.user-profile-card-basic');
  if (basicCard) {
    basicCard.style.display = 'none';
  }

  // 수정용 프로필 카드 보이기
  const modifyCard = document.querySelector('.user-profile-card-modify');
  if (modifyCard) {
    modifyCard.style.display = 'block';
  }
}

document.getElementById('fileInput').addEventListener('change', function (event) {
  const file = event.target.files[0]; // 선택한 파일
  const maxSize = 2 * 1024 * 1024; // 2MB 제한 (단위: 바이트)

  // 오류 메시지를 표시할 요소 선택
  const errorMessage = document.getElementById('errorMessage');

  // 파일 형식 검증
  if (!file.type.startsWith('image/')) {
    errorMessage.textContent = '이미지 파일만 업로드 가능합니다.';
    event.target.value = ''; // 입력 필드 초기화
    return;
  }

  // 파일 크기 검증
  if (file.size > maxSize) {
    errorMessage.textContent = '파일 크기가 2MB를 초과할 수 없습니다.';
    event.target.value = ''; // 입력 필드 초기화
    return;
  }

  // 파일이 유효한 경우
  errorMessage.textContent = ''; // 오류 메시지 초기화
  alert('파일이 성공적으로 선택되었습니다.');
});

