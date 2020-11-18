import random
from bokeh.plotting import figure, show

def tirar_dado(numero_de_tiros):    
    suma_de_los_dados = []    
   
    for _ in range(numero_de_tiros):
        dado1 = random.choice([1, 2, 3, 4, 5, 6])
        dado2 = random.choice([1, 2, 3, 4, 5, 6])
        suma_de_los_dados.append(dado1 + dado2)
        
    return suma_de_los_dados

def graficar(probabilidad_suma):   
    plot = figure(title="Probabilidad de lanzamiento de dados")   
    
    for i in range(len(probabilidad_suma)):
        plot.vbar(x = i+2, top = probabilidad_suma[i], width = 0.5, color = "#CAB2D6")
    show(plot)

def main(numero_de_tiros, numero_de_intentos):
    tiros= []           # [[5], [9], [5], [12], [6], [5]]
    
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)
    
    probabilidad_suma_2_a_12 = []
    for i in range(2,13):
        tiros_suma = 0
        for tiro in tiros:
            if i in tiro:
                tiros_suma += 1
        probabilidad_suma_2_a_12.append(tiros_suma / numero_de_intentos)       
    
    print(f'\nCual sera la probabilidad de la suma de los dados con {numero_de_tiros} tiros:')
    for i in range(len(probabilidad_suma_2_a_12)):
        print(f' - La probabidad que sume {i+2} = {round(probabilidad_suma_2_a_12[i], 2)}')

    graficar(probabilidad_suma_2_a_12)

if __name__=='__main__':
    numero_de_tiros = int(input('Cuantas veces se tira el dado: '))
    numero_de_intentos = int(input('Cuantas veces corre el codigo: '))
    
    main(numero_de_tiros, numero_de_intentos)