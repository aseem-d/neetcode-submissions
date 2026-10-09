class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowered = s.lower()
        lowered_list = []
        for i in lowered:
            if i.isalnum() == True:
                lowered_list.append(i)
        rev = lowered_list[::-1]
        if lowered_list == rev:
            return True
        else:
            return False
        