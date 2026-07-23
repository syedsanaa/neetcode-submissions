class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h={}
        for i in range(len(nums1)): 
            h[nums1[i]]=i 
        s=deque()
        out=[-1]*len(nums1)
        for i in range(len(nums2)): 
            while s and nums2[i]>s[-1]: 
                e=s.pop()
                if e in h: 
                    out[h[e]]=nums2[i]
            s.append(nums2[i])
        return out