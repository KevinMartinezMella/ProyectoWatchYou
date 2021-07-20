let datos = [];

const data = {
    labels: [
        'FAIL',
        'OK',
        'WARNING'
    ], 
    datasets: [{
        label: 'My First Dataset',
        data: datos,
        backgroundColor: [
        'rgb(255, 34, 36)'/*rojo*/,
        'rgb(54, 162, 85)'/*verde*/,
        'rgb(255, 205, 86)',
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


function crearGrafico(estados){ 
    estados = estados.substring(1, estados.length -1)
    for(let i = 0; i < estados.length; i++){
        if (estados.estado == 'is Up'){
            estados.estado[i] = 1;
        }
        else if (estados.estado == 'is Down'){
            estados.estado[i] = 2;
        } 
    }  
    let datos = estados.split(', ' );
    console.log(estados)
    
    console.log(datos)
    var myChart = new Chart(
      document.getElementById('myChart'),
      config
    );
}
// function cargarDatos(){
//     datos = ;
//     // for(let i = 0; i < arr.lenght; i++){
//     //     for(let i = 0; i < 3; i++){
//     //         datos.push(Math.floor(Math.random() *3))
//     // }
//     return datos;
// }

// function traerDatos(){
//     alert('hola')
//     var request = new Request('/datos',{method: 'GET'});
//     return request     
// }