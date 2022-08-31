import re
def arithmetic_arranger(problems,solve=False):   
    if len(problems) > 4 :
        return "Maximum problems are 4"
    else:
        first = ''
        second  = ""
        lines = ""
        sumxy = ""
        string = ""
        for problem in problems:
            if(re.search("[^\s0-9.+-]",problem)):
                if(re.search("[\]",problem) or re.search("[*]")):
                    return "Operator must be + or -"
                return 'Only digits are accepted'
            splited = problem.split(" ")
            firstN = splited[0]
            operation = splited[1] 
            secondN = splited[2]
            if len(firstN) >= 5 or len(secondN)>= 5:
                return "Numbers can't be more than 4 digits"
            sum ="" 
            if operation == '-':
                sum = str(int(firstN) - int(secondN))
            elif operation == '+':
                sum = str(int(firstN) + int(secondN))
            
            length = max(len(firstN),len(secondN))
            top = str(firstN).rjust(length)
            bottom = operation + str(secondN).rjust(length-1)
            line = ""
            res = str(sum).rjust(length)
            for s in range(length):
                line+='-'
            if problem != problems[-1]:
                first += top + '\t'
                second += bottom +'\t' 
                lines += line+'\t'
                sumxy += res +'\t'
            else:
                first += top
                second += bottom
                lines += line
                sumxy += res
        if solve:
            string = first + '\n' + second +'\n' + lines + '\n' + sum
        else: 
            string = first + '\n' + second + lines

        return string

print(arithmetic_arranger(["349 + 230","329 - 3914",'3209 - 1289','13 + 1283'],solve=True))