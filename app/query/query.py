query_zero = """SELECT * FROM Usuario"""

#Mostrar nombre del cliente, el usuario que lo atendio, fecha de ordenAtencion, en que mesa esta y que productos pidió entre el mes de junio y agosto
query_one = """ SELECT cl.nombres, us.nombre, oa.fecha, me.id, pr.nombre, pe.fecha
FROM  Cliente[cl], Usuario[us], OrdenAtencion[oa], Mesa[me], Producto[pr], DetalleOrden[do], Pedido[pe]
WHERE oa.id_cliente = cl.id
AND oa.id_usuario = us.id
AND oa.id_mesa = me.id
AND do.id_ordenAtencion = oa.id
AND do.id_producto = pr.id
AND pe.id_cliente = cl.id
AND pe.id_usuario = us.id
AND MONTH (pe.fecha) IN (6,8); """


#Mostrar nombre del cliente, el usuario que lo atendio, fecha del pedido, nombre del repartidor, placa del vehiculo, latitud y longitud de la ubicacion y los productos que pidio en el mes de julio y septiembre
query_two = """ SELECT cl.nombres, us.nombre, pe.fecha, re.nombre, ve.placa, ub.latitud, ub.longitud,
pr.nombre
FROM Cliente[cl], Usuario[us], Pedido[pe], Repartidor[re], Vehiculo[ve], Ubicacion[ub], Producto[pr], DetallePedido[dp]
WHERE pe.id_cliente = cl.id
AND pe.id_usuario = us.id
AND pe.id_repartidor = re.id
AND pe.id_ubicacion = ub.id
AND dp.id_pedido = pe.id
AND dp.id_producto = pr.id
AND MONTH (pe.fecha) IN (7,9); """

#Mostrar el nombre de un repartidor, placa del vehículo y cuantos pedidos realizo
query_three = """ SELECT re.nombre, ve.placa, COUNT(pe.id_repartidor)[total pedido]
FROM Repartidor[re], Vehiculo[ve], Pedido[pe]
WHERE pe.id_repartidor = re.id
AND ve.id_repartidor = re.id
AND re.id = 1
GROUP BY re.nombre, ve.placa; """

#Mostrar nombre de los clientes, fecha, comensales, hora y observación de los clientes que solicitaron una reserva, dado un mes
query_four = """ SELECT cl.nombres, res.fecha, res.comensales, res.hora, res.observacion
FROM Cliente[cl], Reserva[res]
WHERE res.id_cliente = cl.id
AND MONTH (res.fecha) IN (12) """

#Mostrar nombre del producto, descripción, precio, estado, fecha del menú y nombre de la categoría que pertenece
query_five = """ SELECT pr.nombre, pr.descripcion, pr.precio, lm.estado, me.fecha, ca.nombre
FROM Producto[pr], ListaMenu[lm], Menu[me], Categoria[ca]
WHERE pr.id_categoria = ca.id
AND lm.id_producto = pr.id
AND lm.id_menu = me.id """

#Mostrar nombre del usuario tipo empleado, cuantas ordenAtencion y pedidos realizo en el mes de enero y marzo
query_six = """ SELECT us.nombre, ti.nombre, COUNT(oa.id_usuario)[cantidad de orden], COUNT(pe.id_usuario)[cantidad de pedidos], pe.fecha
FROM Usuario[us], Tipo[ti], OrdenAtencion[oa], Pedido[pe]
WHERE pe.id_usuario = us.id
AND us.id_tipo = ti.id
AND oa.id_usuario = us.id
AND ti.id = 2
AND MONTH (pe.fecha) IN (1,3)
GROUP BY us.nombre, ti.nombre, oa.id_usuario, pe.id_usuario, pe.fecha; """

#Mostrar el monto máximo y mínimo en las ventas que solicito un cliente
query_seven = """ SELECT  MAX(pe.montoTotal)[monto maximo], MIN(pe.montoTotal)[monto minimo], cl.nombres
FROM Pedido[pe], Cliente[cl]
WHERE pe.id_cliente = cl.id
AND cl.nombres = 'Tad'
GROUP BY cl.nombres, montoTotal; """

#Mostrar montoTotal, fecha, nombre del cliente, latitud, longitud y nombre del usuario que resgistraron pedidos en el año 2023
query_eigth = """ SELECT pe.montoTotal, pe.fecha, cl.nombres, ub.latitud, ub.longitud, us.nombre
FROM Pedido[pe], Cliente[cl], Ubicacion[ub], Usuario[us]
WHERE pe.id_usuario = us.id
AND pe.id_cliente = cl.id
AND pe.id_ubicacion = ub.id
AND YEAR (pe.fecha) = 2023 """

#Mostrar montoTotal, fecha, nombre del cliente, latitud, longitud y nombre del usuario que resgistraron pedidos en el año 2023
query_nine = """ SELECT pe.montoTotal, pe.fecha, cl.nombres, ub.latitud, ub.longitud, us.nombre
FROM Pedido[pe], Cliente[cl], Ubicacion[ub], Usuario[us]
WHERE pe.id_usuario = us.id
AND pe.id_cliente = cl.id
AND pe.id_ubicacion = ub.id
AND YEAR (pe.fecha) IN (2023); """