from django.db import models

# Create your models here.
class dimCliente(models.Model):
    id_Cliente=models.AutoField(primary_key=True)
    Nombres=models.CharField(max_length=100, null=True)

    class Meta:
        db_table='[dbo].[dimCliente]'
        managed=False

class dimCondicionPago(models.Model):
    id_CondicionPago=models.AutoField(primary_key=True)
    Descripcion=models.CharField(max_length=50, null=True)

    class Meta:
        db_table='[dbo].[dimCondicionPago]'
        managed=False

class dimEmpleado(models.Model):
    id_Empleado=models.AutoField(primary_key=True)
    Nombres=models.CharField(max_length=100, null=True)

    class Meta:
        db_table='[dbo].[dimEmpleado]'
        managed=False

class dimMetodoPago(models.Model):
    id_MetodoPago=models.AutoField(primary_key=True)
    Tipo=models.CharField(max_length=50, null=True)

    class Meta:
        db_table='[dbo].[dimMetodoPago]'
        managed=False

class dimProducto(models.Model):
    id_Producto=models.AutoField(primary_key=True)
    Nombre=models.CharField(max_length=50, null=True)
    Moto=models.CharField(max_length=60, null=True)
    Marca=models.CharField(max_length=50, null=True)
    Categoria=models.CharField(max_length=100, null=True)

    class Meta:
        db_table='[dbo].[dimProducto]'
        managed=False

class dimTiempo(models.Model):
    id_Tiempo=models.AutoField(primary_key=True)
    Dia=models.IntegerField(null=True)
    Mes=models.IntegerField(null=True)
    Año=models.IntegerField(null=True)
    NombreDia=models.CharField(max_length=10, null=True)
    NombreMes=models.CharField(max_length=10, null=True)

    class Meta:
        db_table='[dbo].[dimTiempo]'
        managed=False

class FactVenta(models.Model):
    id_Venta=models.AutoField(primary_key=True)
    id_Empleado=models.ForeignKey(dimEmpleado, on_delete=models.CASCADE, db_column='id_Empleado')
    id_Cliente=models.ForeignKey(dimCliente, on_delete=models.CASCADE, db_column='id_Cliente')
    id_MetodoPago=models.ForeignKey(dimMetodoPago, on_delete=models.CASCADE, db_column='id_MetodoPago')
    id_CondicionPago=models.ForeignKey(dimCondicionPago, on_delete=models.CASCADE, db_column='id_CondicionPago')
    id_Producto=models.ForeignKey(dimProducto, on_delete=models.CASCADE, db_column='id_Producto')
    id_Tiempo=models.ForeignKey(dimTiempo, on_delete=models.CASCADE, db_column='id_Tiempo')
    Cantidad=models.IntegerField(null=True)
    Subtotal=models.DecimalField(max_digits=7, decimal_places=2, null=True)
    PrecioUnitario=models.DecimalField(max_digits=10, decimal_places=2, null=True)
    NumFactura=models.IntegerField(null=True)

    class Meta:
        db_table='[dbo].[FactVenta]'
        managed=False