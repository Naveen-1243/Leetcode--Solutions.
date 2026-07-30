class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        for i in range(len(number)):
            if number[i]==digit and i+1 < len(number) and number[i] < number[i+1]:
                return number[:i]+number[i+1:]
        
        x=number.rfind(digit)
        return number[:x] + number[x+1:]