var urlAPI = "http://127.0.0.1:8000";

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
// Ejecutar
cargarClientes();