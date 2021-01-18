class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # concat array of number to str
        number = int("".join([str(num) for num in digits])) + 1
        # if number leads with zero
        if digits[0] == 0 and len(digits) > 1:
            # add zero by the len of the digit array to the beginning
            number = int("".join([str(num) for num in digits])) + 1
            integer_len =  len([digit for digit in str(number)])
            return [0]*(len(digits)-integer_len) + [digit for digit in str(number)] 

        # convert it back to int
        # return add 1 to int
        # print(number)
        return  [digit for digit in str(number)] 