from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions

options = EdgeOptions()
driver = webdriver.Edge(options=options)
driver.get("http://10.242.2.107:8586")

driver.title

driver.implicitly_wait(0.5)
# LOGUEO
clave = driver.find_element(By.ID, "usr_clave")
ok_btn = driver.find_element(By.ID, "btn_ingresarOk")
clave.send_keys("268188606")
ok_btn.click()

driver.implicitly_wait(2)

si_btn = driver.find_element(By.ID, "alertify-ok")
si_btn.click()

#Inicio Orden Pedido
driver.implicitly_wait(2)
comentario = driver.find_element(By.ID, "comentario")
comentario.send_keys("Prueba Automatizada con SELENIUM")
driver.implicitly_wait(2)
ok_teclado_btn = driver.find_element(By.ID, "btn_ok_teclado")
ok_teclado_btn.click()

#Toma de Orden Pedido

driver.implicitly_wait(2)
p1 = driver.find_element(By.ID, "btn_p5880A84F-CD7D-EB11-85AA-0003FFE492A0")
print('Seleccionando producto 1: ' + p1.text)
p2 = driver.find_element(By.ID, "btn_p17471F3E-D8BF-EA11-9B05-000D3A0177E9")
print('Seleccionando producto 2: ' + p2.text)
p1.click()
driver.implicitly_wait(2)
si_btn = driver.find_element(By.ID, "alertify-ok")
si_btn.click()
p2.click()
driver.implicitly_wait(2)
si_btn = driver.find_element(By.ID, "alertify-ok")
si_btn.click()
driver.implicitly_wait(2)
pepsi = driver.find_element(By.ID, "pl_prgt_sug_pcn288_1")
print('Seleccionando pregunta sugerida: ' + pepsi.text)
pepsi.click()
driver.implicitly_wait(2)
print('Seleccionando pregunta sugerida: ' + pepsi.text)
pepsi.click()
driver.implicitly_wait(2)
print('Seleccionando pregunta sugerida: ' + pepsi.text)
pepsi.click()
driver.implicitly_wait(2)
continuar = driver.find_element(By.ID, "btn_prgnts_sgrds_cnfrmar")
continuar.click()
driver.implicitly_wait(2)
cobrar = driver.find_element(By.ID, "cobrar")
cobrar.click()

# Facturar
driver.implicitly_wait(2)
aplicar_pago = driver.find_element(By.ID, "btnAplicarPago")
aplicar_pago.click()
#driver.quit()