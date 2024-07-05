let previousInputElement = null;
const userId = document.querySelector('.userId input');
const userEmail = document.querySelector('.userEmail input');
const userName = document.querySelector('.userName input');
const userPhone = document.querySelector('.userPhone input');
const userBirth = document.querySelector('.userBirth input');
const modifyBtn = document.querySelector('.modifybtn');

document.addEventListener('DOMContentLoaded', function () {
    const userId = document.querySelector('.userId input');
    const userEmail = document.querySelector('.userEmail input');
    const userName = document.querySelector('.userName input');
    const userPhone = document.querySelector('.userPhone input');
    const userBirth = document.querySelector('.userBirth input');

    function checkFields() {
        // 각 입력 필드의 값이 비어 있는지 확인
        const useridFilled = userId.value.trim() !== '';
        const userEmailFilled = userEmail.value.trim() !== '';
        const userNameFilled = userName.value.trim() !== '';
        const userPhoneFilled = userPhone.value.trim() !== '';
        const userBirthFilled = userBirth.value.trim() !== '';
        
        if (useridFilled || userEmailFilled || userNameFilled || userPhoneFilled || userBirthFilled) {
            modifyBtn.classList.remove('bin');
        } else {
            modifyBtn.classList.add('bin');
        }
    }

    userId.addEventListener('input', checkFields);
    userEmail.addEventListener('input', checkFields);
    userName.addEventListener('input', checkFields);
    userPhone.addEventListener('input', checkFields);
    userBirth.addEventListener('input', checkFields);
    checkFields();
});

modifyBtn.addEventListener('click', () => {
    if(modifyBtn.classList[1] === 'bin'){
        alert('모든 빈칸을')
    }
})

document.querySelectorAll('.modify').forEach(modifyElement => {
    modifyElement.addEventListener('click', () => {
        if (previousInputElement) {
            previousInputElement.style.border = '';
        }

        const inputElement = modifyElement.querySelector('input');
        if (inputElement) {
            inputElement.style.border = '0';
            previousInputElement = inputElement;
        }
    });
});
