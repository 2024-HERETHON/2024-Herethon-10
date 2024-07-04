const chartDataArray = [
    [1, 2, 1, 1, 5],
    [2, 3, 4, 1, 2],
    [3, 1, 2, 3, 1]
];

document.querySelectorAll('.graph canvas').forEach((canvas, index) => {
    const data = {
        type: 'doughnut',
        data: {
            datasets: [{
                backgroundColor: ["var(--gray)", "var(--gray)", "var(--gray)", "var(--gray)", "#C22370"],
                data: chartDataArray[index]
            }]
        }
    };

    new Chart(canvas, data);
});