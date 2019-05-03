####
# Date 03/05/2019
# @author John Joy Kurian
#
# Write a program to perform pattern matching
#



#Function to replace two or more stars with a single occurence of *
def squeeze(char, s):
    while char * 2 in s:
        s = s.replace(char * 2, char)
    return s


#Main function that takes a string and pattern as input arguments and return a boolean True or False indicating whether it matches or not
def regex(s, p):
    if len(p) == 0 and len(s) == 0: #If both are empty, return True
        return True

    p = squeeze("*", p) #Merging all the stars that occur together into one

    if len(s) == 0 and p == "*": #Empty string matches with a single star
        return True

    if (len(p) == 0 and len(s)!= 0) or len(p) == 1 and p == '*': #If string is non-empty and the pattern is empty or pattern is * and string is non-empty, return False
        return False



    if p[0] == "*": #Removing the first star as it just translates to blank
        p = p[1:]

    i,j, match_counter_string, match_counter_pattern, match_char = 0, 0, 0, 0, ''

    while i <= len(s)-1 and j <= len(p)-1:
        if s[i] == p[j] or p[j] == ".":
            #Move the pointer on string and pattern by 1 each when there is a match or '.' is encountered
            match_counter_string += 1
            match_counter_pattern += 1
            match_char = s[i]
            i += 1
            j += 1
        elif p[j] == "*" and (p[j-1] == s[i] or p[j-1] == '.'):
            match_counter_string += 1
            match_char = s[i]
            i += 1 #Move only the string pointer by 1, the next string char will be checked at same pointer position
        elif (s[i] != p[j] and p[j] == "*") or (match_counter_pattern < match_counter_string):
            #This condition is hit when another string character breaks the star match
            #When * appears, match_counter_pattern will be always be lesser than match_counter_string
            if match_counter_pattern < match_counter_string:
                if (p[j+1] == match_char and p[j+2] == "*") and j+2<len(p):
                    match_counter_pattern += 1 #Since it's a variable used to match the string counter, doesn't have to be incremented by 2 here
                    j += 2 #move over the letter as well as the star
                elif (p[j+1] == "*" or p[j+1] == match_char) and j+1<len(p):
                    match_counter_pattern += 1
                    j += 1
                else:
                    j += 1
            else:
                j += 1
        else:
            match_counter_string, match_counter_pattern = 0, 0
            i = 0 #Reset string pointer to 0
            j += 1
        if i == len(s):
            break

    #If the pointer is at the end of the string, then it's a match
    if len(s) == i:
        return True
    else:
        return False




        ####### Testing code ######

#Test string-pattern combinations
test_combinations = [
    ['aba', '*ab', False],
    ['aa', 'a*', True],
    ['ab', '.*', True],
    ['ab', '.', False],
    ['aab', 'c*a*b', True],
    ['aaa', 'a*', True],
    ['ccaaaabbbddc', 'c*aaaaa***aa*aa*a*aa*ab*d*cbbb', False],
    ['aab', '.ab', True],
    ['abc', '.*', True],
    ['abc', 'cf.*x', True],
    ['dcb', 'dca*b', False],
    ['a', 'a*', True],
    ['aab', 'dc*a*b', True],
    ['abc', '..', False],
    ['abc', '...', True],
    ['abc', '.*..*', True],
    ['abc', '...*', True],
    ['abc', '*...*', True],
    ['abc', 'a', False],
    ['aabaaad', 'c*a*aba*d.*', True],
    ['abc', '*abc', True],
    ['abc', '', False],
    ['abc', '*', False],
    ['abc', '**', False],
    ['abc', '***', False],
    ['abc', '***ab*c', True],
    ['abc', '*.', False],
    ['abc', '*..', False],
    ['abc', '*...', True],
    ['cab', 'ca*a*a*b', False ],
    ['cab', 'caaa*a*a*b', False ],
    ['caaaab', 'caaa*a*a*b', False ],
    ['caaaaab', 'caaa*a*a*b', True],
    ['caaaaab', 'caaa*aa*a*b', False],
    ['caaaaaab', 'caaa*aa*a*b', True],
    ['caaaaaaab', 'caaa*a*a*b', True],
    ['caaaaaaaaaaaaaab', 'caaa*a*a*b', True],
    ['', '', True],
    ['', '*', True],
    ['abcd', 'abcd', True],
    ['string', 'superstring', True]
]



has_passed = False
result_list = []
for test in test_combinations:
    match_result = regex(test[0], test[1])
    print('\nstring: ' + test[0] + '\npattern: ' + test[1] +'\nmatch condition: ' + str(match_result) + '\n')
    if match_result != test[2]:
        print('!!!!! test failed at: ' + '\nstring: ' + test[0] + '\npattern: ' + test[1] )
    result_list.append(match_result == test[2])


for index, result in enumerate(result_list):
    if result is False:
        print('test failed at: ', test_combinations[index])

if False not in result_list:
    print('all tests have passed.')