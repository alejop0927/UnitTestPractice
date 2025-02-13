class Tarjeta_credito:
    def __init__(self,P,I,N):
        self.P=P
        self.I=I
        self.N=N
        self.C=self.cuota()
    #cuota mensual
    def cuota(self):
        return (self.P*self.I)/(1-((1+self.I)**-self.N))
    #cuota de interes 
    def interes(self):
        return (self.C*self.N)-self.P

    def imprimir(self):
        Ti=self.interes()
        print(f'El monto es: {self.P}\n'
              f'La tasa es: {self.I}\n'
              f'La cuota es: {self.C:.2f}\n'
              f'El total de interés es: {Ti:.2f}\n')

Caso1=Tarjeta_credito(200000,0.031,36)
Caso1.imprimir()

caso2=Tarjeta_credito(850000,0.034,24)
caso2.imprimir()

#Caso3=Tarjeta_credito(480000,0,48)
#Caso3.imprimir()

Caso4=Tarjeta_credito(50000,0.125,60)
Caso4.imprimir()

