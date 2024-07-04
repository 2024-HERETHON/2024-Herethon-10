document.addEventListener('DOMContentLoaded', function() {
    const profileBtn = document.querySelector('.profilebtn');
    const profileImg = document.querySelector('.profileimg');
    const popup = document.getElementById('popup');
    const cancelBtn = document.getElementById('cancelBtn');
    const chooseImageBtn = document.getElementById('chooseImageBtn');
    const fileInput = document.createElement('input');
    const profileImageInput = document.getElementById('profileImage'); 

    fileInput.type = 'file';
    fileInput.accept = 'image/*';
    fileInput.style.display = 'none';

    function showPopup() {
        popup.style.display = 'flex';
    }

    function hidePopup() {
        popup.style.display = 'none';
    }

    function handleImageUpload(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                profileImg.src = e.target.result;
                profileImg.classList.add('profileimg'); 
                profileImageInput.value = e.target.result; 
            }
            reader.readAsDataURL(file);
        }
        hidePopup();
    }

    profileBtn.addEventListener('click', showPopup);
    profileImg.addEventListener('click', showPopup);
    cancelBtn.addEventListener('click', hidePopup);
    chooseImageBtn.addEventListener('click', function() {
        fileInput.click();
    });

    fileInput.addEventListener('change', handleImageUpload);
    document.body.appendChild(fileInput);
});