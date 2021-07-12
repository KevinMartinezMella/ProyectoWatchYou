const data = {
    labels: [
        'FAIL',
        'OK',
        'WARNING'
    ], 
    datasets: [{
        label: 'My First Dataset',
        data: cargarDatos(),
        backgroundColor: [
        'rgb(255, 34, 36)'/*rojo*/,
        'rgb(54, 162, 85)'/*verde*/,
        'rgb(255, 205, 86)',
        'rgb(155, 20, 86)',
        'rgb(175, 205, 20)'


        ],
        hoverOffset: 4
    }]
    };
    const config = {
        type: 'pie',
        data: data,
    };


function crearGrafico(){                                                    
    var myChart = new Chart(
      document.getElementById('myChart'),
      config
    );
}
function cargarDatos(arr){
    datos = [];
    // for(let i = 0; i < arr.lenght; i++){
        for(let i = 0; i < 5; i++){
            datos.push(Math.floor(Math.random() *10))
    }
    return datos;
}