class Solution:
    def sumGame(self, num: str) -> bool:
        first=len(num)//2
        first_sum=0
        first_count=0
        second_count=0
        for i in range(first):
            if num[i] =="?":
                first_count+=1
            else:
                first_sum += int(num[i])
        
        second_sum=0
        for i in range(first,len(num)):
            if num[i] != "?":
                second_sum += int(num[i])
            else:
                second_count+=1
        
        count_diff=second_count - first_count
        if count_diff % 2 == 1:
            return True

        sum_diff = first_sum - second_sum

        return count_diff * 9 != 2 * sum_diff
     