document.addEventListener('DOMContentLoaded', function() {
    const toggleButtons = document.querySelectorAll('.toggle-password');

    toggleButtons.forEach(button => {
        const inputId = button.previousElementSibling.previousElementSibling.id;
        button.innerHTML = '<img src="../static/assets/img/passwordshow.svg" alt="show">'; // 초기 상태 설정
        button.addEventListener('click', function() {
            togglePassword(inputId, button);
        });
    });
});

// 비밀번호 보이기 가리기
function togglePassword(inputId, button) {
    const input = document.getElementById(inputId);
    const icon = button.querySelector('img');
    
    if (input.type === "password") {
        input.type = "text";
        icon.src = "../static/assets/img/password.svg";
        icon.alt = "hide";
    } else {
        input.type = "password";
        icon.src = "../static/assets/img/passwordshow.svg";
        icon.alt = "show";
    }
}
