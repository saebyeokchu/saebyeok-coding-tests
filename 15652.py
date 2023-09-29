#오름차순일것
#겹치는 부분이 엇ㅂ을것
class Solution:
    def permute(self, nums, count) :
        results = [] #[[1,2][1,3]...]
        
        if len(nums) == 1 :
            return [nums[:]]
        
        #execute for only two depth
        for i in range(len(nums)) :
            target = nums.pop(0)
            
            if count == 0:
                return nums
            else :
                print("nums : ",nums)
                perms = self.permute(nums,count-1)
                print("perms : ",perms)
                
                perms.append(target)
                
                results.append(perms)
            
            nums.append(target)
        
        return results
            
            
    
answer = Solution().permute([1,2,3,4], 2)
print(answer)
