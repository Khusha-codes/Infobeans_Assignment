s=input("Input")
long=""
for i in range(len(s)):
    temp=""
    for j in range(i,len(s)):
            temp+=s[j]
            c=0
            for k in range(len(s)-len(temp)+1):
             if s[k:k+len(temp)]==temp:
                 c+=1
            if c >= 2 and len(temp) > len(long):
               long = temp  
print("Longest String",long)