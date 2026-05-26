var urlAPI = "http://127.0.0.1:8000";

const navLinks   = document.querySelectorAll('.nav-link');
const secciones  = document.querySelectorAll('.seccion');
const tituloTop  = document.getElementById('topbarTitulo');
const btneditar = document.getElementById('btnEditar');


//material para agregar clientes
const btnAgregarCliente = document.getElementById('btnGuardar');

navLinks.forEach(function(link) {
  link.addEventListener('click', function(e) {
    e.preventDefault();

    // Leer qué sección abrir
    const nombreSeccion = link.dataset.section;

    // Quitar clase activo de todos los links
    navLinks.forEach(function(l) {
      l.classList.remove('activo');
    });

    // Poner clase activo al link clickeado
    link.classList.add('activo');

    // Ocultar todas las secciones
    secciones.forEach(function(s) {
      s.classList.remove('activa');
    });

    // Mostrar la sección correspondiente
    document.getElementById(nombreSeccion).classList.add('activa');

    // Actualizar el título de la barra superior
    tituloTop.textContent = link.textContent;
  });
});


function cargarClientes() {

  fetch(urlAPI + '/catalogos/clientes/')
    .then(function(respuesta) {
      return respuesta.json();
    })
    .then(function(listaCliente) {

      var cuerpoTabla = document.getElementById('bodyCliente');
      var todasLasFilas = '';

      for (var i = 0; i < listaCliente.length; i++) {

        var cliente = listaCliente[i];

        var unaFila = '<tr>';
        unaFila += '<td>' + (i + 1) + '</td>';
        unaFila += '<td class="td-nombre">' + cliente.Nombres + '</td>';
        unaFila += '<td>' + cliente.Apellidos + '</td>';
        unaFila += '<td>' + cliente.NumCedula + '</td>';
        unaFila += '<td>' + cliente.NumTeléfono + '</td>';
        unaFila += '</tr>';

        todasLasFilas += unaFila;
      }

      cuerpoTabla.innerHTML = todasLasFilas;

      document.getElementById('cargandoCliente').style.display = 'none';
      document.getElementById('tablaCliente').classList.add('visible');
    });
}

//Evento click del boton de guardar cliente
btnAgregarCliente.addEventListener('click', agregaCliente,)

//funcion para agregar cliente
function agregaCliente(){

  //Se extraen la información de los input traves del (value)
  const nombre = document.getElementById('nombre').value;
  const apellido = document.getElementById('apellido').value;
  const numCedula = document.getElementById('numCedula').value;
  const telefono = document.getElementById('telefono').value;
  //crear objeto de cliente 
  //Este ojeto sera enviado a la api ejemplo avariable en el bakend (Nombres), en javaScrit (nombre)
  // ejemplo Nombre:nombre, es decir Nombre:Odanel, inserta informacion del input
  const cliente = {
    Nombres: nombre,
    Apellidos: apellido,
    NumCedula:numCedula,
    NumTeléfono: telefono
  };
  //enviar datos a la api
  fetch(urlAPI + '/catalogos/clientes/',{
    //Se utiliza el metodo POST para guardar
    method: 'POST',
    //se le asigna el tipo de información enviada
    headers:{
      'Content-Type': 'application/json'
    },
    // Convierte el objeto js a json
    body: JSON.stringify(cliente)

  })

  //Respuesta del servidor
  .then(function(response){
    return response.json();
  })

  //datos recibidos
  .then(function(data){

    console.log(data);

    //usa la funcion cargarClientes(); para recarga la tabla
    cargarClientes();

    //limpia los input una vez guardada la información
    const nombre = document.getElementById('nombre').value = '';
    const apellido = document.getElementById('apellido').value = '';
    const numCedula = document.getElementById('numCedula').value= '';
    const telefono = document.getElementById('telefono').value = '';
  })

  //captura los errores
  .catch(function(error){
    console.log("Error: ", error)
  });
}

//EMPLEADO

function cargarEmpleados(){
  fetch(urlAPI + '/catalogos/empleados/')
    .then(function(respuesta){
      return respuesta.json();
    })

    .then(function(listaEmpleado){
      let cuerpoTabla = document.getElementById('bodyEmpleado');
      let todasLasFilas = '';

      for (let  i=0; i<listaEmpleado.length; i++){

        let empleado= listaEmpleado[i];
        
        let unaFila = '<tr>';
        unaFila += '<td>'+ (i+1)+'</td>';
        unaFila += '<td class="td-nombreEmp">'+empleado.Nombres+'</td>';
        unaFila += '<td>'+empleado.Apellidos +'</td>';
        unaFila += '<td>'+empleado.Telefono +'</td>';
        unaFila += '<td>'+empleado.NumCedula +'</td>';
        unaFila += '</tr>';

        todasLasFilas += unaFila;
      }
      
      cuerpoTabla.innerHTML = todasLasFilas;

      document.getElementById('cargandoEmpleado').style.display = 'none';
      document.getElementById('tablaEmpleado').classList.add('visible');

    });
}

function cargarFactura(){
  fetch(urlAPI + '/movimiento/factura/')
    .then(function(respuesta){
      return respuesta.json();
    })

    .then(function(listaFactura){
      let cuerpoTabla = document.getElementById('bodyFactura');
      let todasLasFilas = '';

      for (let  i=0; i<listaFactura.length; i++){

        let factura= listaFactura[i];
        
        let unaFila = '<tr>';
        unaFila += '<td>'+ (i+1)+'</td>';
        unaFila += '<td class="td-nombreEmp">'+factura.NumFactura+'</td>';
        unaFila += '<td>'+factura.Fecha +'</td>';
        unaFila += '<td>'+factura.ClienteId +'</td>';
        unaFila += '<td>'+factura.Total +'</td>';
        unaFila += '<td>'+factura.condicionId+'</td>'
        unaFila += '<td>'+factura.estadoCuentaId+'</td>'
        unaFila += '</tr>';

         

        todasLasFilas += unaFila;
      }
      
      cuerpoTabla.innerHTML = todasLasFilas;

      document.getElementById('cargandoFactura').style.display = 'none';
      document.getElementById('tablaFactura').classList.add('visible');

    });
}


// Ejecutar
cargarClientes();
cargarEmpleados();
cargarFactura();
