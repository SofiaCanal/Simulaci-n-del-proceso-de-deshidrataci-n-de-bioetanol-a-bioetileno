# -*- coding: utf-8 -*-
"""
Created on Saturday Dic 03 09:30:30 2022

@author: Sofia Canal
"""

import sympy as sym
from ipywidgets import interactive, fixed, FloatSlider, interactive, Dropdown, IntText
from sympy import solve
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display
from tabulate import tabulate
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#DEFICIÓN DE BOTONES
run_button = widgets.Button(description = 'Mostrar')
run_button2 = widgets.Button(description = 'Mostrar')
#CÓDIGO PARA EL PFR 1
def PFR1(XE = 0.7109, caso = 'Caudal'):
    
    #Datos
    F1 = 6600            #Caudal de alimentación fresca
    S_Et = 0.68          #Selectividad del etileno
    #Variables
    variables = sym.var('F1_E F1_H2O F3 F3_E F3_DEE F3_A F3_B F3_H2O F3_CO F3_CO2 F3_M F3_H F3_Et xi_2 xi_3 xi_4 xi_5 xi_6 xi_7 xi_8')
    global F3
    
    #Ecuaciones de balance
    balances = [
    sym.Eq(0, F1_E - 2*xi_2 - xi_4 - xi_6 - xi_7 - F3_E),
    sym.Eq(0, xi_2 - xi_3 - F3_DEE),
    sym.Eq(0, xi_4 - F3_A),
    sym.Eq(0, 0.5*xi_5 - F3_B),
    sym.Eq(0, F1_H2O + xi_2 + xi_3 - xi_7 - xi_8 - F3_H2O),
    sym.Eq(0, xi_6 + 2*xi_7 - xi_8 - F3_CO),
    sym.Eq(0, xi_8 - F3_CO2),
    sym.Eq(0, xi_6 - F3_M),
    sym.Eq(0, xi_4 + xi_6 + 4*xi_7 + xi_8 - F3_H),
    sym.Eq(0, 2*xi_3 - xi_5 - F3_Et)
    ]
    
    #Especificaciones
    especificaciones = [
        
    sym.Eq(F3, F3_E + F3_H2O + F3_DEE + F3_A + F3_B + F3_CO + F3_CO2 + F3_M + F3_H + F3_Et),
        
    sym.Eq(F1_E, 0.25*F1),             #Alimentación con un 25% de etanol
    sym.Eq(F1_H2O, 0.75*F1),           #Alimentación con un 75% de agua
    
    sym.Eq(F3_E, (1-XE)*F1_E),         #Composición etanol utilizando la conversión
    sym.Eq(F3_A, F3*(0.0018/100)),     #Composición acetaldehído
    sym.Eq(F3_DEE, F3*(2.5274/100)),   #Composición dietiléter
    sym.Eq(F3_CO, F3*(0.0005/100)),    #Composición monóxido de carbono
    sym.Eq(F3_B, F3*(0.0019/100)),     #Composición buteno
    sym.Eq(F3_M, F3*(0.0006/100)),     #Composición metano
        
    sym.Eq(F3_Et, S_Et*(F1_E-F3_E))   #Selectividad del etileno
    
    ]
    
    ecuaciones = balances + especificaciones
    
    #Resolución
    soln = solve(ecuaciones)
    
    #Output
    fig, ax1 = plt.subplots(figsize=(7,7))
    img = mpimg.imread('./imagenes/PFR_1.png')
    imgplot = plt.imshow(img)
    plt.axis('off')
    
    if caso == 'Caudal':
        txt1 = "Etanol: "+str(round(soln[F3_E],4))+" kmol/h\n"
        txt2 = "Dietiléter: "+str(round(soln[F3_DEE],4))+ " kmol/h\n"
        txt3 = "Acetaldehído: "+str(round(soln[F3_A],4))+ " kmol/h\n"
        txt4 = "Buteno: "+str(round(soln[F3_B],4))+ " kmol/h\n"
        txt5 = "Agua: "+str(round(soln[F3_H2O],4))+ " kmol/h\n"
        txt6 = "Monóxido de carbono: "+str(round(soln[F3_CO],4))+ " kmol/h\n"
        txt7 = "Dióxido de carbono: "+str(round(soln[F3_CO2],4))+ " kmol/h\n"
        txt8 = "Metano: "+str(round(soln[F3_M],4))+ " kmol/h\n"
        txt9 = "Hidrógeno: "+str(round(soln[F3_H],4))+ " kmol/h\n"
        txt10 = "Etileno: "+str(round(soln[F3_Et],4))+ " kmol/h\n"
        txt = txt1 + txt2 + txt3 + txt4 + txt5 + txt6 + txt7 + txt8 + txt9 + txt10
        plt.text(320,105,txt, size=14)
        
        
    elif caso == 'Porcentaje':
        txt1 = "Etanol: "+str(round(100*(soln[F3_E]/soln[F3]),4))+" %\n"
        txt2 = "Dietiléter: "+str(round(100*(soln[F3_DEE]/soln[F3]),4))+ " %\n"
        txt3 = "Acetaldehído: "+str(round(100*(soln[F3_A]/soln[F3]),4))+ " %\n"
        txt4 = "Buteno: "+str(round(100*(soln[F3_B]/soln[F3]),4))+ " %\n"
        txt5 = "Agua: "+str(round(100*(soln[F3_H2O]/soln[F3]),4))+ " %\n"
        txt6 = "Monóxido de carbono: "+str(round(100*(soln[F3_CO]/soln[F3]),4))+ " %\n"
        txt7 = "Dióxido de carbono: "+str(round(100*(soln[F3_CO2]/soln[F3]),4))+ " %\n"
        txt8 = "Metano: "+str(round(100*(soln[F3_M]/soln[F3]),4))+ " %\n"
        txt9 = "Hidrógeno: "+str(round(100*(soln[F3_H]/soln[F3]),4))+ " %\n"
        txt10 = "Etileno: "+str(round(100*(soln[F3_Et]/soln[F3]),4))+ " %\n"
        txt = txt1 + txt2 + txt3 + txt4 + txt5 + txt6 + txt7 + txt8 + txt9 + txt10
        plt.text(320,105,txt, size=14)        

#CÓDIGO PARA EL PFR 2
def PFR2(XE = 0.5801, caso = 'Caudal'):
    
    #Variables
    variables = sym.var('F3 F3_E F3_DEE F3_A F3_B F3_H2O F3_CO F3_CO2 F3_M F3_H F3_Et F15 F15_E F15_DEE F15_A F15_B F15_H2O F15_CO F15_CO2 F15_M F15_H F15_Et F4 F4_E F4_DEE F4_A F4_B F4_H2O F4_CO F4_CO2 F4_M F4_H F4_Et F7 F7_E F7_DEE F7_A F7_B F7_H2O F7_CO F7_CO2 F7_M F7_H F7_Et xi_2 xi_3 xi_4 xi_5 xi_6 xi_7 xi_8')
    
    #Ecuaciones de balance
    balances = [
        sym.Eq(0, F4_E - 2*xi_2 - xi_4 - xi_6 - xi_7 - F7_E),
        sym.Eq(0, F4_DEE + xi_2 - xi_3 - F7_DEE),
        sym.Eq(0, F4_A + xi_4 - F7_A),
        sym.Eq(0, F4_B + 0.5*xi_5 - F7_B),
        sym.Eq(0, F4_H2O + xi_2 + xi_3 - xi_7 - xi_8 - F7_H2O),
        sym.Eq(0, F4_CO + xi_6 + 2*xi_7 - xi_8 - F7_CO),
        sym.Eq(0, F4_CO2 + xi_8 - F7_CO2),
        sym.Eq(0, F4_M + xi_6 - F7_M),
        sym.Eq(0, F4_H + xi_4 + xi_6 + 4*xi_7 + xi_8 - F7_H),
        sym.Eq(0, F4_Et + 2*xi_3 - xi_5 - F7_Et)
    ]
    
    #Especificaciones
    especificaciones = [
        
        sym.Eq(F3_E, 476.850000000000),   
        sym.Eq(F3_DEE, 187.003743385105),
        sym.Eq(F3_A, 0.13318300945366),
        sym.Eq(F3_B, 0.14058206553442),
        sym.Eq(F3_H2O, 5935.94827320175),
        sym.Eq(F3_CO, 0.03699528040380),
        sym.Eq(F3_CO2, 0.01390256164592),
        sym.Eq(F3_M, 0.04439433648455),
        sym.Eq(F3_H, 0.20448691871446),
        sym.Eq(F3_Et, 798.680520000000),

        sym.Eq(F15_E, 109),   
        sym.Eq(F15_DEE, 0.31),
        sym.Eq(F15_A, 0.3),
        sym.Eq(F15_B, 0.005),
        sym.Eq(F15_H2O, 490),
        sym.Eq(F15_CO, 0),
        sym.Eq(F15_CO2, 0.005),
        sym.Eq(F15_M, 0),
        sym.Eq(F15_H, 0),
        sym.Eq(F15_Et, 0.8),

        sym.Eq(F4_E, F3_E + F15_E),   
        sym.Eq(F4_DEE, F3_DEE + F15_DEE ),
        sym.Eq(F4_A, F3_A + F15_A),
        sym.Eq(F4_B, F3_B + F15_B),
        sym.Eq(F4_H2O, F3_H2O + F15_H2O),
        sym.Eq(F4_CO, F3_CO + F15_CO),
        sym.Eq(F4_CO2, F3_CO2 + F15_CO2),
        sym.Eq(F4_M, F3_M + F15_M),
        sym.Eq(F4_H, F3_H + F15_H),
        sym.Eq(F4_Et, F3_Et + F15_Et),

        sym.Eq(F3, F3_E + F3_H2O + F3_DEE + F3_A + F3_B + F3_CO + F3_CO2 + F3_M + F3_H + F3_Et),
        sym.Eq(F15, F15_E + F15_H2O + F15_DEE + F15_A + F15_B + F15_CO + F15_CO2 + F15_M + F15_H + F15_Et),
        sym.Eq(F4, F4_E + F4_H2O + F4_DEE + F4_A + F4_B + F4_CO + F4_CO2 + F4_M + F4_H + F4_Et),
        sym.Eq(F7, F7_E + F7_H2O + F7_DEE + F7_A + F7_B + F7_CO + F7_CO2 + F7_M + F7_H + F7_Et),
        
        #Especificaciones PFR 2
        sym.Eq(F7_E, (1-XE)*F4_E),             #Conversión del etanol
        sym.Eq(F7_A, F7*(0.0061/100)),         #Composición del acetaldehído
        sym.Eq(F7_DEE, F7*(0.5688/100)),       #Composición del dietiléter
        sym.Eq(F7_CO, F7*(0.0009/100)),        #Composición del monóxido de carbono
        sym.Eq(F7_B, F7*(0.0108/100)),         #Composición del buteno
        sym.Eq(F7_M, F7*(0.0011/100)),         #Composición del metano
        sym.Eq(F7_Et, F7*(16.4157/100))        #Composición del etileno
        
    ]
    
    ecuaciones = balances + especificaciones
    
    #Resolucion
    soln = solve(ecuaciones)
    
    #Output
    fig, ax1 = plt.subplots(figsize=(10,10))
    img = mpimg.imread('./imagenes/PFR_2.png')
    imgplot = plt.imshow(img)
    plt.axis('off')
    
    txt4_1 = "Etanol: "+str(round(soln[F4_E],4))+" kmol/h\n"
    txt4_2 = "Dietiléter: "+str(round(soln[F4_DEE],4))+ " kmol/h\n"
    txt4_3 = "Acetaldehído: "+str(round(soln[F4_A],4))+ " kmol/h\n"
    txt4_4 = "Buteno: "+str(round(soln[F4_B],4))+ " kmol/h\n"
    txt4_5 = "Agua: "+str(round(soln[F4_H2O],4))+ " kmol/h\n"
    txt4_6 = "Monóxido de carbono: "+str(round(soln[F4_CO],4))+ " kmol/h\n"
    txt4_7 = "Dióxido de carbono: "+str(round(soln[F4_CO2],4))+ " kmol/h\n"
    txt4_8 = "Metano: "+str(round(soln[F4_M],4))+ " kmol/h\n"
    txt4_9 = "Hidrógeno: "+str(round(soln[F4_H],4))+ " kmol/h\n"
    txt4_10 = "Etileno: "+str(round(soln[F4_Et],4))+ " kmol/h\n"
    txt4_tot = txt4_1 + txt4_2 + txt4_3 + txt4_4 + txt4_5 + txt4_6 + txt4_7 + txt4_8 + txt4_9 + txt4_10
    plt.text(0, 100, txt4_tot, size=14)

                              
    if caso == 'Caudal': 
        txt1 = "Etanol: "+str(round(soln[F7_E],4))+" kmol/h\n"
        txt2 = "Dietiléter: "+str(round(soln[F7_DEE],4))+ " kmol/h\n"
        txt3 = "Acetaldehído: "+str(round(soln[F7_A],4))+ " kmol/h\n"
        txt4 = "Buteno: "+str(round(soln[F7_B],4))+ " kmol/h\n"
        txt5 = "Agua: "+str(round(soln[F7_H2O],4))+ " kmol/h\n"
        txt6 = "Monóxido de carbono: "+str(round(soln[F7_CO],4))+ " kmol/h\n"
        txt7 = "Dióxido de carbono: "+str(round(soln[F7_CO2],4))+ " kmol/h\n"
        txt8 = "Metano: "+str(round(soln[F7_M],4))+ " kmol/h\n"
        txt9 = "Hidrógeno: "+str(round(soln[F7_H],4))+ " kmol/h\n"
        txt10 = "Etileno: "+str(round(soln[F7_Et],4))+ " kmol/h\n"
        txt = txt1 + txt2 + txt3 + txt4 + txt5 + txt6 + txt7 + txt8 + txt9 + txt10
        plt.text(380,100,txt, size=14)
        
        
    elif caso == 'Porcentaje':
        txt1 = "Etanol: "+str(round(100*(soln[F7_E]/soln[F7]),4))+" %\n"
        txt2 = "Dietiléter: "+str(round(100*(soln[F7_DEE]/soln[F7]),4))+ " %\n"
        txt3 = "Acetaldehído: "+str(round(100*(soln[F7_A]/soln[F7]),4))+ " %\n"
        txt4 = "Buteno: "+str(round(100*(soln[F7_B]/soln[F7]),4))+ " %\n"
        txt5 = "Agua: " +str(round(100*(soln[F7_H2O]/soln[F7]),4))+ " %\n"
        txt6 = "Monóxido de carbono: "+str(round(100*(soln[F7_CO]/soln[F7]),4))+ " %\n"
        txt7 = "Dióxido de carbono: " +str(round(100*(soln[F7_CO2]/soln[F7]),4))+ " %\n"
        txt8 = "Metano: "+str(round(100*(soln[F7_M]/soln[F7]),4))+ " %\n"
        txt9 = "Hidrógeno: " +str(round(100*(soln[F7_H]/soln[F7]),4))+ " %\n"
        txt10 = "Etileno: "+str(round(100*(soln[F7_Et]/soln[F7]),4))+ " %\n"
        txt = txt1 + txt2 + txt3 + txt4 + txt5 + txt6 + txt7 + txt8 + txt9 + txt10
        plt.text(380,100,txt, size=14)        
    
#CÓDIGO PARA EL PFR 3 
def PFR3(XE = 0.5448, caso = 'Caudal'):
     
    #Variables
    variables = sym.var('F7_E F7_DEE F7_A F7_B F7_H2O F7_CO F7_CO2 F7_M F7_H F7_Et F10 F10_E F10_DEE F10_A F10_B F10_H2O F10_CO F10_CO2 F10_M F10_H F10_Et xi_2 xi_3 xi_4 xi_5 xi_6 xi_7 xi_8')
    
    #Ecuaciones de balance
    balances = [
        sym.Eq(0, F7_E - 2*xi_2 - xi_4 - xi_6 - xi_7 - F10_E),
        sym.Eq(0, F7_DEE + xi_2 - xi_3 - F10_DEE),
        sym.Eq(0, F7_A + xi_4 - F10_A),
        sym.Eq(0, F7_B + 0.5*xi_5 - F10_B),
        sym.Eq(0, F7_H2O + xi_2 + xi_3 - xi_7 - xi_8 - F10_H2O),
        sym.Eq(0, F7_CO + xi_6 + 2*xi_7 - xi_8 - F10_CO),
        sym.Eq(0, F7_CO2 + xi_8 - F10_CO2),
        sym.Eq(0, F7_M + xi_6 - F10_M),
        sym.Eq(0, F7_H + xi_4 + xi_6 + 4*xi_7 + xi_8 - F10_H),
        sym.Eq(0, F7_Et + 2*xi_3 - xi_5 - F10_Et)
    ]
    
    #Especificaciones
    especificaciones = [
        sym.Eq(F7_E, 245.939830000000),          #Composición etanol
        sym.Eq(F7_A, 0.52553648525995),         #Composición acetaldehído
        sym.Eq(F7_DEE, 49.0041234124356),       #Composición dietiléter
        sym.Eq(F7_H2O, 6903.90719936866),     #Composición de agua
        sym.Eq(F7_CO, 0.07753816995639),       #Composición monóxido de carbono
        sym.Eq(F7_CO2, 0.08288628184530),       #Composición del dióxido de carbono
        sym.Eq(F7_B, 0.93045803947663),         #Composición del buteno
        sym.Eq(F7_M, 0.09476887439114),         #Composición del metano
        sym.Eq(F7_H, 0.51950279631748),        #Composición de hidrógeno
        sym.Eq(F7_Et, 1414.27037394782),        #Composición  etileno

        sym.Eq(F10, F10_E + F10_H2O + F10_DEE + F10_A + F10_B + F10_CO + F10_CO2 + F10_M + F10_H + F10_Et),
        
        sym.Eq(F10_E, (1-XE)*F7_E),             #Conversión etanol 
        sym.Eq(F10_A, F10*(0.00679/100)),         #Composición acetaldehído
        sym.Eq(F10_DEE, F10*(0.0395/100)),       #Composición dietiléter
        sym.Eq(F10_CO, F10*(0.00249/100)),       #Composición monóxido de carbono
        sym.Eq(F10_B, F10*(0.05658/100)),         #Composición del buteno
        sym.Eq(F10_M, F10*(0.0034/100)),         #Composición del metano
        sym.Eq(F10_Et, F10*(18.45599/100))        #Composición  etileno
    ]
    
    ecuaciones = balances + especificaciones
    
    #Resolución
    soln = solve(ecuaciones)
    
    #Output
    fig, ax1 = plt.subplots(figsize=(10,10))
    img = mpimg.imread('./imagenes/PFR_3.png')
    imgplot = plt.imshow(img)
    plt.axis('off')
    
    txt7_1 = "Etanol: "+str(round(soln[F7_E],4))+" kmol/h\n"
    txt7_2 = "Dietiléter: "+str(round(soln[F7_DEE],4))+ " kmol/h\n"
    txt7_3 = "Acetaldehído: "+str(round(soln[F7_A],4))+ " kmol/h\n"
    txt7_4 = "Buteno: "+str(round(soln[F7_B],4))+ " kmol/h\n"
    txt7_5 = "Agua: "+str(round(soln[F7_H2O],4))+ " kmol/h\n"
    txt7_6 = "Monóxido de carbono: "+str(round(soln[F7_CO],4))+ " kmol/h\n"
    txt7_7 = "Dióxido de carbono: "+str(round(soln[F7_CO2],4))+ " kmol/h\n"
    txt7_8 = "Metano: "+str(round(soln[F7_M],4))+ " kmol/h\n"
    txt7_9 = "Hidrógeno: "+str(round(soln[F7_H],4))+ " kmol/h\n"
    txt7_10 = "Etileno: "+str(round(soln[F7_Et],4))+ " kmol/h\n"
    txt7_tot = txt7_1 + txt7_2 + txt7_3 + txt7_4 + txt7_5 + txt7_6 + txt7_7 + txt7_8 + txt7_9 + txt7_10
    plt.text(0, 100, txt7_tot, size=14)

    
    if caso == 'Caudal': 
        txt1 = "Etanol: "+str(round(soln[F10_E],4))+" kmol/h\n"
        txt2 = "Dietiléter: "+str(round(soln[F10_DEE],4))+ " kmol/h\n"
        txt3 = "Acetaldehído: "+str(round(soln[F10_A],4))+ " kmol/h\n"
        txt4 = "Buteno: "+str(round(soln[F10_B],4))+ " kmol/h\n"
        txt5 = "Agua: "+str(round(soln[F10_H2O],4))+ " kmol/h\n"
        txt6 = "Monóxido de carbono: "+str(round(soln[F10_CO],4))+ " kmol/h\n"
        txt7 = "Dióxido de carbono: "+str(round(soln[F10_CO2],4))+ " kmol/h\n"
        txt8 = "Metano: "+str(round(soln[F10_M],4))+ " kmol/h\n"
        txt9 = "Hidrógeno: "+str(round(soln[F10_H],4))+ " kmol/h\n"
        txt10 = "Etileno: "+str(round(soln[F10_Et],4))+ " kmol/h\n"
        txt = txt1 + txt2 + txt3 + txt4 + txt5 + txt6 + txt7 + txt8 + txt9 + txt10
        plt.text(380,100,txt, size=14)
        
        
    elif caso == 'Porcentaje':
        txt1 = "Etanol: "+str(round(100*(soln[F10_E]/soln[F10]),4))+" %\n"
        txt2 = "Dietiléter: "+str(round(100*(soln[F10_DEE]/soln[F10]),4))+ " %\n"
        txt3 = "Acetaldehído: "+str(round(100*(soln[F10_A]/soln[F10]),4))+ " %\n"
        txt4 = "Buteno: "+str(round(100*(soln[F10_B]/soln[F10]),4))+ " %\n"
        txt5 = "Agua: " +str(round(100*(soln[F10_H2O]/soln[F10]),4))+ " %\n"
        txt6 = "Monóxido de carbono: "+str(round(100*(soln[F10_CO]/soln[F10]),4))+ " %\n"
        txt7 = "Dióxido de carbono: " +str(round(100*(soln[F10_CO2]/soln[F10]),4))+ " %\n"
        txt8 = "Metano: "+str(round(100*(soln[F10_M]/soln[F10]),4))+ " %\n"
        txt9 = "Hidrógeno: " +str(round(100*(soln[F10_H]/soln[F10]),4))+ " %\n"
        txt10 = "Etileno: "+str(round(100*(soln[F10_Et]/soln[F10]),4))+ " %\n"
        txt = txt1 + txt2 + txt3 + txt4 + txt5 + txt6 + txt7 + txt8 + txt9 + txt10
        plt.text(380,100,txt, size=14)        

def ProcesoC(XE1 = 0.711, XE2 = 0.5802, XE3 = 0.5448, caso = 'C3'):
    
    #Variables
    variables = [
    sym.var('F1_E F1_H2O'),
    sym.var('F3_E F3_DEE F3_A F3_B F3_H2O F3_CO F3_CO2 F3_M F3_H F3_Et'),
    sym.var('F4 F4_E F4_DEE F4_A F4_B F4_H2O F4_CO F4_CO2 F4_M F4_H F4_Et'),
    sym.var('F15_E F15_DEE F15_A F15_B F15_H2O F15_CO F15_CO2 F15_M F15_H F15_Et'),
    sym.var('F7 F7_E F7_DEE F7_A F7_B F7_H2O F7_CO F7_CO2 F7_M F7_H F7_Et'),
    sym.var('F10 F10_E F10_DEE F10_A F10_B F10_H2O F10_CO F10_CO2 F10_M F10_H F10_Et'),
    sym.var('F12_E F12_DEE F12_A F12_B F12_H2O F12_CO F12_CO2 F12_M F12_H F12_Et'),
    sym.var('F13_E F13_DEE F13_A F13_B F13_H2O F13_CO F13_CO2 F13_M F13_H F13_Et'),
    sym.var('F16_E F16_DEE F16_A F16_B F16_H2O F16_CO F16_CO2 F16_M F16_H F16_Et'),
    sym.var('xi_21 xi_31 xi_41 xi_51 xi_61 xi_71 xi_81'),
    sym.var('xi_22 xi_32 xi_42 xi_52 xi_62 xi_72 xi_82'),
    sym.var('xi_23 xi_33 xi_43 xi_53 xi_63 xi_73 xi_83')
    ]
    
    #Ecuaciones de balance
    PFR1 = [
        sym.Eq(0, F1_E - 2*xi_21 - xi_41 - xi_61 - xi_71 - F3_E),
        sym.Eq(0, xi_21 - xi_31 - F3_DEE),
        sym.Eq(0, xi_41 - F3_A),
        sym.Eq(0, 0.5*xi_51 - F3_B),
        sym.Eq(0, F1_H2O + xi_21 + xi_31 - xi_71 - xi_81 - F3_H2O),
        sym.Eq(0, xi_61 + 2*xi_71 - xi_81 - F3_CO),
        sym.Eq(0, xi_81 - F3_CO2),
        sym.Eq(0, xi_61 - F3_M),
        sym.Eq(0, xi_41 + xi_61 + 4*xi_71 + xi_81 - F3_H),
        sym.Eq(0, 2*xi_31 - xi_51 - F3_Et)
    ]

    mezclador = [
        sym.Eq(F4_E, F15_E + F3_E),
        sym.Eq(F4_DEE, F15_DEE + F3_DEE),
        sym.Eq(F4_A, F15_A + F3_A),
        sym.Eq(F4_B, F15_B + F3_B),
        sym.Eq(F4_H2O, F15_H2O + F3_H2O),
        sym.Eq(F4_CO, F15_CO + F3_CO),
        sym.Eq(F4_CO2, F15_CO2 + F3_CO2),
        sym.Eq(F4_M, F15_M + F3_M),
        sym.Eq(F4_H, F15_H + F3_H),
        sym.Eq(F4_Et, F15_Et + F3_Et)
    ]

    PFR2 = [
        sym.Eq(0, F4_E - 2*xi_22 - xi_42 - xi_62 - xi_72 - F7_E),
        sym.Eq(0, F4_DEE + xi_22 - xi_32 - F7_DEE),
        sym.Eq(0, F4_A + xi_42 - F7_A),
        sym.Eq(0, F4_B + 0.5*xi_52 - F7_B),
        sym.Eq(0, F4_H2O + xi_22 + xi_32 - xi_72 - xi_82 - F7_H2O),
        sym.Eq(0, F4_CO + xi_62 + 2*xi_72 - xi_82 - F7_CO),
        sym.Eq(0, F4_CO2 + xi_82 - F7_CO2),
        sym.Eq(0, F4_M + xi_62 - F7_M),
        sym.Eq(0, F4_H + xi_42 + xi_62 + 4*xi_72 + xi_82 - F7_H),
        sym.Eq(0, F4_Et + 2*xi_32 - xi_52 - F7_Et)
    ]

    PFR3 = [
        sym.Eq(0, F7_E - 2*xi_23 - xi_43 - xi_63 - xi_73 - F10_E),
        sym.Eq(0, F7_DEE + xi_23 - xi_33 - F10_DEE),
        sym.Eq(0, F7_A + xi_43 - F10_A),
        sym.Eq(0, F7_B + 0.5*xi_53 - F10_B),
        sym.Eq(0, F7_H2O + xi_23 + xi_33 - xi_73 - xi_83 - F10_H2O),
        sym.Eq(0, F7_CO + xi_63 + 2*xi_73 - xi_83 - F10_CO),
        sym.Eq(0, F7_CO2 + xi_83 - F10_CO2),
        sym.Eq(0, F7_M + xi_63 - F10_M),
        sym.Eq(0, F7_H + xi_43 + xi_63 + 4*xi_73 + xi_83 - F10_H),
        sym.Eq(0, F7_Et + 2*xi_33 - xi_53 - F10_Et)
    ]

    S1 = [
        sym.Eq(F10_E, F12_E + F13_E),
        sym.Eq(F10_DEE, F12_DEE + F13_DEE),
        sym.Eq(F10_A, F12_A + F13_A),
        sym.Eq(F10_B, F12_B + F13_B),
        sym.Eq(F10_H2O, F12_H2O + F13_H2O),
        sym.Eq(F10_CO, F12_CO + F13_CO),
        sym.Eq(F10_CO2, F12_CO2 + F13_CO2),
        sym.Eq(F10_M, F12_M + F13_M),
        sym.Eq(F10_H, F12_H + F13_H),
        sym.Eq(F10_Et, F12_Et + F13_Et)
    ]

    S2 = [
        sym.Eq(F13_E, F15_E + F16_E),
        sym.Eq(F13_DEE, F15_DEE + F16_DEE),
        sym.Eq(F13_A, F15_A + F16_A),
        sym.Eq(F13_B, F15_B + F16_B),
        sym.Eq(F13_H2O, F15_H2O + F16_H2O),
        sym.Eq(F13_CO, F15_CO + F16_CO),
        sym.Eq(F13_CO2, F15_CO2 + F16_CO2),
        sym.Eq(F13_M, F15_M + F16_M),
        sym.Eq(F13_H, F15_H + F16_H),
        sym.Eq(F13_Et, F15_Et + F16_Et)
    ]

    balances = PFR1 + mezclador + PFR2 + PFR3 + S1 + S2
    
    #Especificaciones
    F1 = 6600
    especificaciones = [
    
    #Corriente 1
    sym.Eq(F1_E, 0.25*F1),   #Alimentación con un 25% de etanol
    sym.Eq(F1_H2O, 0.75*F1),  #Alimentación con un 75% de agua
    
    #Corriente 3
    sym.Eq(F3_E, (1-XE1)*F1_E),         #CONVERSIÓN ETANOL
    sym.Eq(F3_A, 0.13318300945366),     #Composición acetaldehído
    sym.Eq(F3_DEE, 187.003743385105),   #Composición dietiléter
    sym.Eq(F3_CO, 0.03699528040380),    #Composición monóxido de carbono
    sym.Eq(F3_B, 0.14058206553442),     #Composición buteno
    sym.Eq(F3_M, 0.04439433648455),     #Composición metano
    sym.Eq(F3_Et, 798.680520000000),    #Composición etileno

    #Corriente 15
    sym.Eq(F15_E, 109),   
    sym.Eq(F15_DEE, 0.31),
    sym.Eq(F15_A, 0.3),
    sym.Eq(F15_B, 0.005),
    sym.Eq(F15_H2O, 490),
    sym.Eq(F15_CO, 0),
    sym.Eq(F15_CO2, 0.005),
    sym.Eq(F15_M, 0),
    sym.Eq(F15_H, 0),
    sym.Eq(F15_Et, 0.8),
    
    #Corriente 7
    #sym.Eq(F7_E, F7*(2.8547/100)),         #Composición etanol
    sym.Eq(F7_E, (1-XE2)*F4_E),    #CONVERSIÓN ETANOL
    sym.Eq(F7_A, F7*(0.0061/100)),         #Composición acetaldehído
    sym.Eq(F7_DEE, F7*(0.5688/100)),       #Composición dietiléter
    sym.Eq(F7_CO, F7*(0.0009/100)),        #Composición monóxido de carbono
    sym.Eq(F7_B, F7*(0.0108/100)),         #Composición del buteno
    sym.Eq(F7_M, F7*(0.0011/100)),         #Composición del metano
    sym.Eq(F7_Et, F7*(16.4157/100)),       #Composición  etileno
    sym.Eq(F7, F7_E + F7_H2O + F7_DEE + F7_A + F7_B + F7_CO + F7_CO2 + F7_M + F7_H + F7_Et),
    
    #Corriente 10 
    #sym.Eq(F10_E, F10*(1.2669/100)),        #Composición etanol 
    sym.Eq(F10_E, (1-XE3)*F7_E),             #CONVERSIÓN ETANOL
    sym.Eq(F10_A, F10*(0.0068/100)),        #Composición acetaldehído
    sym.Eq(F10_DEE, F10*(0.0395/100)),      #Composición dietiléter
    sym.Eq(F10_CO, F10*(0.0025/100)),       #Composición monóxido de carbono
    sym.Eq(F10_B, F10*(0.0566/100)),        #Composición del buteno
    sym.Eq(F10_M, F10*(0.0034/100)),        #Composición del metano
    sym.Eq(F10_Et, F10*(18.4560/100)),      #Composición  etileno
    sym.Eq(F10, F10_E + F10_H2O + F10_DEE + F10_A + F10_B + F10_CO + F10_CO2 + F10_M + F10_H + F10_Et),
    
    #Corriente 16
    sym.Eq(F16_E, 0.026),   #Caudal de etanol
    sym.Eq(F16_DEE, 0),
    sym.Eq(F16_A, 0),
    sym.Eq(F16_B, 0),
    sym.Eq(F16_H2O, 6591),  #Caudal de agua
    sym.Eq(F16_CO, 0),
    sym.Eq(F16_CO2, 0),
    sym.Eq(F16_M, 0),
    sym.Eq(F16_H, 0),
    sym.Eq(F16_Et, 0),
    
    ]
    
    ecuaciones = balances + especificaciones
    
    #Resolución
    soln = solve(ecuaciones)

    #Outputs
    #fig, ax1 = plt.subplots(figsize=(12,12))
    #img = mpimg.imread('./imagenes/ProcesoGlobal2.png')
    #imgplot = plt.imshow(img)
    #plt.axis('off')
    
    if caso == 'C3':
        fig, ax1 = plt.subplots(figsize=(12,12))
        img = mpimg.imread('./imagenes/Corriente3.png')
        imgplot = plt.imshow(img)
        plt.axis('off')
        txt0 = "La corriente 3\n"
        txt1 = "Etanol: "+str(round(soln[F3_E],4))+" kmol/h\n"
        txt2 = "Dietiléter: "+str(round(soln[F3_DEE],4))+ " kmol/h\n"
        txt3 = "Acetaldehído: "+str(round(soln[F3_A],4))+ " kmol/h\n"
        txt4 = "Buteno: "+str(round(soln[F3_B],4))+ " kmol/h\n"
        txt5 = "Agua: "+str(round(soln[F3_H2O],4))+ " kmol/h\n"
        txt6 = "Monóxido de carbono: "+str(round(soln[F3_CO],4))+ " kmol/h\n"
        txt7 = "Dióxido de carbono: "+str(round(soln[F3_CO2],4))+ " kmol/h\n"
        txt8 = "Metano: "+str(round(soln[F3_M],4))+ " kmol/h\n"
        txt9 = "Hidrógeno: "+str(round(soln[F3_H],4))+ " kmol/h\n"
        txt10 = "Etileno: "+str(round(soln[F3_Et],4))+ " kmol/h\n"
        txt = txt0 + txt1 + txt2 + txt3 + txt4 + txt5 + txt6 + txt7 + txt8 + txt9 + txt10
        plt.text(1000,200,txt, size=14)
        
        
    if caso == 'C4':
        fig, ax1 = plt.subplots(figsize=(12,12))
        img = mpimg.imread('./imagenes/Corriente4.png')
        imgplot = plt.imshow(img)
        plt.axis('off')
        txt0 = "La corriente 4\n"
        txt1 = "Etanol: "+str(round(soln[F4_E],4))+" kmol/h\n"
        txt2 = "Dietiléter: "+str(round(soln[F4_DEE],4))+ " kmol/h\n"
        txt3 = "Acetaldehído: "+str(round(soln[F4_A],4))+ " kmol/h\n"
        txt4 = "Buteno: "+str(round(soln[F4_B],4))+ " kmol/h\n"
        txt5 = "Agua: "+str(round(soln[F4_H2O],4))+ " kmol/h\n"
        txt6 = "Monóxido de carbono: "+str(round(soln[F4_CO],4))+ " kmol/h\n"
        txt7 = "Dióxido de carbono: "+str(round(soln[F4_CO2],4))+ " kmol/h\n"
        txt8 = "Metano: "+str(round(soln[F4_M],4))+ " kmol/h\n"
        txt9 = "Hidrógeno: "+str(round(soln[F4_H],4))+ " kmol/h\n"
        txt10 = "Etileno: "+str(round(soln[F4_Et],4))+ " kmol/h\n"
        txt = txt0 + txt1 + txt2 + txt3 + txt4 + txt5 + txt6 + txt7 + txt8 + txt9 + txt10
        plt.text(1000, 200, txt, size=14)
        
    if  caso == 'C7':
        fig, ax1 = plt.subplots(figsize=(12,12))
        img = mpimg.imread('./imagenes/Corriente7.png')
        imgplot = plt.imshow(img)
        plt.axis('off')
        txt0 = "La corriente 7\n"
        txt1 = "Etanol: "+str(round(soln[F7_E],4))+" kmol/h\n"
        txt2 = "Dietiléter: "+str(round(soln[F7_DEE],4))+ " kmol/h\n"
        txt3 = "Acetaldehído: "+str(round(soln[F7_A],4))+ " kmol/h\n"
        txt4 = "Buteno: "+str(round(soln[F7_B],4))+ " kmol/h\n"
        txt5 = "Agua: "+str(round(soln[F7_H2O],4))+ " kmol/h\n"
        txt6 = "Monóxido de carbono: "+str(round(soln[F7_CO],4))+ " kmol/h\n"
        txt7 = "Dióxido de carbono: "+str(round(soln[F7_CO2],4))+ " kmol/h\n"
        txt8 = "Metano: "+str(round(soln[F7_M],4))+ " kmol/h\n"
        txt9 = "Hidrógeno: "+str(round(soln[F7_H],4))+ " kmol/h\n"
        txt10 = "Etileno: "+str(round(soln[F7_Et],4))+ " kmol/h\n"
        txt = txt0 + txt1 + txt2 + txt3 + txt4 + txt5 + txt6 + txt7 + txt8 + txt9 + txt10
        plt.text(1000,200,txt, size=14)
        
    if caso == 'C10':
        fig, ax1 = plt.subplots(figsize=(12,12))
        img = mpimg.imread('./imagenes/Corriente10.png')
        imgplot = plt.imshow(img)
        plt.axis('off')
        txt0 = "La corriente 10\n"
        txt1 = "Etanol: "+str(round(soln[F10_E],4))+" kmol/h\n"
        txt2 = "Dietiléter: "+str(round(soln[F10_DEE],4))+ " kmol/h\n"
        txt3 = "Acetaldehído: "+str(round(soln[F10_A],4))+ " kmol/h\n"
        txt4 = "Buteno: "+str(round(soln[F10_B],4))+ " kmol/h\n"
        txt5 = "Agua: "+str(round(soln[F10_H2O],4))+ " kmol/h\n"
        txt6 = "Monóxido de carbono: "+str(round(soln[F10_CO],4))+ " kmol/h\n"
        txt7 = "Dióxido de carbono: "+str(round(soln[F10_CO2],4))+ " kmol/h\n"
        txt8 = "Metano: "+str(round(soln[F10_M],4))+ " kmol/h\n"
        txt9 = "Hidrógeno: "+str(round(soln[F10_H],4))+ " kmol/h\n"
        txt10 = "Etileno: "+str(round(soln[F10_Et],4))+ " kmol/h\n"
        txt = txt0 + txt1 + txt2 + txt3 + txt4 + txt5 + txt6 + txt7 + txt8 + txt9 + txt10
        plt.text(1000,200,txt, size=14)
    
    if caso == 'C12':
        fig, ax1 = plt.subplots(figsize=(12,12))
        img = mpimg.imread('./imagenes/Corriente12.png')
        imgplot = plt.imshow(img)
        plt.axis('off')
        txt0 = "La corriente 12\n"
        txt1 = "Etanol: "+str(round(soln[F12_E],4))+" kmol/h\n"
        txt2 = "Dietiléter: "+str(round(soln[F12_DEE],4))+ " kmol/h\n"
        txt3 = "Acetaldehído: "+str(round(soln[F12_A],4))+ " kmol/h\n"
        txt4 = "Buteno: "+str(round(soln[F12_B],4))+ " kmol/h\n"
        txt5 = "Agua: "+str(round(soln[F12_H2O],4))+ " kmol/h\n"
        txt6 = "Monóxido de carbono: "+str(round(soln[F12_CO],4))+ " kmol/h\n"
        txt7 = "Dióxido de carbono: "+str(round(soln[F12_CO2],4))+ " kmol/h\n"
        txt8 = "Metano: "+str(round(soln[F12_M],4))+ " kmol/h\n"
        txt9 = "Hidrógeno: "+str(round(soln[F12_H],4))+ " kmol/h\n"
        txt10 = "Etileno: "+str(round(soln[F12_Et],4))+ " kmol/h\n"
        txt = txt0 + txt1 + txt2 + txt3 + txt4 + txt5 + txt6 + txt7 + txt8 + txt9 + txt10
        plt.text(1000,200,txt, size=14)
     
    if caso == 'C13':
        fig, ax1 = plt.subplots(figsize=(12,12))
        img = mpimg.imread('./imagenes/Corriente13.png')
        imgplot = plt.imshow(img)
        plt.axis('off')
        txt0 = "La corriente 13\n"
        txt1 = "Etanol: "+str(round(soln[F13_E],4))+" kmol/h\n"
        txt2 = "Dietiléter: "+str(round(soln[F13_DEE],4))+ " kmol/h\n"
        txt3 = "Acetaldehído: "+str(round(soln[F13_A],4))+ " kmol/h\n"
        txt4 = "Buteno: "+str(round(soln[F13_B],4))+ " kmol/h\n"
        txt5 = "Agua: "+str(round(soln[F13_H2O],4))+ " kmol/h\n"
        txt6 = "Monóxido de carbono: "+str(round(soln[F13_CO],4))+ " kmol/h\n"
        txt7 = "Dióxido de carbono: "+str(round(soln[F13_CO2],4))+ " kmol/h\n"
        txt8 = "Metano: "+str(round(soln[F13_M],4))+ " kmol/h\n"
        txt9 = "Hidrógeno: "+str(round(soln[F13_H],4))+ " kmol/h\n"
        txt10 = "Etileno: "+str(round(soln[F13_Et],4))+ " kmol/h\n"
        txt = txt0 + txt1 + txt2 + txt3 + txt4 + txt5 + txt6 + txt7 + txt8 + txt9 + txt10
        plt.text(1000,200,txt, size=14)
        
    if caso == 'C15':
        fig, ax1 = plt.subplots(figsize=(12,12))
        img = mpimg.imread('./imagenes/Corriente15.png')
        imgplot = plt.imshow(img)
        plt.axis('off')
        txt0 = "La corriente 15\n"
        txt1 = "Etanol: "+str(round(soln[F15_E],4))+" kmol/h\n"
        txt2 = "Dietiléter: "+str(round(soln[F15_DEE],4))+ " kmol/h\n"
        txt3 = "Acetaldehído: "+str(round(soln[F15_A],4))+ " kmol/h\n"
        txt4 = "Buteno: "+str(round(soln[F15_B],4))+ " kmol/h\n"
        txt5 = "Agua: "+str(round(soln[F15_H2O],4))+ " kmol/h\n"
        txt6 = "Monóxido de carbono: "+str(round(soln[F15_CO],4))+ " kmol/h\n"
        txt7 = "Dióxido de carbono: "+str(round(soln[F15_CO2],4))+ " kmol/h\n"
        txt8 = "Metano: "+str(round(soln[F15_M],4))+ " kmol/h\n"
        txt9 = "Hidrógeno: "+str(round(soln[F15_H],4))+ " kmol/h\n"
        txt10 = "Etileno: "+str(round(soln[F15_Et],4))+ " kmol/h\n"
        txt = txt0 + txt1 + txt2 + txt3 + txt4 + txt5 + txt6 + txt7 + txt8 + txt9 + txt10
        plt.text(1000,200,txt, size=14)
     
    if caso == 'C16':
        fig, ax1 = plt.subplots(figsize=(12,12))
        img = mpimg.imread('./imagenes/Corriente16.png')
        imgplot = plt.imshow(img)
        plt.axis('off')
        txt0 = "La corriente 16\n"
        txt1 = "Etanol: "+str(round(soln[F16_E],4))+" kmol/h\n"
        txt2 = "Dietiléter: "+str(round(soln[F16_DEE],4))+ " kmol/h\n"
        txt3 = "Acetaldehído: "+str(round(soln[F16_A],4))+ " kmol/h\n"
        txt4 = "Buteno: "+str(round(soln[F16_B],4))+ " kmol/h\n"
        txt5 = "Agua: "+str(round(soln[F16_H2O],4))+ " kmol/h\n"
        txt6 = "Monóxido de carbono: "+str(round(soln[F16_CO],4))+ " kmol/h\n"
        txt7 = "Dióxido de carbono: "+str(round(soln[F16_CO2],4))+ " kmol/h\n"
        txt8 = "Metano: "+str(round(soln[F16_M],4))+ " kmol/h\n"
        txt9 = "Hidrógeno: "+str(round(soln[F16_H],4))+ " kmol/h\n"
        txt10 = "Etileno: "+str(round(soln[F16_Et],4))+ " kmol/h\n"
        txt = txt0 + txt1 + txt2 + txt3 + txt4 + txt5 + txt6 + txt7 + txt8 + txt9 + txt10
        plt.text(1000,200,txt, size=14)
        
    if caso == 'grad1':
        fig, ax1 = plt.subplots(figsize=(12,12))
        img = mpimg.imread('./imagenes/Grad1.png')
        imgplot = plt.imshow(img)
        plt.axis('off')
        txt0 = "Los grados de avance del PFR 1 son:\n"
        txt1 = "Reacción 2: "+str(round(soln[xi_21],4))+"\n"
        txt2 = "Reacción 3: "+str(round(soln[xi_31],4))+"\n"
        txt3 = "Reacción 4: "+str(round(soln[xi_41],4))+"\n"
        txt4 = "Reacción 5: "+str(round(soln[xi_51],4))+"\n"
        txt5 = "Reacción 6: "+str(round(soln[xi_61],4))+"\n"
        txt6 = "Reacción 7: "+str(round(soln[xi_71],4))+"\n"
        txt7 = "Reacción 8: "+str(round(soln[xi_81],4))+"\n"
        txt = txt0 + txt1 + txt2 + txt3 + txt4 + txt5 + txt6 + txt7
        plt.text(1000,200,txt, size=14)
        
    if caso == 'grad2':
        fig, ax1 = plt.subplots(figsize=(12,12))
        img = mpimg.imread('./imagenes/Grad2.png')
        imgplot = plt.imshow(img)
        plt.axis('off')
        txt0 = "Los grados de avance del PFR 2 son:\n"
        txt1 = "Reacción 2: "+str(round(soln[xi_22],4))+"\n"
        txt2 = "Reacción 3: "+str(round(soln[xi_32],4))+"\n"
        txt3 = "Reacción 4: "+str(round(soln[xi_42],4))+"\n"
        txt4 = "Reacción 5: "+str(round(soln[xi_52],4))+"\n"
        txt5 = "Reacción 6: "+str(round(soln[xi_62],4))+"\n"
        txt6 = "Reacción 7: "+str(round(soln[xi_72],4))+"\n"
        txt7 = "Reacción 8: "+str(round(soln[xi_82],4))+"\n"
        txt = txt0 + txt1 + txt2 + txt3 + txt4 + txt5 + txt6 + txt7
        plt.text(1000,200,txt, size=14)
        
    if caso == 'grad3':
        fig, ax1 = plt.subplots(figsize=(12,12))
        img = mpimg.imread('./imagenes/Grad3.png')
        imgplot = plt.imshow(img)
        plt.axis('off')
        txt0 = "Los grados de avance del PFR 3 son:\n"
        txt1 = "Reacción 2: "+str(round(soln[xi_23],4))+"\n"
        txt2 = "Reacción 3: "+str(round(soln[xi_33],4))+"\n"
        txt3 = "Reacción 4: "+str(round(soln[xi_43],4))+"\n"
        txt4 = "Reacción 5: "+str(round(soln[xi_53],4))+"\n"
        txt5 = "Reacción 6: "+str(round(soln[xi_63],4))+"\n"
        txt6 = "Reacción 7: "+str(round(soln[xi_73],4))+"\n"
        txt7 = "Reacción 8: "+str(round(soln[xi_83],4))+"\n"
        txt = txt0 + txt1 + txt2 + txt3 + txt4 + txt5 + txt6 + txt7
        plt.text(1000,200,txt, size=14)     
    
    control = 0
    for i in soln:
        if soln[i]<0:
            control = control + 1
    if control > 0:
        txtControl = "De entre todos los valores de todas las corrientes hay " +str(control)+ " valores negativos"
        plt.text(0,280, txtControl, size = 14)
        
def MostrarTabla (b):
    print("La tabla de grados de libertad para el reactor PFR 1 es la siguiente:")
    d = [["Variables de flujo", 12], ["Variables de reacción", 7], ["Ecuaciones de balance", 10],
                  ["Caudales especificados", 1 ], ["Composiciones especificadas", 1 ], ["Relación entre variables", 0 ], ["GdL", 7 ]]
    print(tabulate(d, headers =['Títulos', 'PFR 1'], tablefmt='fancy_grid', stralign='center'))
    
def MostrarTabla2 (b):
    print("La tabla de grados de libertad para los reactores PFR 2 y PFR 3 es la siguiente:")
    d = [["Variables de flujo", 20], ["Variables de reacción", 7], ["Ecuaciones de balance", 10],
                  ["Caudales especificados", 1 ], ["Composiciones especificadas", 9 ], ["Relación entre variables", 0 ], ["GdL", 7 ]]
    print(tabulate(d, headers =['Títulos', 'PFR 2 y 3'], tablefmt='fancy_grid', stralign='center'))
       
def RindoTabla (b):
    run_button.on_click(MostrarTabla)
    display(run_button)
    
def RindoTabla2 (b):    
    run_button2.on_click(MostrarTabla2)
    display(run_button2)

def TgLCompleto (b):
    print("La tabla de grados de libertad para el proceso completo es la siguiente:")
    d = [["Variables de flujo", 74], ["Variables de reacción", 21], ["Ecuaciones de balance", 60],
                  ["Caudales especificados", 1 ], ["Composiciones especificadas", 1 ], ["Relación entre variables", 0 ], ["GdL", 33]]
    print(tabulate(d, headers =['Títulos', 'Proceso'], tablefmt='fancy_grid', stralign='center'))
    
def MostrarEspecificaciones (b):
    F1 = 6600
    
    variables = [
    sym.var('F1_E F1_H2O'),
    sym.var('F3_E F3_DEE F3_A F3_B F3_H2O F3_CO F3_CO2 F3_M F3_H F3_Et'),
    sym.var('F15_E F15_DEE F15_A F15_B F15_H2O F15_CO F15_CO2 F15_M F15_H F15_Et'),
    sym.var('F7 F7_E F7_DEE F7_A F7_B F7_H2O F7_CO F7_CO2 F7_M F7_H F7_Et'),
    sym.var('F10 F10_E F10_DEE F10_A F10_B F10_H2O F10_CO F10_CO2 F10_M F10_H F10_Et'),
    sym.var('F16_E F16_DEE F16_A F16_B F16_H2O F16_CO F16_CO2 F16_M F16_H F16_Et'),
    ]

    especificaciones = [
      
    #Corriente 3
    sym.Eq(F3_E, 476.85),               
    sym.Eq(F3_A, 0.13318300945366),     
    sym.Eq(F3_DEE, 187.003743385105),   
    sym.Eq(F3_CO, 0.03699528040380),    
    sym.Eq(F3_B, 0.14058206553442),     
    sym.Eq(F3_M, 0.04439433648455),     
    sym.Eq(F3_Et, 798.680520000000),    
    
    #Corriente 15
    sym.Eq(F15_E, 109),   
    sym.Eq(F15_DEE, 0.31),
    sym.Eq(F15_A, 0.3),
    sym.Eq(F15_B, 0.005),
    sym.Eq(F15_H2O, 490),
    sym.Eq(F15_CO, 0),
    sym.Eq(F15_CO2, 0.005),
    sym.Eq(F15_M, 0),
    sym.Eq(F15_H, 0),
    sym.Eq(F15_Et, 0.8),
    
    #Corriente 7
    sym.Eq(F7_E, F7*(2.8547/100)),         
    sym.Eq(F7_A, F7*(0.0061/100)),         
    sym.Eq(F7_DEE, F7*(0.5688/100)),       
    sym.Eq(F7_CO, F7*(0.0009/100)),        
    sym.Eq(F7_B, F7*(0.0108/100)),         
    sym.Eq(F7_M, F7*(0.0011/100)),         
    sym.Eq(F7_Et, F7*(16.4157/100)),       
    
    #Corriente 10 
    sym.Eq(F10_E, F10*(1.2669/100)),        
    sym.Eq(F10_A, F10*(0.0068/100)),        
    sym.Eq(F10_DEE, F10*(0.0395/100)),      
    sym.Eq(F10_CO, F10*(0.0025/100)),       
    sym.Eq(F10_B, F10*(0.0566/100)),        
    sym.Eq(F10_M, F10*(0.0034/100)),        
    sym.Eq(F10_Et, F10*(18.4560/100)),      
    
    #Corriente 16
    sym.Eq(F16_E, 0.026),   
    sym.Eq(F16_H2O, 6591),  
    
    ]
    
    for eqn in especificaciones:
        display(eqn)


def TablaGradosLibertad1 (VF = 0, VR = 0, EB = 0, CE = 0, CompE = 0, RV = 0):
    errores = 0
    if VF != 12:
        errores = errores + 1
    if VR != 7:
        errores = errores + 1
    if EB != 10:
        errores = errores + 1
    if CE != 1:
        errores = errores + 1
    if CompE != 1:
        errores = errores + 1
    if RV != 0:
        errores = errores + 1
    if errores == 0:
        print("¡Enhorabuena! ya se puede resolver el balance de materia en el primer reactor!")
    elif errores > 0:
        print("Hay ", errores, "errores, por favor revise los números introducidos")

TgL1 = interactive(TablaGradosLibertad1, {'manual': True}, VF=IntText(value=0, description='Var. flujo'), VR = IntText(value=0, description = 'Var. reac.'), EB=IntText(value=0, description='Ec. balance'), CE=IntText(value=0, description='Caud. espe.'), CompE=IntText(value=0, description='Comp. espe.'), RV=IntText(value=0, description='Relación var.'))

def TablaGradosLibertad2 (VF = 0, VR = 0, EB = 0, CE = 0, CompE = 0, RV = 0):
    errores = 0
    if VF != 20:
        errores = errores + 1
    if VR != 7:
        errores = errores + 1
    if EB != 10:
        errores = errores + 1
    if CE != 1:
        errores = errores + 1
    if CompE != 9:
        errores = errores + 1
    if RV != 0:
        errores = errores + 1
    if errores == 0:
        print("¡Enhorabuena! ya se puede resolver el balance de materia en los dos últimos reactores problema!")
    elif errores > 0:
        print("Hay ", errores, "errores, por favor revise los números introducidos")

TgL2 = interactive(TablaGradosLibertad2, {'manual': True}, VF=IntText(value=0, description='Var. flujo'), VR = IntText(value=0, description = 'Var. reac.'), EB=IntText(value=0, description='Ec. balance'), CE=IntText(value=0, description='Caud. espe.'), CompE=IntText(value=0, description='Comp. espe.'), RV=IntText(value=0, description='Relación var.'))


pfr1 = interactive(PFR1, {'manual': True}, XE = FloatSlider(min = 0.72, max = 1., value = 0.72, step = 0.01, description ='Conversión'), caso = Dropdown(options=['Caudal', 'Porcentaje'], value = 'Caudal', description = 'Output'))
   
pfr2 = interactive(PFR2, {'manual': True}, XE = FloatSlider(min = 0.58, max = 1., value = 0.5802, step = 0.01, description ='Conversión'), caso = Dropdown(options=['Caudal', 'Porcentaje'], value = 'Caudal', description = 'Output'))
       
pfr3 = interactive(PFR3, {'manual': True}, XE = FloatSlider(min = 0.55, max = 1., value = 0.5448, step = 0.01, description = 'Conversión'), caso = Dropdown(options=['Caudal', 'Porcentaje'], value = 'Caudal', description = 'Output'))

ProcesoCompleto = interactive(ProcesoC, {'manual': True}, 
               XE1 = FloatSlider(min = 0., max = 1., value = 0.711, step = 0.01, description = 'X PFR 1'),
               XE2 = FloatSlider(min = 0., max = 1., value = 0.5802, step = 0.01, description = 'X PFR 2'),
               XE3 = FloatSlider(min = 0., max = 1., value = 0.5449, step = 0.01, description = 'X PFR 3'),
               caso = Dropdown(options =['C3', 'C4', 'C7', 'C10', 'C12', 'C13', 'C15', 'C16', 'grad1', 'grad2', 'grad3'], value = 'C3',
                               description = 'Output'))  



   

              
        
        
      
    