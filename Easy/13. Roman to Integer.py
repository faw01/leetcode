class Solution:
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
        s = s[::-1] # reverse
        for char in s:
            print(char)
            get_map_value = roman_to_int_map.get(char)
            final_int += get_map_value
        print(f'int is: {final_int}')
        return final_int

if __name__ == "__main__":
    sol = Solution()
    roman = "MCMXCIV"
    assert sol.romanToInt(roman) == 1994

