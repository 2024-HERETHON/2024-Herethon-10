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

function togglePassword(inputId, button) {
    const input = document.getElementById(inputId);
    if (input.type === "password") {
        input.type = "text";
        button.innerHTML = '<img src="../static/assets/img/password.svg" alt="hide">';
    } else {
        input.type = "password";
        button.innerHTML = '<img src="../static/assets/img/passwordshow.svg" alt="show">';
    }
}