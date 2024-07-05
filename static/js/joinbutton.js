document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('myForm');
    const inputs = form.querySelectorAll('input');
    const submitButton = document.getElementById('submitButton');

    function checkInputs() {
        let allFilled = true;

        inputs.forEach(input => {
            if (input.value.trim() === '') {
                allFilled = false;
            }
        });

        if (allFilled) {
            submitButton.classList.remove('joinbtn-disabled');
            submitButton.classList.add('joinbtn-enabled');
        } else {
            submitButton.classList.remove('joinbtn-enabled');
            submitButton.classList.add('joinbtn-disabled');
        }
    }

    inputs.forEach(input => {
        input.addEventListener('input', checkInputs);
    });

    // 처음 로드 시에도 한 번 확인
    checkInputs();
});