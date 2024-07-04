// 차트 생성
new Chart(document.getElementById("doughnut-chart"), {
    type: 'doughnut',
    data: {
        datasets: [
            {
                backgroundColor: ["var(--gray)", "var(--gray)", "var(--gray)", "var(--gray)", "#C22370"],
                data: [1, 2, 1, 1, 5]
            }
        ]
    },
});