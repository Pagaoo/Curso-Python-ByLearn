class Calculadora():
    def Somar(self, num1, num2):
        return num1 + num2

    def Subtrair(self, num1, num2):
        return num1 - num2
    
    def Multiplicar(self, num1, num2):
        return num1 * num2
    
    def Dividir(self, num1, num2):
        return num1 / num2

calc = Calculadora()
teste = calc.Dividir(1,2)
print(teste)