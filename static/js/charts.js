// Admin dashboard map - 
function chart_chef(vars) {
    const labels = []
    const data_count = []
    for ( var i in vars ) {
        labels.push(vars[i]._id)
        data_count.push(vars[i].count)
    }
    console.log(labels)
    const data = {
        labels: labels,
        datasets: [{
            label: 'Top 5 Chefs',
            data: data_count,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 205, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(54, 162, 235, 0.2)'
            ],
            borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)'
            ],
            borderWidth: 1
        }]
    };

    const config = {
        type: 'bar',
        data,
        options: {
            scales: {
                y: {
                  beginAtZero: true
                }
            }
        }
    };

    var myChart = new Chart(
        document.getElementById('chefChart'),
        config
    );
};

// Reference: https://www.chartjs.org/docs/