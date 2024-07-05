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
            document.getElementById('id_new_password1').value = '';
        }

        function deletePassRe() {
            document.getElementById('id_new_password2').value = '';
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

        function showPass(inputId) {
            const inputField = document.getElementById(inputId);
            const currentType = inputField.getAttribute('type');
            inputField.setAttribute('type', currentType === 'password' ? 'text' : 'password');
        }

        function showPassRe(inputId) {
            const inputField = document.getElementById(inputId);
            const currentType = inputField.getAttribute('type');
            inputField.setAttribute('type', currentType === 'password' ? 'text' : 'password');
        }