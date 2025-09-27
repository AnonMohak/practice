### use case
## lets say we have arr=[1,1,2,3,2,2,2,1] and we wanna return topk elements
## we can do that by making a 2d array and put all the elements in the order of there frequency
## then return the topk


def topK(nums, k):
    count={}
    freq=[[] for i in range(len(nums)+1)]   #we will need an extra space at the end
    sol=[]

    for i in nums:
        if i not in count:
            count[i]=1
        else:
            count[i]+=1

    print(count)

    for m,n in count.items():
        freq[n].append(m)

    print(freq)

    for x in range(len(freq)-1, 0, -1):
        for y in freq[x]:
            sol.append(y)
            if len(sol)==k:
                return sol


nums=[1,1,2,3,2,2,2,1]
k=2
rr=topK(nums,k)
print(rr)
