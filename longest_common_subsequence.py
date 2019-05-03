def lcs(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return ''
    if len(s1) == 0 or len(s2) == 0:
        return ''

    matrix = [["" for x in range(len(s2))] for x in range(len(s1))] #Initialise the empty matrix array
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    #Initialising first row and column with empty because the LCS with empty string will be empty
                    matrix[i][j] = s1[i]
                else:
                    #If matched, get the diagonal value and then append to the string
                    matrix[i][j] = matrix[i - 1][j - 1] + s1[i]
            else:
                #If characters in the strings are not the same, then check which character produces the longest subsequence, then keep that character
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1], key=len)

    #The final cell value of the matrix is the LCS
    cs = matrix[-1][-1]

    return cs



#Test combinations created using the site http://lcs-demo.sourceforge.net/
#Test[2] = LCS
test_combinations = [
    ['A', '', ''],
    ['', 'A', ''],
    ['', '', ''],
    ['A', 'A', 'A'],
    ['DCCC', 'CABB', 'C'],
    ['ABCBDAB', 'BDCABA', 'BCBA'],
    ['ACBCCBCBBABBBB', 'DBCADAADAAADBD', 'BCAB'],
    ['CACDAAACDC', 'CBBADCAADD', 'CACAAD'],
    ['BCAAABBBAAAABCCBBACACB', 'ADBCBBDDCCCDBCDDDBAAAD', 'BCBBCCBBAA'],
    ['CDABAABBDCDADDDADBABBBBDDABCBABB', 'AAADAACCCABACAACAADAACDACCDACCDD' , 'CABAACDADADADD']
]

result_list = []
for test in test_combinations:
    if test[2] == lcs(test[0], test[1]):
        result_list.append(True)

if False not in result_list:
    print('all tests have passed.')