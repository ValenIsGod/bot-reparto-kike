# El bot ahora recibe el bloque de texto completo
lista_pedido = """
2 coca 2l
3 manaos pomelo
4 pure marolio
"""

lineas = lista_pedido.strip().split('\n')
reporte_final = []

for linea in lineas:
    # Separamos el número del nombre
    partes = linea.split(' ', 1)
    cantidad = partes[0]
    producto = partes[1]
    
    # El bot busca en la web
    resultado = buscar_en_tienda(producto, cantidad) 
    if resultado == "OK":
        reporte_final.append(f"✅ {producto} cargado.")
    else:
        reporte_final.append(f"❌ {producto} sin stock.")

# Este reporte es el que te llegaría a vos
print("\n".join(reporte_final))
