const urlAPI = "http://127.0.0.1:8000/";

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

let empleadoID=null;

async function cargarEmpleados() {
  const cargando = document.getElementById('cargandoEmpleado')
  const tabla= document.getElementById('tablaEmpleado')
  const tbody=document.getElementById('bodyEmpleado')

  cargando.style.display='block';
  tabla.classList.remove('visible')
  
  try {

    const respuesta = await fetch(urlAPI + '/catalogos/empleados/' );
    const dato = await respuesta.json();

    const empleado = Array.isArray(dato) ? dato : dato.results;

    var filas = "";

    for (let i = 0; i < empleado.length; i++) {
      var emp= empleado[i];
    
      filas += '<tr>'
      filas += '<td> '+(i+1) +' </td>';
      filas += '<td> '+ emp.Nombres +' </td>';
      filas += '<td> '+ emp.Apellidos +' </td>';
      filas += '<td> '+ emp.Telefono +' </td>';
      filas += '<td> '+ emp.NumCedula +' </td>';

      // botenes editar y borra

      filas += '<td class= "td-acciones">'
      filas += '<button class="btn-accion btn-editar"'
              + 'onclick="abrirModalEmpleado (\'editar\','+emp.id+',\''+emp.Nombres+'\',\''+emp.Apellidos+'\',\''+emp.Telefono+'\',\''+emp.NumCedula+'\')">'
              + '✏ Editar'              
              + '</button>';
      filas += '<button class="btn-accion btn-eliminar"'
              + 'onclick="eliminarEmpleado ('+emp.id+',\''+emp.Nombres+'\',\''+emp.Apellidos+'\')">'
              + '🗑 Eliminar'              
              + '</button>';
      filas += ' </td>'
      filas += '</tr>'
    }

    tbody.innerHTML = filas;
    cargando.style.display='none';
    tabla.classList.add('visible');
  } catch (error) {
   cargando.textContent = '⚠ Error al conectar con la API local. ¿Está corriendo el servidor Django?';
    console.error('Error en cargarEmpleado:', error); 
  }
}



// modal empleado
function abrirModalEmpleado(modo,id,nombre,apellido,telefono,numCedula){

  
  document.getElementById('modalTextEmpleado').textContent= modo ==='crear'? 'Nuevo empleado': 'Editar Empleado';

  document.getElementById('empNombre').value = nombre || '';
  document.getElementById('empApellidos').value = apellido || '';
  document.getElementById('empTelefono').value = telefono || '';
  document.getElementById('empCedula').value = numCedula || '';
  document.getElementById('error').textContent  = '';

  empleadoID = modo === 'editar' ? id : null;

  document.getElementById('modalEmpleado').classList.add('activo');
}

function cerrarModal(idModal) {

  document.getElementById('empNombre').value = '';
  document.getElementById('empApellidos').value = '';
  document.getElementById('empTelefono').value= '';
  document.getElementById('empCedula').value = '';
  document.getElementById('error').value='';
  
  document.getElementById(idModal).classList.remove('activo');
}

//guardar

// ── POST / PUT: Guardar departamento ─────────────────────────────────────
// Esta función decide si crear (POST) o editar (PUT) según depIdActual.
async function guardarEmpleado() {

  // Leer los valores del formulario
  var nombre = document.getElementById('empNombre').value.trim();
  var apellidos = document.getElementById('empApellidos').value.trim();
  var telefono = document.getElementById('empTelefono').value.trim();
  var cedula = document.getElementById('empCedula').value.trim();
  var errorEl = document.getElementById('error');

  // Validación básica en el frontend antes de llamar a la API
  if (!nombre || !apellidos || !telefono || !cedula) {
    errorEl.textContent = 'Todos los campos son obligatorios.';
    return;
  }

  // ── Armar el objeto que se enviará como JSON en el body ──────────────
  // JSON.stringify() convierte el objeto JS a texto JSON:
  //   { "codigo": "MN", "nombre": "Managua" }  → '{"codigo":"MN","nombre":"Managua"}'
  var body = JSON.stringify({ Nombres: nombre, Apellidos: apellidos, Telefono: telefono, NumCedula: cedula });

  // ── Definir método y URL según si es creación o edición ─────────────
  // POST → /catalogos/departamentos/          (sin ID, la API lo genera)
  // PUT  → /catalogos/departamentos/<id>      (con ID para identificar el registro)
  var metodo = empleadoID === null ? 'POST' : 'PATCH';
  var url    = empleadoID === null
    ? urlAPI + '/catalogos/empleados/'
    : urlAPI + '/catalogos/empleados/' + empleadoID;

  try {
    // ── fetch con configuración completa ────────────────────────────────
    // A diferencia del GET, aquí pasamos un objeto de opciones:
    //   method  → el verbo HTTP (POST, PUT, DELETE, etc.)
    //   headers → le decimos a la API que le enviamos JSON
    //   body    → el contenido de la petición (solo en POST/PUT/PATCH)
    var respuesta = await fetch(url, {
      method:  metodo,
      headers: { 'Content-Type': 'application/json' },
      body:    body
    });

    if (respuesta.ok) {
      // 201 Created (POST) o 200 OK (PUT) → éxito
      cerrarModal('modalEmpleado');
      cargarEmpleados(); // Recargar la tabla para ver el cambio

      
    } else {
      // La API respondió con error (ej. 400 Bad Request por datos inválidos)
      var errores = await respuesta.json();
      errorEl.textContent = JSON.stringify(errores);
    }

  } catch (error) {
    errorEl.textContent = 'Error de conexión con la API.';
    console.error('Error en guardarEmpleado:', error);
  }
}


// BORRAR EMPLEADO
async function eliminarEmpleado(id, nombre, apellido) {
  var confirmar= window.confirm(`Seguro que quieres eliminar al empleado  ${nombre} ${apellido}`);
  if(!confirmar)
    return;

  try {
    var respuesta= await fetch(urlAPI + '/catalogos/empleados/'+ id,{
      method:'DELETE'

    });

    if (respuesta.status === 204){
      cargarEmpleados();
    }
    else{
      alert('No se puedo eliminar. Codigo: ' + respuesta.status)
    }
  } catch (error) {
    alert('Error de conexión con la API.');
    console.error('Error en eliminarEmpleado:', error);
  }
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
