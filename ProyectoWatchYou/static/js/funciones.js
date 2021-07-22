
function crearGrafico(estados){ 
    estados = estados.substring(1, estados.length -1).split(', ');
    let up = 0;
    let down = 0;
    console.log(estados)
    for(let i = 0; i < estados.length; i++){
        if (estados[i] == "isUp"){
            up++;
        }
        else if (estados[i] == "isDown"){
            down++;
        } 
    }  
    let datos = [up,down];
    
    console.log(datos)
    const data = {
    labels: [
        'OK',
        'FAIL',
    ], 
    datasets: [{
        label: 'My First Dataset',
        data: datos,
        backgroundColor: [
        'rgb(54, 162, 85)'/*verde*/,
        'rgb(255, 34, 36)'/*rojo*/,
        // 'rgb(255, 205, 86)',
        // 'rgb(155, 20, 86)',
        // 'rgb(175, 205, 20)'


        ],
        hoverOffset: 4
    }]
    };
    const config = {
        type: 'pie',
        data: data,
    };
    var myChart = new Chart(
      document.getElementById('myChart'),
      config
    );
}