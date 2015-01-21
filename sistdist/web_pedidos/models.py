from django.db import models

class CategoriasProductos(models.Model):
    categoriaId = models.AutoField(primary_key=True)
    categoriaDescripcion = models.CharField(max_length=100)

class TiposProducto(models.Model):
    tipoProductoId = models.AutoField(primary_key=True)
    tipoProductoDescripcion = models.CharField(max_length=100)

class Productos(models.Model):
    productoId = models.AutoField(primary_key=True)
    productoDescripcion = models.CharField(max_length=100)
    categoriaProducto = models.ForeignKey(CategoriasProductos)
    tipoProducto = models.ForeignKey(TiposProducto)
    productoAlta = models.DateTimeField('fecha de insercion')
    productoActivo = models.BooleanField(default=True)

class ContactosCliente(models.Model):
    contactoClienteId = models.AutoField(primary_key=True)
    contactoNombre = models.CharField(max_length=50)
    contactoApePat = models.CharField(max_length=50)
    contactoApeMat = models.CharField(max_length=50)
    contactoTelefono = models.CharField(max_length=15)
    contactoExtension = models.CharField(max_length=8)
    contactoCelular = models.CharField(max_length=15)
    contactoEmail = models.EmailField(max_length=254)

class Clientes(models.Model):
    clienteId = models.AutoField(primary_key=True)
    clienteRazonSocial = models.CharField(max_length=100)
    clienteRFC = models.CharField(max_length=13)
    clienteCalle = models.CharField(max_length=250)
    clienteNumExt = models.CharField(max_length=10)
    clienteNumInt = models.CharField(max_length=10)
    clienteColonia = models.CharField(max_length=150)
    clienteCP = models.CharField(max_length=5)
    clienteTelefono = models.CharField(max_length=15)
    contactoCliente = models.ForeignKey(ContactosCliente)

class Usuarios(models.Model):
    usuarioId = models.AutoField(primary_key=True)
    usuarioLogin = models.CharField(max_length=20)
    usuarioPassword = models.CharField(max_length=150)




