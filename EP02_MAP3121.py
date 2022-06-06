########################################################
###                                                  ###
###  MAP3121 - Métodos Numéricos e Aplicações (2022) ###
###  Exercicio-Programa 2                            ###
###                                                  ###
###  Bruno Kenzo Minniti Yoshioka - 11805335         ###
###  Pedro Gomes Santana de Souza - 11806211         ###
###                                                  ###
###  Turma: 02                                       ###
###  Professor: Renato Vicente                       ###
###                                                  ###
########################################################

#Importações de bibliotecas

from math import e, pi, sqrt
import numpy as np

#Inicialização dos valores dados para n e w para 6, 8 e 10
#6
n_6 = np.array([-0.9324695142031520278123016, -0.6612093864662645136613996, -0.2386191860831969086305017,
               0.2386191860831969086305017, 0.6612093864662645136613996, 0.9324695142031520278123016])
w_6 = np.array([0.1713244923791703450402961, 0.3607615730481386075698335, 0.4679139345726910473898703,
               0.4679139345726910473898703, 0.3607615730481386075698335, 0.1713244923791703450402961])
#8
n_8 = np.array([-0.9602898564975362316835609, -0.7966664774136267395915539, -0.5255324099163289858177390, -0.1834346424956498049394761,
               0.1834346424956498049394761, 0.5255324099163289858177390, 0.7966664774136267395915539, 0.9602898564975362316835609])
w_8 = np.array([0.1012285362903762591525314, 0.2223810344533744705443560, 0.3137066458778872873379622, 0.3626837833783619829651504,
               0.3626837833783619829651504, 0.3137066458778872873379622, 0.2223810344533744705443560, 0.1012285362903762591525314])
#10
n_10 = np.array([-0.9739065285171717200779640, -0.8650633666889845107320967, -0.6794095682990244062343274, -0.4333953941292471907992659, -0.1488743389816312108848260,
                0.1488743389816312108848260, 0.4333953941292471907992659, 0.6794095682990244062343274, 0.8650633666889845107320967, 0.9739065285171717200779640])
w_10 = np.array([0.0666713443086881375935688, 0.1494513491505805931457763, 0.2190863625159820439955349, 0.2692667193099963550912269, 0.2955242247147528701738930,
                0.2955242247147528701738930, 0.2692667193099963550912269, 0.2190863625159820439955349, 0.1494513491505805931457763, 0.0666713443086881375935688])

#Função para o calculo do valor das integrais duplas
def calculoIntegralDupla(a, b, n, w, c, d, f):
    h1 = (b-a)/2
    h2 = (b+a)/2
    soma = 0

    i = 0

    while(i < len(n)):
        somaParcial = 0
        r1 = n[i]
        w1 = w[i]
        x = h1*r1 + h2
        d1 = d(x)
        c1 = c(x)
        k1 = (d1 - c1)/2
        k2 = (d1 + c1)/2

        j = 0
        while(j < len(n)):
            r2 = n[j]
            w2 = w[j]
            y = k1*r2 + k2
            Q = f(x, y)
            somaParcial = somaParcial + w2*Q
            j += 1

        soma = soma + w1*k1*somaParcial
        i += 1
    soma = h1*soma
    return(soma)

#Função auxiliar para retornar 1-x^2
def parabolax(x):
    return 1 - x**2
#Função auxiliar para retornar sqrt(1-y)
def parabolay(y):
    return (1 - y)**0.5
#Função auxiliar para retornar sqrt(1-x^2)
def raizparabola(x):
    return sqrt(parabolax(x))
#Função auxiliar para retornar 0
def zero(x, y=None):
    return 0
#Função auxiliar para retornar 1
def um(x, y=None):
    return 1
#Função auxiliar para retornar 0.75
def zeroSeteCinco(x, y=None):
    return 0.75
#Função auxiliar para retornar x
def xlinear(x, y=None):
    return x
#Função auxiliar para retornar y
def ylinear(x, y):
    return y
#Função auxiliar para retornar 1-x
def yTetraedro(x):
    return -1*x + 1
#Função auxiliar para retornar 1-x-y
def zTetraedro(x, y):
    return 1 - x - y
#Função auxiliar para retornar x^3
def y0Exp(x):
    return x**3
#Função auxiliar para retornar x^2
def y1Exp(x):
    return x**2
#Função auxiliar para retornar e^(y/x)
def zExp(x, y):
    return e**(y/x)
#Função auxiliar para retornar sqrt(((e^(y/x))/x)^2 + ((y*e^(y/x))/(x^2))^2 + 1)
def zExpArea(x, y):
    return ((e**(y/x) / x)**2 + (y*e**(y/x) / x**2)**2 + 1)**0.5
#Função auxiliar para retornar e^(-x^2)
def expoVarQuadrado(x):
    return (e**(-1*x**2))

#Função principal
def main():
    print('\nOlá! O que gostaria de fazer?')
    rodando = True
    mode = 0

    while (rodando == True): 
        print('Selecione um dos modos de operação:\n')
        print('1) Cálculo dos volumes do cubo cujas arestas tem comprimento 1 e do tetraedro com vértices (0, 0, 0), (1, 0, 0), (0, 1, 0) e (0, 0, 1)')
        print('2) Cálculo da área A da região no primeiro quadrante limitada pelos eixos e pela curva y = 1 - x^2')
        print('3) Cálculo da área e volume abaixo da superfície descrita por z = e^(x/y), 0.1 <= x <= 0.5, x^3 <= y <= x^2 ')
        print('4) Cálculo do volume da calota esférica de altura 1/4 da esfera de raio 1 e o do sólido obtido da rotação da região, em torno do eixo y, delimitada por x = 0, x = e^(-y^2), y = -1 e y = 1')
        print('5) Finalizar o programa')
        mode = int(input('\nDigite o numero do modo de operação desejado: '))

        if (mode == 1):
            print('Opção selecionada:')
            print('1) Cálculo dos volumes do cubo cujas arestas tem comprimento 1 e do tetraedro com vértices (0, 0, 0), (1, 0, 0), (0, 1, 0) e (0, 0, 1)\n')
           
            print('Valores para n=6')
            print('Volume do Cubo: ',calculoIntegralDupla(0, 1, n_6, w_6, zero, um, um))
            print('Volume do Tetraedro',calculoIntegralDupla(0, 1, n_6, w_6, zero, yTetraedro, zTetraedro),'\n')

            print('Valores para n=8')
            print('Volume do Cubo: ',calculoIntegralDupla(0, 1, n_8, w_8, zero, um, um))
            print('Volume do Tetraedro',calculoIntegralDupla(0, 1, n_8, w_8, zero, yTetraedro, zTetraedro),'\n')

            print('Valores para n=10')
            print('Volume do Cubo: ',calculoIntegralDupla(0, 1, n_10, w_10, zero, um, um))
            print('Volume do Tetraedro',calculoIntegralDupla(0, 1, n_10, w_10, zero, yTetraedro, zTetraedro),'\n\n')
        
        elif (mode == 2):
            print('Opção selecionada:')
            print('2) Cálculo da área A da região no primeiro quadrante limitada pelos eixos e pela curva y = 1 - x^2')
          
            print('Valores para n=6')
            print('Área da região (cálculo com a primeira integral): ',calculoIntegralDupla(0, 1, n_6, w_6, zero, parabolax, um))
            print('Área da região (cálculo com a segunda integral): ',calculoIntegralDupla(0, 1, n_6, w_6, zero, parabolay, um),'\n')

            print('Valores para n=8')
            print('Área da região (cálculo com a primeira integral): ',calculoIntegralDupla(0, 1, n_8, w_8, zero, parabolax, um))
            print('Área da região (cálculo com a segunda integral): ',calculoIntegralDupla(0, 1, n_8, w_8, zero, parabolay, um),'\n')

            print('Valores para n=10')
            print('Área da região (cálculo com a primeira integral): ',calculoIntegralDupla(0, 1, n_10, w_10, zero, parabolax, um))
            print('Área da região (cálculo com a segunda integral): ',calculoIntegralDupla(0, 1, n_10, w_10, zero, parabolay, um),'\n\n')
        
        elif (mode == 3):
            print('Opção selecionada:')
            print('3) Cálculo da área e volume abaixo da superfície descrita por z = e^(x/y), 0.1 <= x <= 0.5, x^3 <= y <= x^2 ')
            
            print('Valores para n=6')
            print('Volume calculado: ',calculoIntegralDupla(0.1, 0.5, n_6, w_6, y0Exp, y1Exp, zExp))
            print('Área calculada: ',calculoIntegralDupla(0.1, 0.5, n_6, w_6, y0Exp, y1Exp, zExpArea),'\n')

            print('Valores para n=8')
            print('Volume calculado: ',calculoIntegralDupla(0.1, 0.5, n_8, w_8, y0Exp, y1Exp, zExp))
            print('Área calculada: ',calculoIntegralDupla(0.1, 0.5, n_8, w_8, y0Exp, y1Exp, zExpArea),'\n')

            print('Valores para n=10')
            print('Volume calculado: ',calculoIntegralDupla(0.1, 0.5, n_10, w_10, y0Exp, y1Exp, zExp))
            print('Área calculada: ',calculoIntegralDupla(0.1, 0.5, n_10, w_10, y0Exp, y1Exp, zExpArea),'\n\n')
            
        
        elif (mode == 4):
            print('Opção selecionada:')
            print('4) Cálculo do volume da calota esférica de altura 1/4 da esfera de raio 1 e o do sólido obtido da rotação da região, em torno do eixo y, delimitada por x = 0, x = e^(-y^2), y = -1 e y = 1')            
            print('Valores para n=6')
            print('Volume da Calota: ',2*pi*calculoIntegralDupla(0, sqrt(7)/4, n_6, w_6, zeroSeteCinco, raizparabola, xlinear))
            print('Volume do Sólido: ',2*pi*calculoIntegralDupla(-1, 1, n_6, w_6, zero, expoVarQuadrado, ylinear),'\n')

            print('Valores para n=8')
            print('Volume da Calota: ',2*pi*calculoIntegralDupla(0, sqrt(7)/4, n_8, w_8, zeroSeteCinco, raizparabola, xlinear))
            print('Volume do Sólido: ',2*pi*calculoIntegralDupla(-1, 1, n_8, w_8, zero, expoVarQuadrado, ylinear),'\n')

            print('Valores para n=10')
            print('Volume da Calota: ',2*pi*calculoIntegralDupla(0, sqrt(7)/4, n_10, w_10, zeroSeteCinco, raizparabola, xlinear))
            print('Volume do Sólido: ',2*pi*calculoIntegralDupla(-1, 1, n_10, w_10, zero, expoVarQuadrado, ylinear),'\n\n')

            
        
        elif (mode == 5):
            print('Opção selecionada:')
            print('5) Finalizar o programa')
            
            print("Programa finalizado.", "\n")
            rodando = False
        
        else:
            print('Modo de operação inválido!')

main() #god god