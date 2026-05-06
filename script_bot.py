import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def ejecutar_bot():
    # 1. Recuperar datos (Ej: "Brahma-2|Juan|Calle 123")
    datos_recibidos = sys.argv[1] if len(sys.argv) > 1 else ""
    if not datos_recibidos:
        print("No se recibieron datos de WhatsApp.")
        return
    
    partes = datos_recibidos.split('|')
    producto_buscado = partes[0].split('-')[0] # Extrae "Brahma"
    cantidad = partes[0].split('-')[1] if '-' in partes[0] else "1"

    print(f"🤖 Buscando: {producto_buscado} (Cantidad: {cantidad})")

    # 2. Configuración de Chrome para GitHub Actions
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Invisible
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # 3. Entrar a la tienda
        driver.get("https://distribuidoradelsur.com.ar/tienda/#")
        time.sleep(3)

        # 4. Usar el buscador que vimos en tu código HTML
        # El input se llama 'txtBuscar'
        buscador = driver.find_element(By.NAME, "txtBuscar")
        buscador.send_keys(producto_buscado)
        buscador.send_keys(Keys.ENTER)
        time.sleep(3)

        # 5. Ver resultados
        print("Resultados encontrados. Tomando captura de pantalla...")
        driver.save_screenshot("resultado_busqueda.png")
        
        # 6. Intentar hacer clic en el primer producto
        # En tu HTML, los productos están en la clase 'portfolio-item'
        productos = driver.find_elements(By.CLASS_NAME, "portfolio-item")
        if productos:
            productos[0].click()
            time.sleep(2)
            driver.save_screenshot("producto_abierto.png")
            print("Producto seleccionado con éxito.")
            
            # NOTA: Mañana cuando abra la tienda, buscaremos el ID del botón 
            # "Agregar al carrito" que ahora no aparece por estar cerrada.
        else:
            print("No se encontró el producto.")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    ejecutar_bot()
