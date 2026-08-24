class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_sum=float('inf')
        cur_arr=[]
        cur_sum=0
        #first window 
        for i in range(k):
            cur_arr.append(arr[i])
            cur_sum += abs(arr[i]-x)
        min_sum=min(min_sum, cur_sum)
        best_arr=cur_arr
        left=0
        for num in range(k, len(arr)):
            cur_sum -= abs(arr[left]-x)
            cur_sum += abs(arr[num] - x)
            left+=1
            cur_arr= cur_arr[1:] + [arr[num]]

            if cur_sum < min_sum:

                min_sum = cur_sum
                best_arr = cur_arr
        return best_arr