document.addEventListener('DOMContentLoaded', function() {
    const profileBtn = document.querySelector('.profilebtn');
    const profileImg = document.querySelector('.profileimg');
    const popup = document.getElementById('popup');
    const cancelBtn = document.getElementById('cancelBtn');

    function showPopup() {
        popup.style.display = 'flex';
    }

    function hidePopup() {
        popup.style.display = 'none';
    }

    profileBtn.addEventListener('click', showPopup);
    profileImg.addEventListener('click', showPopup);
    cancelBtn.addEventListener('click', hidePopup);
});