import math

class Complex_numb():

    def __init__(self, real, im):
        self.real = real
        self.im = im

    def get_real(self):
        return self.real

    def get_im(self):
        return self.im

    def add(self, n):
        return Complex_numb(self.real + n.real, self.im + n.im)

    def differ(self, n):
        return Complex_numb(self.real - n.real, self.im - n.im)
    
    def conj(self):
        self.im = -self.im

 
while 1:
    print("Wybierz operacje:\n1.Dodawanie\n2.Odejmowanie\n3.Sprzężenie")
    task = input(": ")

    if task == '1':
        a, b = input("Podaj 1 liczbe w formacie\nreal im:\n").split(" ")
        a2, b2 = input("Podaj 2 liczbe w formacie\nreal im:\n").split(" ")
        x1 = Complex_numb(float(a),float(b))
        x2 = Complex_numb(float(a2),float(b2))
        print("wynik: ", x1.add(x2),"\n")
    elif task == '2':
        a, b = input("Podaj 1 liczbe w formacie\nreal im:\n").split(" ")
        a2, b2 = input("Podaj 2 liczbe w formacie\nreal im:\n").split(" ")
        x1 = Complex_numb(float(a),float(b))
        x2 = Complex_numb(float(a2),float(b2))
        print("wynik: ", x1.differ(x2),"\n")
    elif task == '3':
        a, b = input("Podaj 1 liczbe w formacie\nreal im:\n").split(" ")
        x1 = Complex_numb(float(a),float(b))
        x1.conj()
        print("wynik: ",x1.get_real(),x1.get_im() ,"\n")
    else:
        print("Wybierz ponownie\n")