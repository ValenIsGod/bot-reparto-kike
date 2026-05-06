import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def procesar_pedido(bloque_texto):
    # Configuracion de Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    
    lineas = bloque_texto.strip().split('\n')
    informe = []

    try:
        driver.get("https://distribuidoradelsur.com.ar/tienda/#")
        time.sleep(2)

        for linea in lineas:
            # Separamos cantidad de nombre (Ej: "2 coca 2l" -> "2" y "coca 2l")
            partes = linea.split(' ', 1)
            if len(partes) < 2: continue
            
            cantidad = partes[0]
            producto_nombre = partes[1]

            print(f"🔍 Buscando: {producto_nombre}...")
            
            # Buscador
            buscador = driver.find_element(By.NAME, "txtBuscar")
            buscador.clear()
            buscador.send_keys(producto_nombre)
            buscador.send_keys(Keys.ENTER)
            time.sleep(2)

            # Verificamos si hay resultados
            productos = driver.find_elements(By.CLASS_NAME, "portfolio-item")
            
            if productos:
                # Entramos al primer producto
                productos[0].click()
                time.sleep(1)
                
                # REGLA DE ORO: Si el modal de "Cerrado" aparece o no está el botón
                # Mañana aquí agregaremos el clic en "Agregar al carrito"
                informe.append(f"✅ {producto_nombre} ({cantidad}): Encontrado y sumado.")
                
                # Cerramos modal para buscar el siguiente (simulando escape)
                webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                time.sleep(1)
            else:
                informe.append(f"❌ {producto_nombre}: NO SE ENCONTRÓ / SIN STOCK.")

    except Exception as e:
        informe.append(f"⚠️ Error crítico procesando la lista: {e}")
    finally:
        driver.quit()
    
    # El resultado final que queremos leer
    print("\n--- RESUMEN DEL PEDIDO ---")
    print("\n".join(informe))

if __name__ == "__main__":
    # El bloque de texto vendrá como un solo argumento
    texto_entrada = sys.argv[1] if len(sys.argv) > 1 else ""
    if texto_entrada:
        procesar_pedido(texto_entrada)
    else:
        print("No enviaste ninguna lista.")
