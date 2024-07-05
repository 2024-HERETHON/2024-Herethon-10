document.addEventListener('DOMContentLoaded', () => {
    // teamdata와 team의 데이터를 가져옴
    const teamData = JSON.parse(document.getElementById('teamdata').textContent);
    const teamId = document.getElementById('team').textContent;
    //const teamMemberCount = document.getElementById('team_member_count').textContent;

    function getRandomColors(numColors) {
        const shuffledColors = colors.sort(() => 0.5 - Math.random());
        return shuffledColors.slice(0, numColors);
    }

    function createDoughnutChart(canvasId, data) {
        const hasCompletedTasks = data.some(d => d.completed_tasks > 0);
        const chartData = hasCompletedTasks ? data.map(d => d.completed_tasks) : [1];
        const chartLabels = hasCompletedTasks ? data.map(d => d.username) : ['끝낸 일이 없음'];
        //const chartColors = hasCompletedTasks ? getRandomColors(teamMemberCount) : ["#C0C0C0"];
        const chartColors = hasCompletedTasks ? ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0", "#9966FF", "736989", "6EDB9D", "FF6FBC", "7B9CFF", "F7A36B"] : ["#C0C0C0"];

        new Chart(document.getElementById(canvasId), {
            type: 'doughnut',
            data: {
                labels: chartLabels,
                datasets: [{
                    backgroundColor: chartColors,
                    data: chartData
                }]
            },
            options: {
                tooltips: {
                    callbacks: {
                        label: function(tooltipItem, data) {
                            return data.labels[tooltipItem.index];
                        }
                    }
                }
            }
        });
    }

    // teamId를 통해 차트를 생성
    createDoughnutChart(`doughnut-chart-${teamId}`, teamData);
});


/*

,
            options: {
                legend: {
                    display: true,
                    position: 'bottom',
                    labels: {
                        generateLabels: function(chart) {
                            const { datasets } = chart.data;
                            return datasets[0].usernames.map((username, index) => ({
                                text: `${username}`,
                                fillStyle: datasets[0].backgroundColor[index]
                            }));
                        }
                    }
                },
                tooltips: {
                    callbacks: {
                        label: function(tooltipItem, chartData) {
                            if (!hasCompletedTasks) {
                                return 'No completed tasks';
                            }
                            const dataset = chartData.datasets[tooltipItem.datasetIndex];
                            const label = chartData.labels[tooltipItem.index];
                            const value = dataset.data[tooltipItem.index];
                            return `${label}: ${value}`;
                        }
                    }
                }
            }
*/