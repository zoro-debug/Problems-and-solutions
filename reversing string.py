"""Given a String of length S, reverse the whole string without reversing the individual words in it. Words are separated by dots.
Example:
Input:
2
i.like.this.program.very.much
pqr.mno

Output:
much.very.program.this.like.i
mno.pqr"""


t = int(input())
for i in range(t):
    st= input().split('.')
    st=st[::-1]
    st='.'.join(st)
    print(st)