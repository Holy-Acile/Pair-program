import sys
sys.path.append("../../../")
from module.gen_num import gen_num

if __name__ == "__main__":
    mod = 10
    ok = True
    
    for i in range(100) :
        num = gen_num(mod)
        if num >= mod :
            ok = False
            break
    
    if ok :
        print("Finish test!!!")
    else :
        print("Error!!!")