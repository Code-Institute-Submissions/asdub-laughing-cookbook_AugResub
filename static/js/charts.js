// Admin dashboard Charts  - Chart.js config

// Top 5 chefs by recipe chart
function chart_chef(chef_data) {
    const labels = []
    const data_count = []
    for ( var i in chef_data ) {
        labels.push(chef_data[i]._id)
        data_count.push(chef_data[i].count)
    }
    const data = {
        labels: labels,
        datasets: [{
            label: 'Top 5 Chefs, by recipe count',
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

// Top 5 users by activity chart
function chart_user(activity_data) {
    const labels = []
    const data_count = []
    for ( var i in activity_data ) {
        labels.push(activity_data[i]._id)
        data_count.push(activity_data[i].total)
    }
    const data = {
        labels: labels,
        datasets: [{
            label: 'Top 5 Active Users',
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
        document.getElementById('userChart'),
        config
    );
};

// Reference: https://www.chartjs.org/docs/