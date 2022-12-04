class Solution:
    # first attempt - LEETCODE SUBMISSION: Accepted
    def romanToInt(self,s: str) -> int:
        roman_to_int_map = {
            'I': 1,
            'V': 5,
            'X' : 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        final_int = 0
        s = s[::-1] # reverse VICXMCM
        for char in s:
            print(char)
            get_map_value = roman_to_int_map.get(char) 
            final_int += get_map_value
        print(f'int is: {final_int}')
        return final_int

    # 

    # neetcode attempt - LEETCODE SUBMISSION: Accepted
    def romanToInt(self,s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X' : 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        res = 0

        for i in range(len(s)):
            print(i)
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        
        return res


if __name__ == "__main__":
    sol = Solution()
    roman = "III"
    assert sol.romanToInt(roman) == 3