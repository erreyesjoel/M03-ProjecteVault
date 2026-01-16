import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Configuració inicial
driver = webdriver.Chrome() # O webdriver.Firefox()
file_path = "file://" + os.path.abspath("login.html")

# 2. Llista de contrasenyes per l'atac de diccionari
passwords = ['1234', 'qwerty', 'admin', 'password123', 'letmein']
usuari_target = "admin"

try:
    for pwd in passwords:
        # Obrir la pàgina
        driver.get(file_path)
        
        # Localitzar els elements del formulari
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "loginBtn")

        # Injectar dades
        username_field.send_keys(usuari_target)
        password_field.send_keys(pwd)
        
        print(f"Provant contrasenya: {pwd}")
        
        # Clicar botó
        login_button.click()
        
        # Esperar un moment perquè s'actualitzi el DOM
        time.sleep(1)
        
        # 3. Assert de Seguretat i Evidence Collection
        resultat = driver.find_element(By.ID, "message").text
        
        if resultat == "ACCESS_GRANTED":
            print("-------------------------")
            print("VULNERABILITAT TROBADA")
            print(f"Contrasenya correcta: {pwd}")
            print("-------------------------")
            
            # Captura de pantalla automàtica
            driver.save_screenshot('hacked.png')
            break # Aturem l'atac un cop hem entrat

finally:
    # Tancar el navegador després d'uns segons
    time.sleep(2)
    driver.quit()