import unittest
import os
import time
import json
import pyautogui
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestDesafioautomatizacionqa(unittest.TestCase):
    def setup_method(self, method):
      self.driver = webdriver.Chrome(executable_path=r"C:\\proyecto\\driver\\chromedriver.exe")
      self.vars = {}
  
    def teardown_method(self, method):
      self.driver.quit()
  
    def test_desafioautomatizacionqa(self):
      self.driver = webdriver.Chrome(executable_path=r"C:\\proyecto\\driver\\chromedriver.exe")
      self.driver.get("https://opencart.abstracta.us/")
      self.driver.set_window_size(1936, 1048)
      self.driver.find_element(By.NAME, "search").click()
      self.driver.find_element(By.CSS_SELECTOR, ".col-sm-5").click()
      self.driver.find_element(By.NAME, "search").send_keys("imac")
      self.driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)
      #element = self.driver.find_element(By.CSS_SELECTOR, ".button-group > button:nth-child(2)")
      click=self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div/div/div[2]/div[2]/button[1]/span")
      actions = ActionChains(self.driver)
      actions.click(click).perform()
      time.sleep(3)
      click=self.driver.find_element_by_xpath("/html/body/div[2]/ul/li[1]/a/i")
      actions = ActionChains(self.driver)
      actions.click(click).perform()
      self.driver.find_element(By.NAME, "search").click()
      self.driver.find_element(By.NAME, "search").send_keys("ipod Classic")
      time.sleep(3)
      self.driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)
      #self.driver.find_element(By.CSS_SELECTOR, ".button-group .hidden-xs hidden-sm hidden-md").click()
      click=self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div/div/div[2]/div[2]/button[1]/span")
      actions = ActionChains(self.driver)
      actions.click(click).perform()
      actions = ActionChains(self.driver)
      click=self.driver.find_element_by_xpath("/html/body/div[2]/ul/li[1]/a/i")
      actions = ActionChains(self.driver)
      actions.click(click).perform()
      self.driver.find_element(By.NAME, "search").click()
      self.driver.find_element(By.NAME, "search").send_keys("apple cinema 30")
      time.sleep(3)
      self.driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)
      #self.driver.find_element(By.CSS_SELECTOR, ".button-group .hidden-xs hidden-sm hidden-md").click()
      click=self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div/div/div[2]/div[2]/button[1]/span")
      actions = ActionChains(self.driver)
      actions.click(click).perform()
      actions = ActionChains(self.driver)####agregar al carrito
      time.sleep(3)
      radio_bt = self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/label/input")
      radio_bt.click()
      time.sleep(3)
      radio_bt = self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[4]/label/input")
      radio_bt.click()
      time.sleep(3)
      self.driver.find_element(By.ID, "input-option208").send_keys("_1")
      self.driver.find_element(By.ID, "input-option217").click()
      time.sleep(3)
      select = self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div[2]/div[2]/div[4]/select")
      opcion = select.find_elements_by_tag_name("option")
      time.sleep(3)
      for option in opcion:
          print("los valores son: %s" % option.get_attribute("value"))
          option.click()
          time.sleep(1)
      seleccionar = Select(self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div[2]/div[2]/div[4]/select"))
      seleccionar.select_by_value("2")
      time.sleep(3)
      self.driver.find_element(By.ID, "input-option209").click()
      self.driver.find_element(By.ID, "input-option209").send_keys("Data de prueba")
      time.sleep(3)
      self.driver.find_element(By.ID, "button-upload222").send_keys(r'C:\\proyecto\\prueba1.jpg') #subir archivo
      time.sleep(4)
      click2=self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div[2]/div[2]/div[10]/button")
      actions = ActionChains(self.driver)
      actions.click(click2).perform()
      actions = ActionChains(self.driver)####agregar al carrito
      time.sleep(5)
      click3=self.driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul/li[4]/a/i")
      actions = ActionChains(self.driver)
      actions.click(click3).perform()
      actions = ActionChains(self.driver)####seleccionar carrito
      time.sleep(5)
      click4=self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div[2]/a")
      actions = ActionChains(self.driver)
      actions.click(click4).perform()
      actions = ActionChains(self.driver)####chekout
      time.sleep(3)
      click5=self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/input")
      actions = ActionChains(self.driver)
      actions.click(click5).perform()
      actions = ActionChains(self.driver)####continue
      time.sleep(3)
      with open('datos.txt') as file:
        for i, line in enumerate(file)
            usuario = (line)
            sep = ","
            dividir = usuario.split(sep)
            try:
              gotdata = dividir[1]
              user =  dividir[0]
              apell = dividir[1]
            except IndexError:
              gotdata = 'null'
            print(user)
            print(apell)


      self.driver.find_element(By.ID, "input-payment-firstname").send_keys(user)
      self.driver.find_element(By.ID, "input-payment-lastname").send_keys(apell)
if __name__ == '__main__':
unittest.main()