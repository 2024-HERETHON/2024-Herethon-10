document.addEventListener('DOMContentLoaded', () => {
    const teamdata = JSON.parse(document.getElementById('team-data').textContent);

    function getRandomColors(numColors) {
        const shuffledColors = ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0", "#9966FF"].sort(() => 0.5 - Math.random());
        return shuffledColors.slice(0, numColors);
    }

    function createDoughnutChart(canvasId, data) {
        const hasCompletedTasks = data.some(d => d.completed_tasks > 0);
        const chartData = hasCompletedTasks ? data.map(d => d.completed_tasks) : [1];
        const chartLabels = hasCompletedTasks ? data.map(d => d.username) : ['No completed tasks'];
        // const chartColors = hasCompletedTasks ? getRandomColors(data.length) : ["#C0C0C0"];
        const chartColors = hasCompletedTasks ? ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0", "#9966FF", "736989", "6EDB9D", "FF6FBC", "7B9CFF", "F7A36B"] : ["#C0C0C0"];


        new Chart(document.getElementById(canvasId), {
            type: 'doughnut',
            data: {
                //labels: chartLabels,
                datasets: [{
                    backgroundColor: chartColors,
                    data: chartData
                }]
            },
            options: {
                tooltips: {
                    enabled: false
                }
            }
        });
    }

    for (const teamId in teamdata) {
        createDoughnutChart(`doughnut-chart-${teamId}`, teamdata[teamId]);
    }
});
