import datetime
import pandas as pd
import numpy as np
import csv

def update(file_name):
    datos_pandas = leer_datos(file_name)
    funcion_maximo(datos_pandas,file_name)
    funcion_Minimo(datos_pandas,file_name)
    funcion_Mediana(datos_pandas,file_name)
    funcion_Promedio(datos_pandas,file_name)
    funcion_Desviacion(datos_pandas,file_name)
    funcion_Varianza(datos_pandas,file_name)
 
 
    datos_graficar = leer_datos(file_name)
    return datos_graficar

def save(data, file_name):
  with open(file_name, 'a', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(data)


def funcion_maximo(datos,file_name):
    now=datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    
    maximo=valores_temperatura.max()
    
    dato_guardar = [1, date_string, "Maximo", maximo]
    save(dato_guardar,file_name)
    return maximo

def funcion_Minimo(datos,file_name):
    now=datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    
    minimo=valores_temperatura.min()
    
    dato_guardar = [1, date_string, "Minimo", minimo]
    save(dato_guardar,file_name)
    return minimo

def funcion_Mediana(datos,file_name):
    now=datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    
    mediana=valores_temperatura.median()
    
    dato_guardar = [1, date_string, "Mediana", mediana]
    save(dato_guardar,file_name)
    return mediana

def funcion_Promedio(datos,file_name):
    now=datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    
    promedio=valores_temperatura.mean()
    
    dato_guardar = [1, date_string, "Promedio", promedio]
    save(dato_guardar,file_name)
    return promedio

def funcion_Desviacion(datos,file_name):
    now=datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    
    desviacion=np.std(valores_temperatura)
    
    dato_guardar = [1, date_string, "Desviacion", desviacion]
    save(dato_guardar,file_name)
    return desviacion

def funcion_Varianza(datos,file_name):
    now=datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    
    varianza=np.var(valores_temperatura)
    
    dato_guardar = [1, date_string, "Varianza", varianza]
    save(dato_guardar,file_name)
    return varianza


def leer_datos(file_name):
    datos_pandas = pd.read_csv(file_name, index_col=0, parse_dates=True)
    return datos_pandas