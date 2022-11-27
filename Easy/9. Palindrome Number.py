class Solution:
    # first attempt - LEETCODE SUBMISSION: Accepted
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        palindrome_array = []
        x_array = [x]
        for i in str(x):
            palindrome_array.append(i)

        palindrome_array.reverse()
        palindrome_array = int("".join(map(str, palindrome_array)))
        palindrome_array = [palindrome_array]

        if palindrome_array == x_array:
            return True
        
        return False

    # i knew i had to kind of convert the integer to a string, so i started with that, buy quickly changed
    # my approach to an array based one using reverse and then join the str using map to convert each
    # element to an integer so i could compare

    # second attempt with google - LEETCODE SUBMISSION: Accepted
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]

    # this is a much more efficient way of doing it, i forgot about string slicing as
    # in my appraoch i already used arrays, however im sure if i had used strings i would have
    # started with string slicing, [::-1] reverses the string however
    # this is still inefficient

    # neetcode attempt - LEETCODE SUBMISSION: Accepted
    # https://youtu.be/yubRKwixN-U
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        div = 1
        while x >= 10 * div:
            div *= 10

        while x > 0:
            right = x % 10
            left = x // div
            if left != right:
                return False
            x = (x % div) // 10
            div //= 100
        return True

if __name__ == "__main__":
    sol = Solution()
    num = -1001
    print(f'returns: {sol.isPalindrome(num)}')
    # assert sol.isPalindrome(num) == True