def permutator(arr):
    input=arr.split(',')
    for i,j in enumerate(input):
        input[i]=int(j)
    result = [input[:]]
    c = [0] * len(input)
    i = 0
    while i < len(input):
        if c[i] < i:
            if i % 2 == 0:
                input[0], input[i] = input[i], input[0]
            else:
                input[c[i]], input[i] = input[i], input[c[i]]
            result.append(input[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result


def createNumstr(num):
    strr=''
    for i in range(1,num+1):
        if i==1:
            strr=strr+str(i)
        elif i>1:
            strr=strr+","+str(i)

    return strr


def hire(paselimit, remain):
    for i in range(len(remain)):
        if remain[i]>=paselimit:
            return remain[i]
    return remain[len(remain)-1]

result=[]

for i in range(4,10):
    best={'candidate':1,'preview':0,'probability':0}#딕셔너리
    successs=[]
    print('지원자 ',i,"명")
    for j in range(1,i-1):
        print("this is j : ",j)
        cases =permutator(createNumstr(i))
        for k in cases:
            preview=k[0:j]
            passlimit=max(preview)
            remain=k[j:]
            success=hire(passlimit,remain)
            if success==i:
                successs.append(success)
        probabilty=len(successs)/len(cases)

        if best['probability']> probabilty:
            break
        if best['probability'] < probabilty:
            best['preview']=j
            best['probability']= probabilty
        print(j,"명 살펴보기, 채용 성공 확률:",len(successs)/len(cases))
        successs=[]
    result.append(best['probability'])
print(result)

