import sys
sys.path.append("../../../")
from module.gen_problem import gen_problem
from fractions import Fraction

if __name__ == "__main__":
    for i in range(100) :
        ok_exp = True
        ok_val = True

        cmp_val = Fraction(0, 1)
        mod = 10

        problem = gen_problem(mod)

        for elem in problem :
            if type(elem) == type(cmp_val) :
                if elem >= mod :
                    ok_val = False
                    break

        exp = ""
        for elem in problem :
            if type(elem) == type(cmp_val) :
                exp += "(" + str(elem) + ")"
            else :
                if elem == "×" : 
                    exp += "*"
                elif elem == "÷" : 
                    exp += "/"
                else :
                    exp += elem
        
        try:
            eval(exp)
        except:
            ok_exp = False
        finally:
            if ok_exp and ok_val :
                pass
            else :
                if ok_exp == False :
                    print("Expression Error!!!")
                    print(exp)
                if ok_val == False :
                    print("Value greater than mod!!!")
                
                break
    
    if ok_exp and ok_val :
        print("Finish Test")
