import Test

def max_number(n):
    numStr = str(n) #turn your int n into a string
    max_num_Str = ""
    digitList = []
    
    for digitStr in numStr:
        digitList.append(int(digitStr))
    
    digitList.sort(reverse=True)
    
    for digit in digitList:
        max_num_Str += str(digit)
        
    return int(max_num_Str)
    
    
        
Test.describe("Basic tests")
Test.assert_equals(max_number(213), 321)
Test.assert_equals(max_number(7389), 9873)
Test.assert_equals(max_number(63792), 97632)
Test.assert_equals(max_number(566797), 977665)
Test.assert_equals(max_number(1000000), 1000000)
print("<COMPLETEDIN::>")