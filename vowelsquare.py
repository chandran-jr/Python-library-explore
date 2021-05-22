def fn(l):
    for i in range(len(l)-1):
        for j in range(len(l[i])-1):
            k=[l[i][j],l[i][j+1],l[i+1][j],l[i+1][j+1]]
            if(set(k).issubset(v)):
                return i,j
                break
    return 'No'

l=["aqrst", "ukaei", "ffooo"]
v=['a','e','i','o','u']
v=set(v)

print(fn(l))


'''
Vowel Square
Have the function VowelSquare(strArr)
take the strArr parameter being passed which will be a 2D matrix of some arbitrary size filled with letters from the alphabet, 
and determine if a 2x2 square composed entirely of vowels exists in the matrix. 
For example: strArr is ["abcd", "eikr", "oufj"] then this matrix looks like the following:
a b c d
e i k r
o u f j
Within this matrix there is a 2x2 square of vowels starting in the second row and first column, namely, ei, ou.
If a 2x2 square of vowels is found your program should return the top-left position (row-column) of the square,
so for this example your program should return 1-0. If no 2x2 square of vowels exists, then return the string not found.
If there are multiple squares of vowels, return the one that is at the most top-left position in the whole matrix.
The input matrix will at least be of size 2x2.
Examples
Input: ["aqrst", "ukaei", "ffooo"]
Output: 1-2
Input: ["gg", "ff"]
Output: not found
'''
