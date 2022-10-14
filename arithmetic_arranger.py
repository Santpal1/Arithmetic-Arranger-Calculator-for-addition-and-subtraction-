def arithmetic_arranger(x, b = False):
    if len(x) > 5:
        print("Error: Too many problems.")
    else:
        for a in range(len(x)):
            l = x[a]
            dig = 0
            m = False
            for q in l:
                if q.lower() in 'qwertyuiopasdfghjklzxcvbnm`~!@#$%^&*()_=[{]}\|;:,<.>/?':
                    m = True
            if m:
                print("Error: Numbers must only contain digits.")
                continue
            for i in l:
                if i.isdigit():
                    num = dig *10 + int(i)
                    dig = num
                else:
                    break
            y = len(str(num))
            if y > 4:
                print("Error: Numbers cannot be more than four digits.")
                continue
            if l[y + 1] not in ['+','-']:
                print("Error: Operator must be '+' or '-'.")
                continue
            if len(str(num)) == 1:
                num = ' '+' '+' '+' '+str(num)
            elif len(str(num)) == 2:
                num = ' '+' '+' '+str(num)
            elif len(str(num)) == 3:
                num = ' '+' '+str(num)
            elif len(str(num)) == 4:
                num = ' '+str(num)
            print(num)
            print(l[y + 1],end='')
            digit = 0
            for j in l[y + 1: ]:
                if j.isdigit():
                    number = digit *10 + int(j)
                    digit = number
            if len(str(number)) == 1:
                number = ' '+' '+' '+str(number)
            elif len(str(number)) == 2:
                number = ' '+' '+str(number)
            elif len(str(number)) == 3:
                number = ' '+str(number)
            elif len(str(number)) == 4:
                number = str(number)
            print (number)
            print('-----')
            if l[y + 1] == '+':
                z = int(num) + int(number)
            elif l[y + 1] == '-':
                z = int(num) - int(number)
            if len(str(z)) == 1:
                z = ' '+' '+' '+' '+str(z)
            elif len(str(z)) == 2:
                z = ' '+' '+' '+str(z)
            elif len(str(z)) == 3:
                z = ' '+' '+str(z)
            elif len(str(z)) == 4:
                z = ' '+str(z)
            if b == True:
                print(z)
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49","24 - 1"],True)