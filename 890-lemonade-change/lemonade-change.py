class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        5 = add 
        10 = if 5  then add 10 and 5count-=1
        if 20  if (10 and 5) then (10count-=1, 5count-=1) or (5count >=3 then 5count-=3)
        """
        count_5=0
        count_10=0

        for i in bills:
            if i ==5:
                count_5 += 1
            elif i == 10:
                if count_5 >=1:
                    count_5 -= 1
                else:
                    return False
                count_10 += 1
            else:
                if (count_10 >=1 and count_5 >= 1):
                    count_10 -= 1
                    count_5 -= 1
                elif (count_5 >= 3):
                    count_5 -=3
                else:
                    return False
        
        return True