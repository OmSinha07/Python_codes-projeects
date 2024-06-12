import random
def linear_search(nums,item):
     j=0
     while j < len(nums):
        if nums[j]==item:
          return j
        else:
          j=j+1
     return -1
i=0
nums=[]
while i < 10:
 j =random.randint(1,20)
 nums.append(j)
 i+=1
print(nums)
item=int(input("Enter number to be searched"))
print(linear_search(nums,item))