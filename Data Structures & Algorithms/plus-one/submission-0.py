class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        no = ""
        for i in digits:
            no += str(i)
        result = int(no) + 1

        result_list = [int(i) for i in str(result)]
        return result_list