# Finalização da calculadora com try/except
class Calculadora():
    def Somar(self, num1, num2):
        return num1 + num2

    def Subtrair(self, num1, num2):
        return num1 - num2
    
    def Multiplicar(self, num1, num2):
        return num1 * num2
    
    def Dividir(self, num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            print('Não há como dividir por zero')

calc = Calculadora()
teste = calc.Dividir(1,0)
print(teste)