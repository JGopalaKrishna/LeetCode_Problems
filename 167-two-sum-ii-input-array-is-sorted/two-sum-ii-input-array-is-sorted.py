class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sets=set(numbers)
        for i in sets:
            find=target-i
            if find in sets:
                inx1=numbers.index(i)+1
                inx2=numbers.index(find)+1
                if inx1 > inx2:
                    return [inx2,inx1]
                elif inx1==inx2:
                    return [inx1,inx1+1]
                else:
                    return [inx1,inx2]