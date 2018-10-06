class Solution{
    findSubstring(s, words) {
        /*
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        */

        var combinations = [];
        var combination = '';
        var reverse_combination = '';
        var results = [];

        words.forEach(function(word) {
          combination += word;
        });

        words.reverse();
        words.forEach(function(word) {
          reverse_combination += word;
        });

        combinations.push(combination);
        combinations.push(reverse_combination);

        combinations.forEach(function(word) {
          var max_index = (s.length - 1);
          var start = 0;
          var end = word.length;
          while ((end <= max_index)) {
              if ((word === s.slice(start, end))) {
                  results.push(start);
              }
              start += 1;
              end += 1;
          }
        });

        return results;
    }
}
function main() {
    var s, solution, words;
    solution = new Solution();
    s = "barfoothefoobarman";
    words = ["foo", "bar"];
    console.log(solution.findSubstring(s, words));
    s = "wordgoodstudentgoodword";
    words = ["word", "student"];
    console.log(solution.findSubstring(s, words));
}

main();
