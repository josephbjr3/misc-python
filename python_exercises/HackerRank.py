def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    #first for loop allows jump every 3 letters in the stirng
    for letter_index in range(0,n,k):
        #placeholder for "u" substring
        u = ""
        #weeds out the duplicates in the substring
        for sub_letter in string [letter_index : letter_index + k]:
            if sub_letter not in u:
                #adds non-duplicates to "u"
                u += sub_letter
        #prints "u" each iteration, allowing them to be printed on seperate lines
        print(u)


            
if __name__ == '__main__':
    
    merge_the_tools('AABCAAADA', 3)