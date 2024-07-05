const userId = document.querySelector('.putuserId');
const userPass = document.querySelector('.putuserpass');
const userPassRe = document.querySelector('.putuserpassre');
const ModifyButton = document.querySelector('.ModifyButton');
const wrongMsg = document.querySelector('.wrongMsg');

const checkAllFull = () => {
    if (userId.value !== '' && userPass.value !== '' && userPassRe.value !== '') {
        ModifyButton.classList.add('full');
    } else {
        ModifyButton.classList.remove('full');
    }
};

userId.addEventListener('input', checkAllFull);
userPass.addEventListener('input', checkAllFull);
userPassRe.addEventListener('input', checkAllFull);

// 비밀번호 삭제 버튼 

function deletePass() {
    userPass.value = '';
}

function deletePassRe() {
    userPassRe.value = '';
}

// 비밀번호 일치 여부
function checkPasswordMatch() {
    if (userPass.value !== userPassRe.value) {
        wrongMsg.textContent = '비밀번호가 일치하지 않습니다.'
    } else {
        wrongMsg.textContent = ''
    }
}

userPass.addEventListener('change', checkPasswordMatch)
userPassRe.addEventListener('change', checkPasswordMatch)

function checkInput() {
    if (userId.value === '' || userPass.value === '' || userPassRe.value === '') {
        alert('내용을 모두 입력해주세요!');
        return false;
    }
    return true;
}

function showPass() {
    const currentType = userPass.getAttribute('type');
    userPass.setAttribute('type', currentType === 'password' ? 'text' : 'password');

    const togglePassImg = document.getElementById('togglePassImg');
    console.log(togglePassImg)
    togglePassImg.setAttribute('src', currentType === 'password' ? '../../static/assets/img/password_show.svg' : '../../static/assets/img/password.svg');
    togglePassImg.classList.add('show_passwordImg')
}

function showPassRe() {
    const currentType = userPassRe.getAttribute('type');
    userPassRe.setAttribute('type', currentType === 'password' ? 'text' : 'password');

    const togglePassReImg = document.getElementById('togglePassReImg');
    togglePassReImg.setAttribute('src', currentType === 'password' ? '../../static/assets/img/password_show.svg' : '../../static/assets/img/password.svg');
    togglePassReImg.classList.add('show_passwordImg')
}