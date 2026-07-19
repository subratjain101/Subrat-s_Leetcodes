class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        answer = []

        def solve(index, current):

            if index == len(s):

                answer.append(current)

                return

            if s[index].isalpha():

                solve(index + 1, current + s[index].lower())

                solve(index + 1, current + s[index].upper())


            else:

                solve(index + 1, current + s[index])

        solve(0, "")
        return answer

 
