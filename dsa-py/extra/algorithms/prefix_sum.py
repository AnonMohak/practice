### use case
## let say we have an arr=[1,2,4,6] and we want to return an arr of the product of numbers except self and in O(n)
## we can use product prefix and suffix 

def productExceptSelf(nums):
    res=[1]*len(nums)
    pre,post=1,1

    for i in range(len(nums)):
        res[i]=pre
        pre*=nums[i]

    for j in range(len(nums)-1, -1, -1):
        res[j]*=post
        post*=nums[j]

    return res

nums=[1,2,4,6]
pp=productExceptSelf(nums)
print(pp)
