// let datos = [];

// const data = {
//     labels: [
//         'FAIL',
//         'OK',
//         'WARNING'
//     ], 
//     datasets: [{
//         label: 'My First Dataset',
//         data: datos,
//         backgroundColor: [
//         'rgb(255, 34, 36)'/*rojo*/,
//         'rgb(54, 162, 85)'/*verde*/,
//         'rgb(255, 205, 86)',
//         // 'rgb(155, 20, 86)',
//         // 'rgb(175, 205, 20)'


//         ],
//         hoverOffset: 4
//     }]
//     };
//     const config = {
//         type: 'pie',
//         data: data,
//     };


function crearGrafico(estados){ 
    estados = estados.substring(1, estados.length -1).split(', ');
    let up = 0;
    let down = 0;
    for(let i = 0; i < estados.length; i++){
        if (estados[i]== '1'){
            up++;
        }
        else if (estados[i]== '2'){
            down++;
        } 
    }  
    let datos = [up,down];
    console.log(estados)
    console.log(estados)
    
    console.log(datos)
    const data = {
    labels: [
        'FAIL',
        'OK',
    ], 
    datasets: [{
        label: 'My First Dataset',
        data: datos,
        backgroundColor: [
        'rgb(255, 34, 36)'/*rojo*/,
        'rgb(54, 162, 85)'/*verde*/,
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