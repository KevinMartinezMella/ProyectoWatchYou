
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
<<<<<<< HEAD
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




function video(){
(function () {

    var bv = new Bideo();
    bv.init({
      // Video element
      videoEl: document.querySelector('#background_video'),
  
      // Container element
      container: document.querySelector('body'),
  
      // Resize
      resize: true,
  
      // autoplay: false,
  
      // Array of objects containing the src and type
      // of different video formats to add
      src: [
        {
          src: 'https://vjs.zencdn.net/v/oceans.mp4',
          type: 'video/mp4'
        },
        {
          src: 'https://vjs.zencdn.net/v/oceans.webm',
          type: 'video/webm;codecs="vp8, vorbis"'
        }
      ],
  
      // What to do once video loads (initial frame)
      onLoad: function () {
        document.querySelector('#video_cover').style.display = 'none';
      }
    });
  }());
} 
=======
}
>>>>>>> 7fcc8e2b4752bd392f308370eaf147328a6366b9
