
class Bullcows:
    def bullsCows(secret, guess):
        bulls=0
        cows=0
        i_secret=list(secret)
        i_guess=list(guess)
        for i in range(0, len(secret)):
            if(secret[i]==guess[i]):
                bulls += 1
                i_secret.remove(secret[i])
                i_guess.remove(guess[i])

        x=0
        while (x<len(i_secret)):
            if(i_guess[x] in i_secret):
                cows += 1
                value=str(i_guess[x])
                i_guess.remove(value)
                i_secret.remove(value)
            else:
                x=x+1

        output= "%sA%sB" %(bulls,cows)
        return output

