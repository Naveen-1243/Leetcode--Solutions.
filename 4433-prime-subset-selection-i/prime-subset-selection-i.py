class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        
        def prime_numbers(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False

            for i in range(2, int(n ** 0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False

            return [i for i in range(2, n + 1) if is_prime[i]]
    
        x=prime_numbers(n)
        ind=0
        total=0
        for i, val in enumerate(x):
            if total + val >s:
                return x[:i]
            else:
                total += val
        return x if total <=s else []