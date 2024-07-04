// 전체 동의 체크박스 함수입니다.
const allAgreeCheckbox = document.getElementById('allAgree');
const checkboxes = document.querySelectorAll('.checkbox-item input[type="checkbox"]:not(#allAgree)');

allAgreeCheckbox.addEventListener('change', function () {
    checkboxes.forEach(checkbox => {
        checkbox.checked = this.checked;
    });
});

checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', function () {
        if (!this.checked) {
            allAgreeCheckbox.checked = false;
        } else if (Array.from(checkboxes).every(cb => cb.checked)) {
            allAgreeCheckbox.checked = true;
        }
    });
});
