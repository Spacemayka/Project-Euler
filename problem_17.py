# https://projecteuler.net/problem=17

lenOneToNine = 36
lenTentonNineteen = 70
lenOneToNineteen = 106
lenTwentyToNinety = 46
lenTwentyToNinetynine = 748 # 10*lenTwentyToNinety + 8*lenOneToNine 
lenOneToNinetyNine = 854 # lenTwentyToNinetynine + lenOneToNineteen
lenHundredAnd = 10
lenHundred = 7
lenOneThousand = 11

lengthOfNumbers = lenOneToNinetyNine + lenOneToNine*100 + lenOneToNinetyNine*9 + lenHundredAnd*891 + lenHundred*9 + lenOneThousand

print(lengthOfNumbers)

