def solution(text, ending):
    # your code here...
    return text[-len(ending):] == ending

#-------------OR---------------
'''
def solution(text, ending):
    # your code here...
    return text.endswith(ending)
'''

print(solution('abcde', 'cde'))
print(solution('abcde', 'abc'))
print(solution('abc', 'abcd'))
