import time
from datetime import date, datetime

import pandas as pd
import os
import fitz
import glob
import re
import numpy as np
import warnings
warnings.filterwarnings('ignore')

warnings.filterwarnings("ignore", category=UserWarning, module="PyPDF2")

import locale
locale.setlocale(locale.LC_MONETARY, 'en_US.UFT-8')

import os
from tika import parser
import re

import threading

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains



class Limpieza():
    def __init__(self,dato):
        self.dato = dato
    def precio(self): 
        lista = ['PRECIO',':',' ',',','MXN','$',')','(']
        y = self.dato.upper()
        for i in lista:
            y = y.replace(i,'').strip()
        return y
    def cp(self):
        y = (5-len(self.dato))*'0'+self.dato
        return y
    def auto(self):
        y = self.dato.upper()
        palabras = ['SEDAN','COUPE','CONVERTIBLE']
        for i in palabras:
            y = y.replace(i,'').strip()
        return y
    def moneda(self):
        return locale.currency(float(self.dato),grouping=True)
    
    def Normalizar(self):
        acentos_dict = {"Á":"A","É":"E","Í":"I","Ó":"O","Ú":"U",'á':'a','é':'e','í':'i','ó':'o','ú':'u'}
        y = self.dato
        for con_acento, sin_acento in acentos_dict.items():
            y = y.replace(con_acento, sin_acento)
        return y
    
class Wait_Scrap():
    def __init__(self,driver,seconds):
        self.driver = driver
        self.seconds = seconds
        self.wait = WebDriverWait(self.driver, self.seconds)
    def xpath(self,ruta):
        wait = self.wait
        element = wait.until(EC.presence_of_element_located((By.XPATH, ruta)))
        return element
    def class_name(self,ruta):
        wait = self.wait
        element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, ruta)))
        return element
    def css_selector(self,ruta):
        wait = self.wait
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ruta)))
        return element
        
class Find_Scrap():
    def __init__(self,driver):
        self.driver = driver
    def xpath_p(self,ruta):
        elements  = self.driver.find_elements(By.XPATH,ruta)
        return elements
    def xpath_s(self,ruta):
        element  = self.driver.find_element(By.XPATH,ruta)
        return element
    def css_p(self,ruta):
        elements  = self.driver.find_elements(By.CSS_SELECTOR,ruta)
        return elements
    def css_s(self,ruta):
        element  = self.driver.find_element(By.CSS_SELECTOR,ruta)
        return element
    def class_p(self,ruta):
        elements  = self.driver.find_elements(By.CLASS_NAME,ruta)
        return elements
    def class_s(self,ruta):
        element  = self.driver.find_element(By.CLASS_NAME,ruta)
        return element
    def id_p(self,ruta):
        elements  = self.driver.find_elements(By.ID,ruta)
        return elements
    def id_s(self,ruta):
        element  = self.driver.find_element(By.ID,ruta)
        return element
    

class Find_Wait_Scrap():
    def __init__(self,driver):
        self.driver = driver
    def xpath_p(self,ruta):
        elements = 0
        for second in range(1,25):
            time.sleep(1)
            try:
                elements = self.driver.find_elements(By.XPATH,ruta)
                break
            except:
                continue
        return elements
    def xpath_s(self,ruta):
        element = 0
        for second in range(1,25):
            time.sleep(1)
            try:
                element = self.driver.find_element(By.XPATH,ruta)
                break
            except:
                continue
        return element
    def css_p(self,ruta):
        elements = 0
        for second in range(1,25):
            time.sleep(1)
            try:
                elements = self.driver.find_elements(By.CSS_SELECTOR,ruta)
                break
            except:
                continue
        return elements
    def css_s(self,ruta):
        element = 0
        for second in range(1,25):
            time.sleep(1)
            try:
                element = self.driver.find_element(By.CSS_SELECTOR,ruta)
                break
            except:
                continue
        return element
    def class_p(self,ruta):
        elements = 0
        for second in range(1,25):
            time.sleep(1)
            try:
                elements = self.driver.find_elements(By.CLASS_NAME,ruta)
                break
            except:
                continue
        return elements
    def class_s(self,ruta):
        element = 0
        for second in range(1,25):
            time.sleep(1)
            try:
                element = self.driver.find_element(By.CLASS_NAME,ruta)
                break
            except:
                continue
        return element
    def id_p(self,ruta):
        elements = 0
        for second in range(1,25):
            time.sleep(1)
            try:
                elements = self.driver.find_elements(By.ID,ruta)
                break
            except:
                continue
        return elements
    def id_s(self,ruta):
        element = 0
        for second in range(1,25):
            time.sleep(1)
            try:
                element = self.driver.find_element(By.ID,ruta)
                break
            except:
                continue
        return element
    
def Click_Wait(element):
    for s in range(0,25):
        try:
            element.click()
            break
        except:
            time.sleep(1)


def Select_Wait(element):
    a=0
    for s in range(0,25):
        try:
            a = Select(element)
            break
        except:
            time.sleep(1)
    return a