import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def ejecutar_pedido():
    # Leemos los datos que nos manda el "Oído"
    pedido_raw = os.getenv("PEDIDO_DATA", "Sin datos")
    
    # Separamos los datos (Asumimos el formato que me dijiste)
    lineas = pedido_raw.split('|')
    productos = lineas[0]
    nombre = lineas[1]
    direccion = lineas[2]

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get("https://distribuidoradelsur.com.ar")
        # Aquí va la lógica de búsqueda y carga que ya vimos
        print(f"Procesando pedido de {nombre} en {direccion} con los productos: {productos}")
        
        # ... (resto del código de carga)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    ejecutar_pedido()
