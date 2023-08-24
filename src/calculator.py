class Calculator():

    def addition(self, a, b):
        return a + b

    def subtraction (self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b
    
    def division(self, a, b):
        return a / b
    



    
    
if __name__=='_main_':
    
    #objeto
    calc = Calculator()
    #=================================
    #teste1
    #oraculo
    print("Test case 1 addition")
    expected_result = 4

    if calc.addition(2,2) == expected_result:
        print("passou")
    else:
        print("falhou")

 #=================================
    #teste2
    #oraculo
    print("Test case 2 subtraction")
    expected_result = 2

    if calc.subtraction(4,2) == expected_result:
        print("passou")
    else:
        print("falhou")

#=================================
    #teste3
    #oraculo
    print("Test case 3 multiplication")
    expected_result = 9

    if calc.subtraction(3,3) == expected_result:
        print("passou")
    else:
        print("falhou")

#=================================
    #teste4
    #oraculo
    print("Test case 4 addition")
    expected_result = 2

    if calc.addition(2,0) == expected_result:
        print("passou")
    else:
        print("falhou")

#=================================
    #teste5
    #oraculo
    print("Test case 5 division")
    expected_result = 2

    if calc.division(2,0) == expected_result:
        print("passou")
    else:
        print("falhou")