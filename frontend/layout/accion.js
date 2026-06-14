const urlAPI = "http://127.0.0.1:8000/";

import { registrarControlInactividad,logout, fetchConAutenticacion } from "../login/auth.js";

//registrarControlInactividad();
document.addEventListener("DOMContentLoaded",() => {registrarControlInactividad();});

//impot

const navLinks   = document.querySelectorAll('.nav-link');
const secciones  = document.querySelectorAll('.seccion');
const tituloTop  = document.getElementById('topbarTitulo');
const btneditar = document.getElementById('btnEditar');


//material para agregar clientes
//const btnAgregarCliente = document.getElementById('btnGuardar');

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
// ==========================================
// LOGICA DE cerrar sesion
// ==========================================

const btnCerraSesion= document.getElementById("btnCerrarSesion")

if(btnCerraSesion){
  btnCerraSesion.addEventListener("click", (e)=>{
    e.preventDefault();//evita cualquier comportamiento por default

    const confirmar= confirm("¿Estás seguro de que deseas cerrar la sesión actual?")

    if(confirmar){
      logout(); //si el usuario acepta ejecutamos la funcion
    }

  })
}


// ==========================================
// LOGICA DE CLIENTES
// ==========================================

let clienteID = null;

// Hacemos la función exportable por si otro módulo necesita refrescar la tabla
export async function cargarClientes() {
  const cargando = document.getElementById('cargandoCliente');
  const tabla = document.getElementById('tablaCliente');
  const tbody = document.getElementById('bodyCliente');

  cargando.style.display = 'block';
  tabla.classList.remove('visible');
  
  try {
    // REEMPLAZO 1: Usamos tu función con autenticación automática.
    // Ojo: fetchConAutenticacion ya concatena urlAPI internamente según tu diseño previo.
    let respuesta = await fetchConAutenticacion('catalogos/clientes/');
    const dato = await respuesta.json();

    const cliente = Array.isArray(dato) ? dato : dato.results;
    let filas = "";

    for (let i = 0; i < cliente.length; i++) {
      let cli = cliente[i];
    
      filas += '<tr>';
      filas += '<td> '+(i+1) +' </td>';
      filas += '<td> '+ cli.Nombres +' </td>';
      filas += '<td> '+ cli.Apellidos +' </td>';
      filas += '<td> '+ cli.NumCedula +' </td>';
      filas += '<td> '+ cli.NumTeléfono +' </td>';

      // Botones editar y borrar
      filas += '<td class="td-acciones">';
      filas += '<button class="btn-accion btn-editar" '
              + `onclick="abrirModalCliente('editar', ${cli.id}, '${cli.Nombres}', '${cli.Apellidos}', '${cli.NumTeléfono}', '${cli.NumCedula}')">`
              + '✏ Editar'              
              + '</button>';
      filas += '<button class="btn-accion btn-eliminar" '
              + `onclick="eliminarCliente(${cli.id}, '${cli.Nombres}', '${cli.Apellidos}')">`
              + '🗑 Eliminar'              
              + '</button>';
      filas += ' </td>';
      filas += '</tr>';
    }

    tbody.innerHTML = filas;
    cargando.style.display = 'none';
    tabla.classList.add('visible');
  } catch (error) {
    cargando.textContent = '⚠ Error al conectar con la API local. ¿Está corriendo el servidor Django?';
    console.error('Error en cargarClientes:', error); 
  }
}

// modal cliente
window.abrirModalCliente = function(modo, id, nombre, apellido, telefono, numCedula) {
  document.getElementById('modalTextCliente').textContent = modo === 'crear' ? 'Nuevo cliente' : 'Editar Cliente';

  document.getElementById('clienNombre').value = nombre || '';
  document.getElementById('clienApellidos').value = apellido || '';
  document.getElementById('clienTelefono').value = telefono || '';
  document.getElementById('clienCedula').value = numCedula || '';
  
  const errorEl = document.getElementById('error');
  if (errorEl) errorEl.textContent = '';

  clienteID = modo === 'editar' ? id : null;
  document.getElementById('modalCliente').classList.add('activo');
}

window.cerrarModalCliente = function(idModal) {
  document.getElementById('clienNombre').value = '';
  document.getElementById('clienApellidos').value = '';
  document.getElementById('clienTelefono').value = '';
  document.getElementById('clienCedula').value = '';
  
  const errorEl = document.getElementById('error');
  if (errorEl) errorEl.textContent = '';
  
  document.getElementById(idModal).classList.remove('activo');
}

// ── POST / PUT: Guardar cliente ─────────────────────────────────────
window.guardarCliente = async function guardarCliente() {
  let nombre = document.getElementById('clienNombre').value.trim();
  let apellidos = document.getElementById('clienApellidos').value.trim();
  let telefono = document.getElementById('clienTelefono').value.trim();
  let cedula = document.getElementById('clienCedula').value.trim();
  let errorEl = document.getElementById('error');

  if (!nombre || !apellidos || !telefono || !cedula) {
    errorEl.textContent = 'Todos los campos son obligatorios.';
    return;
  }

  let body = JSON.stringify({ Nombres: nombre, Apellidos: apellidos, Telefono: telefono, NumCedula: cedula });

  let metodo = clienteID === null ? 'POST' : 'PATCH';
  // Pasamos solo la ruta relativa porque fetchConAutenticacion le pega la urlAPI
  let url = clienteID === null
    ? 'catalogos/clientes/'
    : 'catalogos/clientes/' + clienteID;

  try {
    // REEMPLAZO 2: Removimos la validación manual del token.
    // Tu función 'fetchConAutenticacion' inyectará el Header 'Authorization' automáticamente.
    let respuesta = await fetchConAutenticacion(url, {
      method: metodo,
      body: body
    });

    if (respuesta.ok) {
      cerrarModalCliente('modalCliente');
      cargarClientes(); 
    } else {
      let errores = await respuesta.json();
      errorEl.textContent = JSON.stringify(errores);
    }
  } catch (error) {
    errorEl.textContent = 'Error de conexión con la API.';
    console.error('Error en guardarCliente:', error);
  }
}

// BORRAR CLIENTE
window.eliminarCliente = async function(id, nombre, apellido) {
  let confirmar = window.confirm(`Seguro que quieres eliminar al cliente ${nombre} ${apellido}`);
  if (!confirmar) return;

  try {
    // REEMPLAZO 3: Petición DELETE limpia usando tu interceptor automático
    let url = 'catalogos/clientes/' + id;
    let respuesta = await fetchConAutenticacion(url, {
      method: 'DELETE'
    });

    if (respuesta.status === 204 || respuesta.ok) {
      cargarClientes();
    } else {
      alert('No se pudo eliminar. Código: ' + respuesta.status);
    }
  } catch (error) {
    alert('Error de conexión con la API.');
    console.error('Error en eliminarCliente:', error);
  }
}


// ==========================================
// 1. IMPORTACIONES AL INICIO DEL ARCHIVO
// ==========================================
// Importamos la función estrella de tu auth.js y la URL base si la tienes ahí
//import { fetchConAutenticacion, iniciarRefrescoAutomatico } from './auth.js'; 

//const urlAPI = "http://127.0.0.1:8000"; // Asegúrate de que no choque con las barras diagonales /

// Reavivamos el temporizador automático en esta página
//iniciarRefrescoAutomatico();

// ==========================================
// LOGICA DE EMPLEADOS
// ==========================================

let empleadoID = null;

// Hacemos la función exportable por si otro módulo necesita refrescar la tabla
export async function cargarEmpleados() {
  const cargando = document.getElementById('cargandoEmpleado');
  const tabla = document.getElementById('tablaEmpleado');
  const tbody = document.getElementById('bodyEmpleado');

  cargando.style.display = 'block';
  tabla.classList.remove('visible');
  
  try {
    // REEMPLAZO 1: Usamos tu función con autenticación automática.
    // Ojo: fetchConAutenticacion ya concatena urlAPI internamente según tu diseño previo.
    let respuesta = await fetchConAutenticacion('catalogos/empleados/');
    const dato = await respuesta.json();

    const empleado = Array.isArray(dato) ? dato : dato.results;
    let filas = "";

    for (let i = 0; i < empleado.length; i++) {
      let emp = empleado[i];
    
      filas += '<tr>';
      filas += '<td> '+(i+1) +' </td>';
      filas += '<td> '+ emp.Nombres +' </td>';
      filas += '<td> '+ emp.Apellidos +' </td>';
      filas += '<td> '+ emp.Telefono +' </td>';
      filas += '<td> '+ emp.NumCedula +' </td>';

      // Botones editar y borrar
      filas += '<td class="td-acciones">';
      filas += '<button class="btn-accion btn-editar" '
              + `onclick="abrirModalEmpleado('editar', ${emp.id}, '${emp.Nombres}', '${emp.Apellidos}', '${emp.Telefono}', '${emp.NumCedula}')">`
              + '✏ Editar'              
              + '</button>';
      filas += '<button class="btn-accion btn-eliminar" '
              + `onclick="eliminarEmpleado(${emp.id}, '${emp.Nombres}', '${emp.Apellidos}')">`
              + '🗑 Eliminar'              
              + '</button>';
      filas += ' </td>';
      filas += '</tr>';
    }

    tbody.innerHTML = filas;
    cargando.style.display = 'none';
    tabla.classList.add('visible');
  } catch (error) {
    cargando.textContent = '⚠ Error al conectar con la API local. ¿Está corriendo el servidor Django?';
    console.error('Error en cargarEmpleado:', error); 
  }
}

// modal empleado
window.abrirModalEmpleado = function(modo, id, nombre, apellido, telefono, numCedula) {
  document.getElementById('modalTextEmpleado').textContent = modo === 'crear' ? 'Nuevo empleado' : 'Editar Empleado';

  document.getElementById('empNombre').value = nombre || '';
  document.getElementById('empApellidos').value = apellido || '';
  document.getElementById('empTelefono').value = telefono || '';
  document.getElementById('empCedula').value = numCedula || '';
  
  const errorEl = document.getElementById('error');
  if (errorEl) errorEl.textContent = '';

  empleadoID = modo === 'editar' ? id : null;
  document.getElementById('modalEmpleado').classList.add('activo');
}

window.cerrarModal = function(idModal) {
  document.getElementById('empNombre').value = '';
  document.getElementById('empApellidos').value = '';
  document.getElementById('empTelefono').value = '';
  document.getElementById('empCedula').value = '';
  
  const errorEl = document.getElementById('error');
  if (errorEl) errorEl.textContent = '';
  
  document.getElementById(idModal).classList.remove('activo');
}

// ── POST / PUT: Guardar empleado ─────────────────────────────────────
window.guardarEmpleado = async function guardarEmpleado() {
  let nombre = document.getElementById('empNombre').value.trim();
  let apellidos = document.getElementById('empApellidos').value.trim();
  let telefono = document.getElementById('empTelefono').value.trim();
  let cedula = document.getElementById('empCedula').value.trim();
  let errorEl = document.getElementById('error');

  if (!nombre || !apellidos || !telefono || !cedula) {
    errorEl.textContent = 'Todos los campos son obligatorios.';
    return;
  }

  let body = JSON.stringify({ Nombres: nombre, Apellidos: apellidos, Telefono: telefono, NumCedula: cedula });

  let metodo = empleadoID === null ? 'POST' : 'PATCH';
  // Pasamos solo la ruta relativa porque fetchConAutenticacion le pega la urlAPI
  let url = empleadoID === null
    ? 'catalogos/empleados/'
    : 'catalogos/empleados/' + empleadoID;

  try {
    // REEMPLAZO 2: Removimos la validación manual del token.
    // Tu función 'fetchConAutenticacion' inyectará el Header 'Authorization' automáticamente.
    let respuesta = await fetchConAutenticacion(url, {
      method: metodo,
      body: body
    });

    if (respuesta.ok) {
      cerrarModal('modalEmpleado');
      cargarEmpleados(); 
    } else {
      let errores = await respuesta.json();
      errorEl.textContent = JSON.stringify(errores);
    }
  } catch (error) {
    errorEl.textContent = 'Error de conexión con la API.';
    console.error('Error en guardarEmpleado:', error);
  }
}

// BORRAR EMPLEADO
window.eliminarEmpleado = async function(id, nombre, apellido) {
  let confirmar = window.confirm(`Seguro que quieres eliminar al empleado ${nombre} ${apellido}`);
  if (!confirmar) return;

  try {
    // REEMPLAZO 3: Petición DELETE limpia usando tu interceptor automático
    let url = 'catalogos/empleados/' + id;
    let respuesta = await fetchConAutenticacion(url, {
      method: 'DELETE'
    });

    if (respuesta.status === 204 || respuesta.ok) {
      cargarEmpleados();
    } else {
      alert('No se pudo eliminar. Código: ' + respuesta.status);
    }
  } catch (error) {
    alert('Error de conexión con la API.');
    console.error('Error en eliminarEmpleado:', error);
  }
}





function cargarFactura1(){
  const token = localStorage.getItem("access");

  console.log("Token de acceso:", token); // Verificar que el token se está obteniendo correctamente
  if (!token) {
    alert('No se encontró token de acceso. Por favor, inicia sesión.');
    return;
  }

  fetch(urlAPI + '/movimiento/factura/', {
    headers: {
      'Authorization': `Bearer ${token}`
    }
  })
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
        unaFila += '<td>'+factura.fecha_formateada +'</td>';
        unaFila += '<td>'+factura.cliente_nombre +'</td>';
        unaFila += '<td>'+factura.Total +'</td>';
        unaFila += '<td>'+factura.condicion_nombre+'</td>'
        unaFila += '<td>'+factura.estadoCuenta_nommbre+'</td>'
        unaFila += '</tr>';

         

        todasLasFilas += unaFila;
      }
      
      cuerpoTabla.innerHTML = todasLasFilas;

      document.getElementById('cargandoFactura').style.display = 'none';
      document.getElementById('tablaFactura').classList.add('visible');

    });
}

async function cargarFactura() {
  const cargando = document.getElementById('cargandoFactura');
  const tabla = document.getElementById('tablaFactura');
  const tbody = document.getElementById('bodyFactura');

  cargando.style.display = 'block';
  tabla.classList.remove('visible');
  
  try {
    // REEMPLAZO 1: Usamos tu función con autenticación automática.
    // Ojo: fetchConAutenticacion ya concatena urlAPI internamente según tu diseño previo.
    let respuesta = await fetchConAutenticacion('/movimiento/factura/');
    const dato = await respuesta.json();

    const facturas = Array.isArray(dato) ? dato : dato.results;
    let filas = "";

    for (let i = 0; i < facturas.length; i++) {
      let factura = facturas[i];

      filas += '<tr>';
      filas += '<td>'+ (i+1)+'</td>';
      filas += '<td class="td-nombreEmp">'+factura.NumFactura+'</td>';
      filas += '<td>'+factura.fecha_formateada +'</td>';
      filas += '<td>'+factura.cliente_nombre +'</td>';
      filas += '<td>'+factura.Total +'</td>';
      filas += '<td>'+factura.condicion_nombre+'</td>'
      filas += '<td>'+factura.estadoCuenta_nommbre+'</td>'

      // Botones editar y borrar
      /*filas += '<td class="td-acciones">';
      filas += '<button class="btn-accion btn-editar" '
              + `onclick="abrirModalEmpleado('editar', ${emp.id}, '${emp.Nombres}', '${emp.Apellidos}', '${emp.Telefono}', '${emp.NumCedula}')">`
              + '✏ Editar'              
              + '</button>';
      filas += '<button class="btn-accion btn-eliminar" '
              + `onclick="eliminarEmpleado(${emp.id}, '${emp.Nombres}', '${emp.Apellidos}')">`
              + '🗑 Eliminar'              
              + '</button>';
      filas += ' </td>';*/
      filas += '</tr>';
    }

    tbody.innerHTML = filas;
    cargando.style.display = 'none';
    tabla.classList.add('visible');
  } catch (error) {
    cargando.textContent = '⚠ Error al conectar con la API local. ¿Está corriendo el servidor Django?';
    console.error('Error en cargarEmpleado:', error); 
  }
}


// Ejecutar
cargarClientes();
cargarEmpleados();
cargarFactura();


