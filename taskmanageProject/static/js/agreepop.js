document.querySelector('.agree1btn').addEventListener('click', () => {
    document.querySelector('.agree1').classList.add('active');
});

document.querySelector('.backbtn-ag1').addEventListener('click', () => {
    document.querySelector('.agree1').classList.remove('active');
});

document.querySelector('.agree2btn').addEventListener('click', () => {
    document.querySelector('.agree2').classList.add('active');
});

document.querySelector('.backbtn-ag2').addEventListener('click', () => {
    document.querySelector('.agree2').classList.remove('active');
});

document.querySelector('.agree3btn').addEventListener('click', () => {
    document.querySelector('.agree3').classList.add('active');
});

document.querySelector('.backbtn-ag3').addEventListener('click', () => {
    document.querySelector('.agree3').classList.remove('active');
});