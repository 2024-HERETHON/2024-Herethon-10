const Popup = document.querySelector('.popup_wrap');
const No = document.querySelector('.no');
const addTeam = document.querySelector('.add_team');
const First = document.querySelector('.first');
const Second = document.querySelector('.second');

function showPop() {
    Popup.classList.remove('none');
}

function noPop() {
    Popup.classList.add('none');
}

function addFriend() {
    addTeam.classList.remove('none');
}

function teamName() {
    First.classList.add('none');
    Second.classList.remove('none');
}