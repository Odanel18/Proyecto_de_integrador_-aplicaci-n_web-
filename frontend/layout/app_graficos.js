// ====================================================
//  app_graficos.js
//  Responsabilidad: Procesar la lista de FactVenta y dibujar el Dashboard.
// ====================================================

import { registrarControlInactividad, logout, fetchConAutenticacion } from "../login/auth.js";

document.addEventListener("DOMContentLoaded", () => {
    registrarControlInactividad();
    cargarGraficos();
});

var graficosCreados = false;

async function cargarGraficos() {
  if (graficosCreados) return;

  try {
    // 1. Consumir tu API real (retorna el Array de ventas)
    var respuesta = await fetchConAutenticacion('dashboard/ventas/factventa/');
    var ventas = await respuesta.json(); // Esto es el [ {id_Venta: 1...}, {...} ]

    if (!Array.isArray(ventas)) {
        console.error("La API no devolvió un formato de lista válido.");
        return;
    }

    // 2. VARIABLES PARA PROCESAR LOS DATOS (Métricas y Agrupaciones)
    let totalIngresos = 0;
    let totalUnidades = 0;
    let transacciones = ventas.length;
    let clientesUnicos = new Set();

    // Objetos para agrupar gráficos
    let agrupadoMes = {};         // { "202512": acumulado, ... }
    let agrupadoMetodoPago = {};  // { "2": cantidad, "5": cantidad, ... }
    let agrupadoProducto = {};    // { "118": cantidad, "22": cantidad, ... }
    let agrupadoEmpleado = {};    // { "3": acumulado, "1": acumulado, ... }

    // 3. PROCESAR EL ARRAY EN UN SOLO BUCLE (Eficiencia)
    ventas.forEach(venta => {
        let subtotal = parseFloat(venta.Subtotal) || 0;
        let cantidad = parseInt(venta.Cantidad) || 0;

        // Acumuladores de las Tarjetas
        totalIngresos += subtotal;
        totalUnidades += cantidad;
        if(venta.id_Cliente) clientesUnicos.add(venta.id_Cliente);

        // Agrupar para Gráfico 1: Por mes/tiempo (usamos id_Tiempo como identificador)
        let mes = venta.tiempo_año ? String(venta.id_Tiempo).substring(0, 6) : "Sin Fecha"; 
        agrupadoMes[mes] = (agrupadoMes[mes] || 0) + subtotal;

        // Agrupar para Gráfico 2: Métodos de Pago
        let metodo = venta.metodo_pago_tipo || "Desconocido";
        agrupadoMetodoPago[metodo] = (agrupadoMetodoPago[metodo] || 0) + 1;

        // Agrupar para Gráfico 3: Productos
        let prod = venta.producto_nombre || "Otro";

        let productoArray = Object.keys(agrupadoProducto).map(key => key.toLowerCase());
        agrupadoProducto[prod] = (agrupadoProducto[prod] || 0) + cantidad;


        // Agrupar para Gráfico 4: Empleados
        let emp = venta.empleado_nombre || "Vendedor";
        agrupadoEmpleado[emp] = (agrupadoEmpleado[emp] || 0) + subtotal;
    });

    // 4. INYECTAR DATOS EN LAS TARJETAS HTML
    if (document.getElementById('totalIngresos')) {
        document.getElementById('totalIngresos').textContent = `$${totalIngresos.toFixed(2)}`;
        document.getElementById('totalUnidades').textContent = totalUnidades;
        document.getElementById('totalTransacciones').textContent = transacciones;
        document.getElementById('totalClientesAtendidos').textContent = clientesUnicos.size;
    }

    // 5. CONFIGURACIÓN GLOBAL DE CHART.JS
    Chart.defaults.color = '#000000';
    Chart.defaults.borderColor = 'rgba(255, 255, 255, 0.24)';

    // ════════════════════════════════════════════════════════════════════
    // GRÁFICO 1 — Ventas en el Tiempo (id_Tiempo)
    // ════════════════════════════════════════════════════════════════════
    new Chart(
      document.getElementById('graficoVentas'),
      {
        type: 'bar',
        data: {
          labels: Object.keys(agrupadoMes), // Códigos de mes ej: ["202512", "202511"]
          datasets: [{
            label: 'Ingresos ($)',
            data: Object.values(agrupadoMes),
            backgroundColor: 'rgba(59,130,246,0.75)',
            borderRadius: 4
          }]
        },
        options: { plugins: { legend: { display: false } } }
      }
    );

    // ════════════════════════════════════════════════════════════════════
    // GRÁFICO 2 — Métodos de Pago más Utilizados (id_MetodoPago)
    // ════════════════════════════════════════════════════════════════════
    new Chart(
      document.getElementById('graficoMetodosPago'),
      {
        type: 'line',
        data: {
          labels: Object.keys(agrupadoMetodoPago).map(id => ` ${id}`), 
          datasets: [{
            label: 'Transacciones',
            data: Object.values(agrupadoMetodoPago),
            borderColor: '#10b981',
            backgroundColor: 'rgba(16,185,129,0.12)',
            fill: true,
            tension: 0.4,
            pointRadius: 7
          }]
        },
        options: { plugins: { legend: { display: false } } }
      }
    );

    // ════════════════════════════════════════════════════════════════════
    // GRÁFICO 3 — Dona: Distribución por ID de Producto
    // ════════════════════════════════════════════════════════════════════
    // 1. Convertimos el objeto agrupadoProducto a un Array para poder ordenarlo
    let productosArray = Object.keys(agrupadoProducto).map(nombre => {
        return { nombre: nombre, cantidad: agrupadoProducto[nombre] };
    });

    // 2. Ordenamos de mayor a menor según la cantidad vendida
    productosArray.sort((a, b) => b.cantidad - a.cantidad);

    // 3. Cortamos la lista para quedarnos estrictamente con los 10 mejores
    let top10Productos = productosArray.slice(0, 10);

    // 4. Extraemos las etiquetas (nombres) y los datos (cantidades) correspondientes
    let top10Labels = top10Productos.map(p => p.nombre);
    let top10Data = top10Productos.map(p => p.cantidad);
    new Chart(
      
      
      document.getElementById('graficoCategorias'),
      {
        // doughnut, para que el digrama tenga un ueco
        //pie caso contrario
        type: 'doughnut',
        data: {
          labels: top10Labels,
          datasets: [{
            data: top10Data,
            backgroundColor: [ '#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6',
              '#ec4899', '#06b6d4', '#14b8a6', '#f97316', '#64748b'],
            borderWidth: 1
          }]
        },
        options:{
          responsive: true,
         // maintainAspectRatio: false,
         plugins:{
          legend:{
            display: true,
            position:'right',
            labels:{
              boxWidth:15,
              padding: 15,
              font:{
                size: 16
              }
            }
          }
         }
        }
      }
    );


    // ════════════════════════════════════════════════════════════════════
    // GRÁFICO 4 — Barras horizontales: Ventas por ID de Empleado
    // ════════════════════════════════════════════════════════════════════
    new Chart(
      document.getElementById('graficoEmpleados'),
      {
        type: 'bar',
        data: {
          labels: Object.keys(agrupadoEmpleado).map(id => `Empleado ${id}`),
          datasets: [{
            label: 'Total Vendido ($)',
            data: Object.values(agrupadoEmpleado),
            backgroundColor: ['#10b981', '#3b82f6', '#f59e0b', '#ef4444'],
            borderRadius: 4
          }]
        },
        options: {
          indexAxis: 'y',
          plugins: { legend: { display: false } }
        }
      }
    );

    graficosCreados = true;

  } catch (error) {
    console.error('Error procesando el listado de hechos:', error);
  }
}