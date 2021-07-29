function crearGrafico(estados,newservers){ 
    estados = estados.substring(1, estados.length -1).split(', ');
    let up = 0;
    let down = 0;

    let jsonR = JSON.parse(newservers);
    let labels = []
    let datosDict = {}
    let datos =[]
    let colores = []
    for(key in jsonR){
        labels.push(key+ " OK")
        labels.push(key+ " FAIL")
        let up = 0
        let down = 0
        for( i of jsonR[key]){
            if(i=="isUp"){
                up++;
            }
            else if(i=="isDown"){
                down++;
            }
            datosDict[labels[labels.length-2]] = up;
            datosDict[labels[labels.length-1]] = down;
        }
        datos.push(up);
        datos.push(down);
    }

    const data = {
    labels: labels,
    datasets: [{
        label: 'My First Dataset',
        data: datos,
        backgroundColor: [
        'rgb(54, 162, 85)'/*verde*/,
        'rgb(255, 34, 36)'/*rojo*/,

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

function carga(){
setTimeout(function(){
    var contenedor = document.getElementById('contenedor_carga');

    contenedor.style.visibility = 'hidden';
    contenedor.style.opacity = '0';

    }, 3000)
}