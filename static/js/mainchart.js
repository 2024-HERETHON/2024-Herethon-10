// 차트 생성
new Chart(document.getElementById("doughnut-chart"), {
    type: 'doughnut',
    data: {
        datasets: [
            {
                backgroundColor: ["var(--gray)", "var(--gray)", "var(--gray)", "var(--gray)", "#C22370"],
                data: [10, 20, 10, 10, 50]
            }
        ]
    },
});

const Popup = document.querySelector('.popup_wrap');
const No = document.querySelector('.no');

function showPop() {
    Popup.classList.remove('none')
}

function noPop() {
    Popup.classList.add('none')
}