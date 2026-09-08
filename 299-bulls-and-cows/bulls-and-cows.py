class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        """
        if secret[i]==guess[i]
        count_bulls += 1
        secret[i] -> remove
        guess[i] -> remove
        secret=secret[:i]] + secret[i:]
        guess=guess[:i] + guess[:i]
        """
        n=len(secret)
        bulls_count=0
        cows_count=0
        freq_secret={}
        freq_guess={}
        for i in range(n):
            if secret[i] == guess[i]:
                bulls_count += 1
            else:
                freq_secret[secret[i]]=freq_secret.get(secret[i], 0)+1
                freq_guess[guess[i]]=freq_guess.get(guess[i], 0)+1
        
        for i in freq_secret:
            if i in freq_guess:
                cows_count += min(freq_secret[i], freq_guess[i])
        
        return str(bulls_count) + "A" + str(cows_count) + "B"