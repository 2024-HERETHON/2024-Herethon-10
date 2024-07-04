let previousInputElement = null;
const userPass = document.querySelector('.putuserpass');
const userPassRe = document.querySelector('.putuserpassre');

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

document.getElementById('profileInput').addEventListener('change', function (event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            document.getElementById('profileImg').src = e.target.result;
        }
        reader.readAsDataURL(file);
    }
});