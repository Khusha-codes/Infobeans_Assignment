def subarray(lst,t):
    if t < 1:
        print("Targen must be a positive integers")
    else:
        i = 0
        res = [0]*len(lst)
        while i <= len(lst):
            temp = []
            sum = 0
            j = i
            while j <= len(lst):
                sum += j
                temp.append(j)
                if sum == t:
                    if len(temp) < len(res):
                        res = temp
                        break
                    else:
                        break
                j+=1
            i+=1
        print(res)
