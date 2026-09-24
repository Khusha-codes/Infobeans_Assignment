def substring(str):
    for i in range(len(str)):
        for j in range(len(str)):
            s = str[i:j+1]
            if s:
                print(s)
            
