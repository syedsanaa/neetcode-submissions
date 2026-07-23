class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            my_dict = {key: 1 for key in nums}
            for i in range(len(nums)):
                count=1
                if my_dict.get(nums[i]-1,0)==0: 
                    number=nums[i]
                    while  my_dict.get(number+1,0)!=0:
                        print(number)
                        count+=1 
                        number+=1
                    my_dict[nums[i]]=count
            maxi=max(my_dict.values(), default=0)
            return maxi 

