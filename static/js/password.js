document.addEventListener('DOMContentLoaded', function() {
    const toggleButtons = document.querySelectorAll('.toggle-password');

    toggleButtons.forEach(button => {
        const input = button.parentElement.previousElementSibling;
        
        if (input && input.tagName === 'INPUT') {
            button.innerHTML = '<img src="../static/assets/img/passwordshow.svg" alt="show">';
            button.addEventListener('click', function() {
                togglePassword(input, button);
            });
        } else {
            console.error('No input found for the toggle button');
        }
    });
});

// 비밀번호 보이기 가리기
function togglePassword(input, button) {
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
