class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        combinations = []
        combination = str()
        reverse_combination = str()

        results = []

        for word in words:
            combination += word

        for word in words[::-1]:
            reverse_combination += word

        combinations.append(combination)
        combinations.append(reverse_combination)

        for word in combinations:
            max_index = len(s)-1
            start = 0
            end = len(word)

            while end <= max_index:
                if word == s[start:end]:
                    results.append(start)

                start += 1
                end += 1

        results.sort()

        return results

def main():
    solution = Solution()
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    print(solution.findSubstring(s,words))
    s = "wordgoodstudentgoodword"
    words = ["word", "student"]
    print(solution.findSubstring(s,words))

if __name__ == '__main__':
    main()
