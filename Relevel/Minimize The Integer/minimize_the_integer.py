num = input()
k=int(input())
newnum ="";
num = list(num)
count=0
for i in range(len(num)):
    # print(i)
    if(i==0):
        num[i] ="1"
    elif(num[i] != "0" and count<k-1):
        num[i]="0"
        count=count+1
    newnum = newnum+num[i]
print(newnum)