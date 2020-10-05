import sys
sys.path.append("../../../")
from module.check_problem import check_problem

<<<<<<< HEAD
=======
if __name__ == "__main__":
    test = [
        [   [5, "+", 4], [4, "+", 5], ["same"] ],
        [   [5, "+", 4], [5, "+", 5], ["diff"] ],
        [   [1, "×", 2], [2, "×", 1], ["same"] ],
        [   [5, "-", 5], [5, "-", 5], ["same"] ],
        [   [5, "÷", 1], [1, "÷", 5], ["diff"] ],
        [   [1, "+", 2, "-", 3], [2, "+", 1, "-", 3], ["same"] ],
        [   [1, "+", 2, "+", 3], [1, "+", 3, "+", 2], ["diff"] ], 
        [   [1, "+", 2, "+", 3], [3, "+", "(", 1, "+", 2, ")"], ["same"] ],
        [   [1, "+", 2, "+", 3], [3, "+", "(", 2, "+", 1, ")"], ["same"] ],
        [   [1, "+", "(", 2, "×", 3, ")"], [2, "×", 3, "+", 1], ["same"] ],
        []
    ]

    flag = True

    for problem_list in test :
        if len(problem_list) == 0 : break

        vis = {}
        ok = True

        for problem in problem_list :
            if len(problem) == 1 : break
            ok = check_problem(problem, vis)
            if ok == False : break

        if ok :
            if problem_list.pop() != ["diff"] :
                print("Error!!!")
                print(problem_list)
                flag = False
        else :
            if problem_list.pop() != ["same"] :
                print("Error!!!")
                print(problem_list)
                flag = False
    
    if flag :
        print("Finish test!!!")
>>>>>>> 1e8e2168e2714060848fee3f0116c94a18be50fd
