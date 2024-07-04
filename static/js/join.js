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

// 공통 유효성 검사 함수
function validateField(fieldId, errorId, minLen, checkFunc) {
    const field = document.getElementById(fieldId);
    const error = document.getElementById(errorId);
    const checkmark = field.parentNode.querySelector('.checkmark');
    const wrongmark = field.parentNode.querySelector('.wrongmark');
    let isValid = true;

    if (field.value.length < minLen || (checkFunc && !checkFunc(field.value))) {
        error.style.display = 'block';
        field.classList.add('error-border');
        field.classList.remove('valid');
        checkmark.style.display = 'none';
        wrongmark.style.display = 'block';
        isValid = false;
    } else {
        error.style.display = 'none';
        field.classList.remove('error-border');
        field.classList.add('valid');
        checkmark.style.display = 'block';
        wrongmark.style.display = 'none';
    }
    return isValid;
}

function validatePasswordMatch() {
    const userPassword = document.getElementById('userPassword');
    const userPasswordre = document.getElementById('userPasswordre');
    const userPasswordreError = document.getElementById('userPasswordreError');
    const userPasswordreEmptyError = document.getElementById('userPasswordreEmptyError');
    const userPasswordreCheckmark = userPasswordre.parentNode.querySelector('.checkmark');
    const userPasswordreWrongmark = userPasswordre.parentNode.querySelector('.wrongmark');
    let isValid = true;

    if (userPasswordre.value === '') {
        userPasswordreEmptyError.style.display = 'block';
        userPasswordreError.style.display = 'none';
        userPasswordre.classList.add('error-border');
        userPasswordre.classList.remove('valid');
        userPasswordreCheckmark.style.display = 'none';
        userPasswordreWrongmark.style.display = 'block';
        isValid = false;
    } else if (userPasswordre.value !== userPassword.value) {
        userPasswordreEmptyError.style.display = 'none';
        userPasswordreError.style.display = 'block';
        userPasswordre.classList.add('error-border');
        userPasswordre.classList.remove('valid');
        userPasswordreCheckmark.style.display = 'none';
        userPasswordreWrongmark.style.display = 'block';
        isValid = false;
    } else {
        userPasswordreEmptyError.style.display = 'none';
        userPasswordreError.style.display = 'none';
        userPasswordre.classList.remove('error-border');
        userPasswordre.classList.add('valid');
        userPasswordreCheckmark.style.display = 'block';
        userPasswordreWrongmark.style.display = 'none';
    }
    return isValid;
}

function validateBirthDate() {
    const userBirth = document.getElementById('userBirth');
    const userBirthCheckmark = userBirth.parentNode.querySelector('.checkmark');
    const userBirthError = document.getElementById('userBirthError');
    const birthPattern = /^\d{4}-\d{2}-\d{2}$/;

    if (userBirth.value === '') {
        userBirth.classList.remove('error-border', 'valid');
        userBirthError.style.display = 'none';
        userBirthCheckmark.style.display = 'none';
    } else if (!birthPattern.test(userBirth.value)) {
        userBirth.value = ''; // 잘못된 형식일 경우 입력값 초기화
        userBirth.classList.add('error-border');
        userBirth.classList.remove('valid');
        userBirthError.style.display = 'block';
        userBirthCheckmark.style.display = 'none';
    } else {
        userBirth.classList.remove('error-border');
        userBirth.classList.add('valid');
        userBirthError.style.display = 'none';
        userBirthCheckmark.style.display = 'block';
    }
}

function validate() {
    let isValid = true;

    isValid &= validateField('userId', 'userIdError', 6);
    isValid &= validateField('userEmail', 'userEmailError', 1, value => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value));
    isValid &= validateField('userPassword', 'userPasswordError', 8);
    isValid &= validateField('userPhone', 'userPhoneError', 10, value => /^[0-9]{10,11}$/.test(value) && !value.includes('-'));
    isValid &= validateField('userName', 'userNameError', 1);
    isValid &= validatePasswordMatch();
    validateBirthDate();

    const joinButton = document.querySelector('.joinbtn');
    if (!isValid) {
        joinButton.classList.add('joinbtn-disabled');
    } else {
        joinButton.classList.remove('joinbtn-disabled');
    }
    return Boolean(isValid);
}

// 폼 제출 이벤트 리스너
document.forms['login'].addEventListener('submit', function(event) {
    if (!validate()) {
        event.preventDefault();
    }
});

// 모든 입력 필드에 이벤트 리스너 추가 (처음에 유효성 검사 실행되지 않도록 수정)
const inputs = document.querySelectorAll('input');
inputs.forEach(input => {
    input.addEventListener('input', function() {
        document.querySelector('.joinbtn').classList.remove('joinbtn-disabled');
    });
});

const joinButton = document.querySelector('.joinbtn');
joinButton.addEventListener('click', function(event) {
    validate();
});

// clearInput 함수
function clearInput(inputId) {
    const input = document.getElementById(inputId);
    input.value = '';
    input.classList.remove('error-border', 'valid');
    const errorElement = document.getElementById(inputId + 'Error');
    if (errorElement) {
        errorElement.style.display = 'none';
    }
    const duplicateErrorElement = document.getElementById(inputId + 'DuplicateError');
    if (duplicateErrorElement) {
        duplicateErrorElement.style.display = 'none';
    }
    const checkmark = input.parentNode.querySelector('.checkmark');
    const wrongmark = input.parentNode.querySelector('.wrongmark');
    if (checkmark) {
        checkmark.style.display = 'none';
    }
    if (wrongmark) {
        wrongmark.style.display = 'none';
    }
}

// 중복 체크 함수 예시 (실제 구현 필요)
function checkEmailDuplicate(email) {
    // 이메일 중복 체크 로직 구현
    return false; // 예시로 중복이 없다고 가정
}

function checkPhoneDuplicate(phone) {
    // 전화번호 중복 체크 로직 구현
    return false; // 예시로 중복이 없다고 가정
}
