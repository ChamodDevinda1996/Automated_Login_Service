import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
     # Get the path to the directory containing this script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the WebDriver executable
    webdriver_path = os.path.join(script_directory, 'msedgedriver.exe')

    # s = Service('C:\\Users\\Chamod.Devinda\\Downloads\\Selenium\\msedgedriver.exe')
    # driver = webdriver.Edge(service=s)

    edge_service = Service(webdriver_path)
    driver = webdriver.Edge(service=edge_service)

    driver.get("https://app.mihcm.com/")

    wait = WebDriverWait(driver, 20)

    wait.until(EC.presence_of_all_elements_located((By.XPATH,"""/html/body/div/div[2]/div[2]/div[1]/form/div[1]/input""")))

    username = driver.find_element(By.XPATH,"""/html/body/div/div[2]/div[2]/div[1]/form/div[1]/input""")
    username.send_keys("chamod.devinda@kaleris.com")

    password = driver.find_element(By.XPATH,"""/html/body/div/div[2]/div[2]/div[1]/form/div[2]/input""")
    password.send_keys("Cham!k2@Ka13r!s")

    driver.find_element(By.XPATH,"""//*[@id="btnSignin"]""").click()
    
    wait.until(EC.presence_of_element_located((By.XPATH,"""/html/body/aside/div/nav/ul/li[1]""")))
    driver.find_element(By.XPATH,"""/html/body/aside/div/nav/ul/li[1]""").click()

    wait.until(EC.presence_of_element_located((By.XPATH,"""/html/body/aside/div/div[2]/div/ul/li/ul/li[2]""")))
    driver.find_element(By.XPATH,"""/html/body/aside/div/div[2]/div/ul/li/ul/li[2]""").click()

    wait.until(EC.presence_of_all_elements_located((By.XPATH,"""/html/body/aside/div/div[2]/div/ul/li/ul/li[2]/ul/ul/li[3]/a""")))
    driver.find_element(By.XPATH,"""/html/body/aside/div/div[2]/div/ul/li/ul/li[2]/ul/ul/li[3]/a""").click()

    wait.until(EC.presence_of_all_elements_located((By.XPATH,"""/html/body/div[1]/section/div/div[2]/div/div[1]/div[2]/button/span[1]""")))
    driver.find_element(By.XPATH,"""/html/body/div[1]/section/div/div[2]/div/div[1]/div[2]/button/span[1]""").click()

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    time.sleep(20)
    driver.quit()