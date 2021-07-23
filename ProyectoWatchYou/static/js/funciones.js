
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


// window.onload = function(){
//     var contenedor = document.getElementById('contenedor_carga')
//     contenedor.style.visibility = 'hidden';
//     contenedor.style.opacity = '0';

// }

function carga(){
setTimeout(function(){
    var contenedor = document.getElementById('contenedor_carga');

    contenedor.style.visibility = 'hidden';
    contenedor.style.opacity = '0';

    }, 3000)
}