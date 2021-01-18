class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start_increment = 0
        end_increment = -1
        target = abs(target)
        start = numbers[start_increment]
        end = numbers[end_increment]
        while abs(sum([start,end])) != target:
            TwoSum = abs(sum([start,end]))
            if TwoSum > target:
                end_increment -= 1
                end = numbers[end_increment]
            elif TwoSum < target:
                start_increment += 1
                start = numbers[start_increment]
        return [start_increment+1,len(numbers)+end_increment+1]