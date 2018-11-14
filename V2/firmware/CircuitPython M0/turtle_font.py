from turtle import *

# Try running this file from Python on a computer (it is too big to run on Turtle Robot).
# Use only the fuctions for the letters you need in 'turtle_font_example.py'.

scale = 100

def setScale(value):
    global scale
    scale = value


def A():
    penup()
    left(90)
    pendown()
    forward(3 * scale)
    right(45)
    forward(1.41 * scale)
    right(90)
    forward(1.41 * scale)
    right(45)
    forward(2 * scale)
    right(90)
    forward(2 * scale)
    backward(2 * scale)
    left(90)
    forward(1 * scale)
    penup()
    left(90)
    forward(0.5 * scale)


def B():
    pendown()
    forward(1 * scale)
    left(45)
    forward(1.41 * scale)
    left(90)
    forward(1.41 * scale)
    right(90)
    forward(1.41 * scale)
    left(90)
    forward(1.41 * scale)
    left(45)
    forward(1 * scale)
    left(90)
    forward(4 * scale)
    penup()
    left(90)
    forward(2.5 * scale)        


def C():
    penup()
    left(90 - 33.7)
    forward(3.61 * scale)
    pendown()
    left(78.7)
    forward(1.41 * scale)
    left(90)
    forward(1.41 * scale)
    left(45)
    forward(2 * scale)
    left(45)
    forward(1.41 * scale)
    left(90)
    forward(1.41 * scale)
    penup()
    right(90)
    forward(1.41 * scale)
    left(45)
    backward(0.5 * scale)


def D():
    pendown()
    forward(1 * scale)
    left(45)
    forward(1.41 * scale)
    left(45)
    forward(2 * scale)
    left(45)
    forward(1.41 * scale)
    left(45)
    forward(1 * scale)
    left(90)
    forward(4 * scale)
    penup()
    left(90)
    forward(2.5 * scale)


def E():
    penup()
    left(90)
    forward(4 * scale)
    right(90)
    forward(2 * scale)
    pendown()
    backward(2 * scale)
    right(90)
    forward(2 * scale)
    left(90)
    forward(1 * scale)
    penup()
    backward(1 * scale)
    right(90)
    pendown()
    forward(2 * scale)
    left(90)
    forward(2 * scale)
    penup()
    forward(0.5 * scale)



def F():
    penup()
    left(90)
    pendown()
    forward(4 * scale)
    right(90)
    forward(2 * scale)
    penup()
    backward(2 * scale)
    right(90)
    forward(2 * scale)
    left(90)
    pendown()
    forward(2 * scale)
    penup()
    right(90)
    forward(2* scale)
    left(90)
    forward(0.5* scale)


def G():
    penup()
    left(56.3)#left(90 - 33.7) #63.4
    forward(3.61 * scale)
    pendown()
    left(90-56.3+45)#left(78.7)
    forward(1.41 * scale)
    right(90)
    backward(1.41 * scale)
    left(45)
    backward(2 * scale)
    left(45)
    backward(1.41 * scale)
    right(90)
    forward(1.41 * scale)
    left(45)
    forward(1 * scale)
    right(90)
    backward(1 * scale)
    penup()
    right(45)
    forward(2.82 * scale)
    left(45)
    backward(0.5 * scale)
    

def H():
    penup()
    left(90)
    pendown()
    forward(4 * scale)
    penup()
    backward(2 * scale)
    right(90)
    pendown()
    forward(2 * scale)
    penup()
    left(90)
    forward(2 * scale)
    pendown()
    backward(4 * scale)
    penup()
    right(90)
    forward(0.5 * scale)


def I():
    penup()
    left(90 - 7.13)
    forward(4.03 * scale)
    left(7.13)
    pendown()
    backward(4 * scale)
    penup()
    right(90)
    forward(1 * scale)


def J():
    penup()
    left(90)
    forward(1 * scale)
    pendown()
    backward(1 * scale)
    left(90)
    backward(2 * scale)
    left(90)
    backward(4 * scale)
    penup()
    left(14)
    forward(4.12 * scale)
    left(90 - 14)
    backward(0.5 * scale)


def K():
    penup()
    left(90)
    pendown()
    forward(4 * scale)
    backward(2 * scale)
    penup()
    right(45)
    forward(2.83 * scale)
    pendown()
    backward(2.83 * scale)
    right(90)
    forward(2.83 * scale)
    penup()
    left(45)
    forward(0.5 * scale)


def L():
    penup()
    left(90)
    forward(4 * scale)
    pendown()
    backward(4 * scale)
    right(90)
    forward(2 * scale)
    penup()
    forward(0.5 * scale)


def M():
    penup()
    left(90)
    pendown()
    forward(4 * scale)
    left(26.6)
    backward(2.24 * scale)
    right(26.6 + 26.6)
    forward(2.24 * scale)
    left(26.6)
    backward(4 * scale)
    penup()
    right(90)
    forward(0.5 * scale)


def N():
    penup()
    left(90)
    pendown()
    forward(4 * scale)
    left(26.6)
    backward(4.47 * scale)
    right(26.6)
    forward(4 * scale)
    penup()
    backward(4 * scale)
    right(90)
    forward(0.5 * scale)


def O():
    penup()
    forward(1 * scale)
    left(45)
    pendown()
    forward(1.41 * scale)
    left(45)
    forward(2 * scale)
    left(45)
    forward(1.41 * scale)
    right(90)
    backward(1.41 * scale)
    left(45)
    backward(2 * scale)
    left(45)
    backward(1.41 * scale)    
    penup()
    right(90+45)
    forward(1.5 * scale)


def P():
    penup()
    right(90)
    pendown()
    backward(4 * scale)
    right(90)
    backward(1 * scale)
    right(45)
    backward(1.41 * scale)
    right(90)
    backward(1.41 * scale)
    right(45)
    backward(1 * scale)
    penup()
    right(33.7)
    forward(3.61 * scale)
    left(33.7)
    backward(0.5 * scale)


def Q():
    penup()
    forward(1 * scale)
    left(45)
    pendown()
    forward(1.41 * scale)
    left(45)
    forward(2 * scale)
    left(45)
    forward(1.41 * scale)
    left(90)
    forward(1.41 * scale)
    left(45)
    forward(2 * scale)
    left(45)
    forward(1.41 * scale)    
    penup()
    left(45)
    forward(1 * scale)
    right(45)
    pendown()
    backward(1.41 * scale)
    penup()
    forward(1.41 * scale)
    left(45)
    forward(0.5 * scale)


def R():
    penup()
    left(90)
    pendown()
    forward(4 * scale)
    right(90)
    forward(1 * scale)
    right(45)
    forward(1.41 * scale)
    left(90)
    backward(1.41 * scale)
    right(45)
    backward(1 * scale)
    right(45)
    forward(2.83 * scale)
    penup()
    left(45)
    forward(0.5 * scale)


def S():
    pendown()
    forward(1 * scale)
    left(45)
    forward(1.41 * scale)
    right(90)
    backward(2.83 * scale)
    left(90)
    forward(1.41 * scale)
    right(45)
    forward(1 * scale)
    penup()
    right(76)
    forward(4.123 * scale)
    left(76)
    backward(0.5 * scale)


def T():
    penup()
    forward(1 * scale)
    left(90)
    pendown()
    forward(4 * scale)
    penup()
    right(90)
    backward(1 * scale)
    pendown()
    forward(2 * scale)
    penup()
    right(76)
    forward(4.123 * scale)
    left(76)
    backward(0.5 * scale)


def U():
    penup()
    left(90)
    forward(4 * scale)
    pendown()
    backward(4 * scale)
    left(90)
    backward(2 * scale)
    left(90)
    backward(4 * scale)
    penup()
    left(14)
    forward(4.123 * scale)
    left(76)
    backward(0.5 * scale)


def V():
    penup()
    left(90)
    forward(4 * scale)
    pendown()
    backward(3 * scale)
    left(45)
    backward(1.41 * scale)
    left(90)
    backward(1.41 * scale)
    left(45)
    backward(3 * scale)
    penup()
    left(14)
    forward(4.123 * scale)
    left(76)
    backward(0.5 * scale)


def W():
    penup()
    right(90)
    backward(4 * scale)
    pendown()
    forward(4.123 * scale)
    right(26.6)
    backward(2.24 * scale)
    left(26.6 + 26.6)
    forward(2.24 * scale)
    right(26.6)
    backward(4 * scale)
    penup()
    left(14)
    forward(4.123 * scale)
    left(76)
    backward(0.5 * scale)


def X():
    penup()
    left(90 - 26.6)
    pendown()
    forward(4.47 * scale)
    penup()
    right(90 - 26.6)
    backward(2 * scale)
    right(90 - 26.6)
    pendown()
    forward(4.47 * scale)
    penup()
    left(90 - 26.6)
    forward(0.5 * scale)


def Y():
    penup()
    right(90)
    backward(4 * scale)
    left(27)
    pendown()
    forward(2.24 * scale)
    right(27 + 27)
    backward(2.24 * scale)
    forward(2.24 * scale)
    left(27)
    forward(2 * scale)
    penup()
    left(90)
    forward(1.5 * scale)


def Z():
    penup()
    left(90)
    forward(4 * scale)
    right(90)
    pendown()
    forward(2 * scale)
    left(90 - 26.6)
    backward(4.47 * scale)
    right(90 - 26.6)
    forward(2 * scale)
    penup()
    forward(0.5 * scale)


def spc():
    # Create a space equal to one character. #
    penup()
    forward(2.5 * scale)


def N0():
    #Numeral zero#
    pendown()
    forward(2 * scale)
    left(90)
    forward(4 * scale)
    left(90)
    forward(2 * scale)
    left(90)
    forward(4 * scale)
    penup()
    left(90)
    forward(2.5 * scale)


def N1():
    #Numeral 1#
    penup()
    left(90 - 14)
    forward(4.123 * scale)
    left(14)
    pendown()
    backward(4 * scale)
    penup()
    right(90)
    forward(1.5 * scale)


def N2():
    #Numeral 2#
    penup()
    left(90)
    forward(4 * scale)
    right(90)
    pendown()
    forward(2 * scale)
    right(90)
    forward(2 * scale)             
    right(90)
    forward(2 * scale)
    left(90)
    forward(2 * scale)                 
    left(90)
    forward(2 * scale)
    penup()
    forward(0.5 * scale)


def N3():
    #Numeral 3#
    penup()
    left(90)
    forward(4 * scale)
    right(90)
    pendown()
    forward(2 * scale)
    right(90)
    forward(2 * scale)
    right(90)
    forward(2 * scale)
    backward(2 * scale)
    left(90)
    forward(2 * scale)
    left(90)
    backward(2 * scale)
    penup()
    forward(2.5 * scale)

    
def N4():
    #Numeral 4#
    penup()
    left(90)
    forward(4 * scale)
    pendown()
    backward(2 * scale)
    right(90)
    forward(2 * scale)
    left(90)
    forward(2 * scale)
    backward(4 * scale)
    penup()
    right(90)
    forward(0.5 * scale)


def N5():
    #Numeral 5#
    pendown()
    forward(2 * scale)                
    left(90)                                        
    forward(2 * scale)     
    left(90)    
    forward(2 * scale)     
    right(90)
    forward(2 * scale)     
    right(90)
    forward(2 * scale)
    penup()
    right(76)
    forward(4.123 * scale)
    left(76)
    backward(0.5 * scale)


def N6():
    #Numeral 6#
    penup()
    left(90)
    forward(4 * scale)
    pendown()
    backward(4 * scale)
    right(90)
    forward(2 * scale)
    right(90)                
    backward(2 * scale)
    left(90)
    backward(2 * scale)
    penup()
    right(38.66)
    forward(3.20 * scale)
    left(38.66)


def N7():
    #Numeral 7#
    penup()
    left(90)
    forward(4 * scale)
    right(90)
    pendown()
    forward(2 * scale)
    left(90 - 26.6)
    backward(4.47 * scale)
    penup()
    right(90 - 26.6)
    forward(2.5 * scale)


def N8():
    #Numeral 8#
    pendown()
    forward(2 * scale)                
    left(90)
    forward(4 * scale)                
    left(90)
    forward(2 * scale) 
    left(90)
    forward(2 * scale)
    left(90)
    forward(2 * scale)                
    backward(2 * scale)
    right(90)
    forward(2 * scale)
    penup()
    left(90)
    forward(2.5 * scale)


def N9():
    #Numeral 9#
    penup()
    forward(2 * scale)                
    left(90)
    pendown()
    forward(4 * scale)                
    left(90)
    forward(2 * scale) 
    left(90)
    forward(2 * scale)
    left(90)
    forward(2 * scale)
    penup()
    right(75.96)
    forward(2.06* scale)
    left(75.96)


def period():
    #Period#
    penup()
    forward(0.5 * scale)
    pendown()
    for x in range(4):
        forward(0.5 * scale)
        left(90)
    
    penup()
    forward(1.0 * scale)


def comma():
    #Comma#
    penup()
    forward(0.5 * scale)
    left(45)
    pendown()
    forward(0.707 * scale)
    left(90 - 45)
    forward(0.5 * scale)
    right(90)
    backward(0.5 * scale)
    left(90)
    backward(0.5 * scale)
    right(90)
    forward(0.5 * scale)
    penup()
    right(26.56)
    forward(1.12 * scale)
    left(26.56)


def qm():
    #Question mark#
    penup()
    forward(1 * scale)             
    pendown()             
    for x in range(4):
        forward(0.5 * scale)
        left(90)
    
    penup()
    left(90 - 14.03)
    forward(1.03 * scale)
    left(14.03)
    pendown()
    forward(1 * scale)
    right(90)                
    forward(1 * scale)
    left(90) 
    forward(2 * scale)
    left(90) 
    forward(2 * scale)
    left(90) 
    forward(0.5 * scale)
    penup()
    left(35.54)
    forward(4.30 * scale)
    left(90 - 35.54)


def apost():
    #Apostrophe#
    penup()
    left(90 - 18.43)
    forward(3.16 * scale)
    right(90 - 18.43 - 45)
    pendown()
    forward(0.707 * scale)
    left(45)
    forward(0.5 * scale)
    left(90)
    forward(0.5 * scale)
    left(90)
    forward(0.5 * scale)
    left(90)
    forward(0.5 * scale)
    penup()
    right(90 - 15.95)
    forward(3.64 * scale)
    left(90 - 15.95)


def cq():
    #Close quote#
    penup()
    left(90 - 9.46)
    forward(3.04 * scale)
    right(90 - 9.46 - 45)
    pendown()
    forward(0.707 * scale)
    left(45)
    forward(0.5 * scale)
    left(90)
    forward(0.5 * scale)
    left(90)
    forward(0.5 * scale)
    left(90)
    forward(0.5 * scale)
    penup()
    right(45)
    forward(0.707 * scale)
    left(90)
    pendown()
    forward(0.707 * scale)
    left(45)
    forward(0.5 * scale)
    left(90)
    forward(0.5 * scale)
    left(90)
    forward(0.5 * scale)
    left(90)
    forward(0.5 * scale)
    penup()
    right(90 - 15.95)
    forward(3.64 * scale)
    left(90 - 15.95)


def oq():
    #Open quote#
    penup()
    left(90 - 18.43)
    forward(3.16 * scale)
    left(18.43 + 45)
    pendown()
    forward(0.707 * scale)
    right(45)                
    forward(0.5 * scale)
    right(90)
    forward(0.5 * scale)
    right(90)
    forward(0.5 * scale)
    left(90)
    backward(0.5 * scale)
    penup()
    right(18.43)
    forward(1.58 * scale)
    right(45 - 18.43)
    pendown()
    backward(0.707 * scale)
    left(45)
    forward(0.5 * scale)
    left(90)
    forward(0.5 * scale)
    left(90)
    forward(0.5 * scale)
    left(90)
    forward(0.5 * scale)
    penup()

    left(23.20)
    forward(3.81 * scale)
    left(90 - 23.20)


def ex():
    # Exclamation point #
    penup()
    forward(0.5 * scale)             
    pendown()             
    for x in range(4):
        forward(0.5 * scale)
        left(90)
    
    penup()
    left(63.45)
    forward(1.12 * scale)
    left(90 - 63.45)
    pendown()
    forward(3 * scale)
    left(90)
    forward(0.5 * scale)
    left(90)
    forward(3 * scale)
    left(90)
    forward(0.5 * scale)
    penup()
    right(45)
    forward(1.41 * scale)
    left(45)



def coolS1() : 
    pendown()
    forward(1* scale)
    left(45)
    forward(1.41* scale)
    right(45)
    forward(1* scale)
    right(45)
    forward(1.41* scale)
    right(90) # top
    forward(1.41* scale)
    right(45)
    forward(1* scale)
    right(45)
    forward((1.41* scale) / 2)

    penup()
    right(90)
    forward((1.41* scale)/2)
    right(45)
    forward(1* scale)
    right(180)
    pendown()
    forward(1* scale)
    left(45)
    forward(1.41* scale)
    right(45)
    forward(1* scale)
    right(45)
    forward(1.41* scale)
    right(90) # bottom
    forward(1.41* scale)
    right(45)
    forward(1* scale)
    right(45)
    forward((1.41* scale)/2)
    
    penup()
    forward(150)


def superS():# https:#en.wikipedia.org/wiki/Cool_S
    backward(1.5 * scale)
    pendown()
    forward(1* scale)
    left(45)
    forward(1.41* scale)
    right(45)
    forward(1* scale)
    right(45)
    forward(1.41* scale)
    left(90) # top

    backward(1.41* scale)
    right(45)

    backward(1* scale)
    right(45)
    backward((1.41* scale) / 2)
    penup()
    
    left(90)
    forward((1.41* scale)/2)
    right(45)
    forward(1* scale)
    pendown()
    backward(1* scale)
    left(45)
    backward(1.41* scale)
    right(45)
    backward(1* scale)
    right(45)
    backward(1.41 * scale)
    left(90)
    forward(1.41 * scale)
    right(45)
    forward(1 * scale)
    right(45)
    forward(1.41 * scale / 2)
    penup()
    backward(75)


if __name__ == '__main__':
    setScale(25)
    speed(0)
    penup()
    backward(425)
    right(90)
    backward(275)
    left(90)
    A()
    B()
    C()
    D()
    E()
    F()
    F()
    G()
    H()
    I()
    J()
    K()
    L()
    M()
    left(90)
    backward(6 * scale)
    right(90)
    backward(33 * scale)
    N()
    O()
    P()
    Q()
    R()
    S()
    T()
    U()
    V()
    W()
    X()
    Y()
    Z()
    left(90)
    backward(6 * scale)
    right(90)
    backward(33 * scale)
    N0()
    N1()
    N2()
    N3()
    N4()
    N5()
    N6()
    N7()
    N8()
    N9()
    left(90)
    backward(6 * scale)
    right(90)
    backward(25 * scale)
    period()
    comma()
    apost()
    qm()
    oq()
    cq()
    ex()
    forward(50)
    left(90)
    forward(50)
    superS()

    done()
