arr=[1,4,2,5,6,3,4,7,6,4,3,1,5,7,8,3,9,1,10,13,15,16,12,17,19,16,12]

even=[]

odd=[]
i=0

while(i<len(arr)):

    if i%2==0:

        even.append(i)
        i=i+1

    else:
        odd.append(i)
        i=i+1

print("Even List=",even)

print("Odd List=",odd)
