#### [537. Complex Number Multiplication](https://leetcode.com/problems/complex-number-multiplication/description/) ()
* 題目: 以字串形式給兩負數, 請回傳相乘結果
* Example 1:
    ```
    Input: "1+1i", "1+1i"
    Output: "0+2i"
    Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
    ```
* Example 2:
    ```
    Input: "1+-1i", "1+-1i"
    Output: "0+-2i"
    Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
    ```
* 解法簡述:
    ```
    給 a1+b1i & a2+b2i
    解法就是直接拆成 a1*a2 + a1*b2i+ a2*b1i + b1*b2*-1
    ```

#### [696. Count Binary Substrings](https://leetcode.com/problems/count-binary-substrings/description/) ()
* 題目: 
* Example 1:
    ```
    Input: "00110011"
    Output: 6
    Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

    Notice that some of these substrings repeat and are counted the number of times they occur.

    Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
    ```
* Example 2:
    ```
    Input: "10101"
    Output: 4
    Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
    ```
* 解法簡述:
    ```
    本題重點可以放在 因為只考慮連續的情況
    所以可以利用這個特性, 只要將連續的 0 跟 1 分開，然後兩兩找最小就可以了
    或是走過整個字串，檢查 i 及 i+1 是否相同
    如果相同就 cnt += 1
    如果不同就 ret.append(cnt), cnt = 1
    這樣就可以紀錄連續的 0 和 1的長度，接下來只要兩兩比較, 把短的那邊加起來就好了
    ```
#### [890. Find and Replace Pattern](https://leetcode.com/problems/find-and-replace-pattern/description/) (String)
* 題目: 給一字串陣列```words```及另一字串```pattern```, 找出在```words```中和```pattern```結構相同的字串並回傳
* Example 1:
    ```
    Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
    Output: ["mee","aqq"]
    Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
    "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
    since a and b map to the same letter.
    ```
* 解法簡述:
    ```
    這題解法可以完全使用 205. Isomorphic Strings 的解法
    只要所有 words 中的字串和 pattern 逐一比對就好了
    ```

#### [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/description/) (Hash Table, String)
* 題目: 給一字串陣列, 將同屬錯位字的字串變成一群後回傳
* Example 1:
    ```
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
    Output:
    [
    ["ate","eat","tea"],
    ["nat","tan"],
    ["bat"]
    ]
    ```
* 解法簡述:
    ```
    本題解法有兩種
    一是對每一個字串先計算字頻, 然後看過其他所有的字串並比較兩者字頻
    如果字頻相同就將其從原輸入陣列中移出放在另外一個陣列, 避免重複查閱
    二是利用 python 的 tuple 及 sort 來處理
    先將每個單字都 sort, 所以所有的錯位字都會變成一樣的
    接著使用 tuple 包起來以作為 dictionary 的 key
    這樣就可以確保所有的錯位字都會使用到同一個 key 放在一起
    最後回傳所有 dictionary 的 values
    ```
#### [205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/description/) ()
* 題目: 回傳兩輸入字串的結構是否相同
* Example 1:
    ```
    Input: s = "egg", t = "add"
    Output: true
    ```
* Example 2:
    ```
    Input: s = "foo", t = "bar"
    Output: false
    ```
* Example 3:
    ```
    Input: s = "paper", t = "title"
    Output: true
    ```
* 解法簡述:
    ```
    本題核心想法是假若兩字串結構一樣,
    則兩者每個字必定對應且出現位置必然相同
    所以我們使用兩陣列 [-1]*256 紀錄兩個字串中出現的字的位子
    接著同時查看兩個字串同位置上的字並記錄他們的 index
    如果遇到兩個字串上同位置的字在陣列中的值不同
    就表示對應的字之前出現在不同的地方，就代表結構不一樣
    ```

#### [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/description/) ()
* 題目: 給一字串陣列，回傳這陣列中所有字串的最長共通前綴
* Example 1:
    ```
    Input: ["flower","flow","flight"]
    Output: "fl"
    ```
* Example 2:
    ```
    Input: ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
    ```
* 解法簡述:
    ```
    這題的普通解法是
    先找出最短字串, 然後根據最短字串比對其他字串找出答案
    Python 則可以使用 zip*(strs)
    會使每個子字串的同一個位置的字都變成一個 tuple
    如此只要比較該 tupe 內是否一樣就沒問題了, 可以用 set 直接比較長度是否為 1
    ```
#### [409. Longest Palindrome](https://leetcode.com/problems/longest-palindrome/description/) ()
* 題目: 給一字串, 回傳將此字串重組後可以找到的最長的回文字串的長度
* Example 1:
    ```
    Input:
    "abccccdd"

    Output:
    7

    Explanation:
    One longest palindrome that can be built is "dccaccd", whose length is 7.
    ```
* 解法簡述:
    ```
    最簡單的做法就是先計算這個字串中每個字的字頻
    只要字頻 > 2 就可以幫助構成回文字串
    所以我們檢查每個字, 把 (字頻 //2) * 2 加起來
    最後要記得，如果這個加起來的值跟原字串等長, 就表示用完了字
    如果沒用完, 可以在回文字串正中間加一個字使其更長一個字元
    ```
#### [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/description/) ()
* 題目: 給一字串, 找出其連續的最長回文子字串
* Example 1:
    ```
    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.
    ```
* Example 2:
    ```
    Input: "cbbd"
    Output: "bb"
    ```
* 解法簡述:
    ```
    這題的解法可以借用 647. Palindromic Substrings 的想法
    這邊不多加贅述, 請往下看 647
    走過所有可能的回文字串中心點並向外逐漸擴增
    例如 "0123" 的字串, 回文字串的中心點只會是 [0, 1, 2, 3, 01, 12, 23]
    就可以確保看過所有的回文字串, 只要回傳就可以
    ```

#### [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/description/) ()
* 題目: 給一正整數 k 及一字串 S, k 表示你可以忽略的字元數,找出最長的且僅包含單一字元的字串之長度, 
* Example 1:
    ```
    Input:
    s = "ABAB", k = 2

    Output:
    4

    Explanation:
    Replace the two 'A's with two 'B's or vice versa.
    ```
* Example 2:
    ```
    Input:
    s = "AABABBA", k = 1

    Output:
    4

    Explanation:
    Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    The substring "BBBB" has the longest repeating letters, which is 4.
    ```
* 解法簡述:
    ```
    核心概念是運用 sliding windows
    可以先從假設 k 沒有限制開始想
    如果 k 沒有限制但希望用最少次, 那一定是找當前出現最多次的字
    然後將 string 全長 - 最多次的字的出現次數就是答案
    但現在有長度限制，所以我們從子字串 [start:end] = [0:0] 開始探索
    為了方便解釋，以下將"當前出現最多次的字的次數"稱為 max_char_count
    如果目前子字串長度扣掉 max_char_count 還小於等於 k, 就表示我還可以接受下一個字, 將 end += 1
    如果超過了，也就是當前子字串長度 > max_char_count + k, 就表示目前這個字串只用k次沒辦法改了
    我就持續將目前 start 的字從紀錄中扣掉，然後 start += 1
    直到滿足 (end-start+1) < max_char_count + k 才回到增加 end 的流程
    而每次增加 end 之前，都對當前長度進行比較，留下最大值，最後進行回傳即可
    ```
#### [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/) ()
* 題目: 給一字串，找出不包含重複字元的最長子字串
* Example 1:
    ```
    Input: "abcabcbb"
    Output: 3 
    Explanation: The answer is "abc", with the length of 3. 
    ```
* Example 2:
    ```
    Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    ```
* Example 3:
    ```
    Input: "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3. 
                Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
    ```
* 解法簡述:
    ```
    首先我們使用雙指針 start = 0 及 end
    然後使用迴圈來逐步增加 end
    並使用 dictionary 記錄每個字出現的最後位置
    如果目前看到的字是重複出現的(有在dictionary)
    而且這個字上次出現在目前 start 之後就表示會重複，
    所以要把 start 更新至這個字上次出現的下一個位子, 如此一來就可以避免重複。
    例如說 "abcabc"
    當我看到第3個字 也就是 c 的時候,
    我的字典是 {a:0, b:1, c:2}, start = 0, end = 2
    但我看到第四個字 也就是 a 的時候,
    我發現字典裡面已經有 a , 所以我要把 start 移到 d[a]+1 的位子
    並且更新我的字典 d
    所以會變成 {a:3, b:1, c:2}, start = 1, end = 3
    最後, 由於我只是要記錄長度, 所以我每個迴圈都比較看看
    end - start + 1 就好, 最後回傳最大值
    ```
#### [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/description/) ()
* 題目: 給一數字, 檢查是否回文
* Example 1:
    ```
    Input: 121
    Output: true
    ```
* Example 2:
    ```
    Input: -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
    ```
* Example 3:
    ```
    Input: 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    ```
* 解法簡述:
    ```
    這題的解法是透過建立一個反轉的 input 來比較
    可以到中間就斷掉也可以建立完整的反轉
    例如說 input = 12345, 就用 while 迴圈建立一個 54321 然後比較一下就好
    另外如果遇到 0 就是 True
    遇到負數就是 False
    ```
#### [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/description/) ()
* 題目: 給一字串, 回傳所有的連續回文子字串的數量
* Example 1:
    ```
    Input: "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".
    ```
* Example 2:
    ```
    Input: "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
    ```
* 解法簡述:
    ```
    這個解法的想法分成2個部分
    1) 走過所有的 substring
    2) 每走過一個 substring, 就確認他是不是回文
    下面的解法將這兩點同時利用，從長度 1 和 2 的 substring 開始
    如果目前的 substring 是回文的，那就將其左右各加一，繼續檢查
    下方迴圈所要走遍所有可能 substring 的中心點
    pp則去檢查說，以目前的中心點往外不斷擴張，可以有幾個 substring
    如此一來就可以涵蓋到所有的 substring, 如果要更仔細地解釋，
    可以想像出所有的 substring 分成奇數長度跟偶數長度, 若假設 s 的長度為 3
    可能的奇數長度 substring 的中心點就一定是第 0, 1 ,2 個元素
    而可能的偶數長度substring 的中心點就一定是 [0:1], [1:2] 的連續元素
    接著我們將這些可能的中心點同時向左右拓展就會得到
        0 : 0
        1 : 1, [0:2]
        2 : 2
        [0:1] : [0:1]
        [1:2] : [1:2]
    如此一來就看完了所有可能的 substring
    ```

#### [459. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/description/) ()
* 題目: 給一字串, 請問這個字串是否是由另一子字串連接數次而成
* Example 1:
    ```
    Input: "abab"
    Output: True
    Explanation: It's the substring "ab" twice.
    ```
* Example 2:
    ```
    Input: "aba"
    Output: False
    ```
* Example 3:
    ```
    Input: "abcabcabcabc"
    Output: True
    Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
    ```
* 解法簡述:
    ```
    我知道的解法有兩種
    1)  這個想法比較難想到
        如果是一個重複的字串
        那麼s第一個字必定是重複字串的字首
        那麼s最後一個個字必定是重複字串的字尾
        把s *2 然後把頭跟尾去掉
        假設他是個重複的字串
        就一定會在中間出現s

    2)  這個想法比較務實一點
        就是根據長度判斷如果是重複的，那麼 substring 之長度必定可以整除 string
        從 1 ~ len(s)//2 去找可以整除的值, 將這段substring串接成和string等長
        然後做比較看看是不是一樣的
    ```
#### [856. Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/description/) ()
* 題目: 很複雜但建議看看
* Example 1:
    ```
    Input: "()"
    Output: 1
    ```
* Example 2:
    ```
    Input: "(())"
    Output: 2
    ```
* Example 3:
    ```
    Input: "()()"
    Output: 2
    ```
* Example 4:
    ```
    Input: "(()(()))"
    Output: 6
    ```
* 解法簡述:
    ```
    這個解法的想法是括號的深度
    計算深度來區別目前的乘法量，也就是說
    深度已經決定這層括號內的每個數字要被乘幾次了
    舉例來說 ()(()(()(())))
    先將 () 相連的抽換成 1 就會變成
    1(1(1(1)) -> 1 + (1) + ((1)) + (((1))) -> 1 + 2 + 4 + 8
    而下面的解法是
    當遇到左括號，就往下一層深度, stack 多加一個 0
    當遇到右括號，就退出一層深度，stack.pop(), 而根據當前的數值，這裡分成兩種狀況
        假若 stack.pop() 為 0 那就表示這是一個單獨的(), 在上一層+1
        假若 stack.pop() 大於 0, 就表示這是一個包含其他括號的右括號結尾如 (()()) 的最後一個括號
        這樣的話我就把當前的值*2, 加回到上一層的 stack
    可以看 https://leetcode.com/problems/score-of-parentheses/solution/ 的 solution 2
    ```
#### [678. Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/description/) ()
* 題目: 沒上面複雜, 也比較好寫的題目, 自己去看
* Example 1:
    ```
    Input: "()"
    Output: True
    ```
* Example 2:
    ```
    Input: "(*)"
    Output: True
    ```
* Example 3:
    ```
    Input: "(*))"
    Output: True
    ```
* 解法簡述:
    ```
    這個 greedy 的解法的想法是在 pass 整個字串的過程中
    去計算當前的 `balance`, 所謂的 balance 
    就是把'('當成+1, 把')'當成-1, 把字串轉換成一個數字的意思
    一個合法的括號方式，從 0 開始的子字串之 balance 必定大於 0
    (balance 大於 0 的意思其實就是左括號比右括號多的意思)
    而這題又多了一個萬能字元 - 星號，所以我們不能只計算 balance
    要考慮 balance 可能的最大值及最小值
    也就是說
        '(' 會使 最大值跟最小值都 +1
        ')' 會使 最大值跟最小值都 -1
        '*' 會使 最大值 +1 而最小值 -1
    過程中，只要最大值沒有 == 0 就沒關係
    最小值每次要經過 max(0, 最小值), 確保其 >0
    這個動作的前提是最大值要是大於0的
    只要最大值大於0, 就表示目前還有機會是合法的括號字串
    所以如果要往後再接一個, 必定是基於合法的往後接
    不可能是基於一個 balance = -1 的字串繼續計算 balance
    所以最小值如果小於0 就一定要重製成 0
    最後跳出迴圈的時候，如果最大值是 > 0 而且最小值 <= 0
    就會是正確的，這個條件之所以要求最小值 <= 0 是因為
    必須讓最大值跟最小值之間包含 0, 因為合法的括號字串 balance 只能為 0
    假若看過最後一個字母後, 最小值 > 0, 這代表我們有太多左括號
    經過 low = max(low, 0) 依然會是 > 0
    但如果 low 是負的且 high 是正的, low = max(low, 0) 就會是 0
    ```
#### [916. Word Subsets](https://leetcode.com/problems/word-subsets/description/) ()
* 題目: 給兩個字串陣列 A , B, 試著找出 A 之中完全包含 B 所有字串的字串
* Example 1:
    ```
    Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
    Output: ["facebook","google","leetcode"]
    ```
* Example 2:
    ```
    Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
    Output: ["apple","google","leetcode"]
    ```
* Example 3:
    ```
    Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
    Output: ["facebook","google"]
    ```
* Example 4:
    ```
    Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
    Output: ["google","leetcode"]
    ```
* Example 5:
    ```
    Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
    Output: ["facebook","leetcode"]
    ```
* 解法簡述:
    ```
    直覺的想法就是分成 3 個步驟
        1) 求出每個 b 的要求
        2) 整合 B 的最低要求
        3) 檢查每個 a 是否符合 B 的最低要求
    額外的改善是使用 dict
    total_dict 就是 B 的要求，但不同於長度為 26 的 list
    這邊只記錄了字母數 > 0 的字母，所以後面再檢驗 a 的時候會比較快
    另外也利用了 count function 加速
    ```
#### [6. ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/description/) ()
* 題目: 很難說明
* Example 1:
    ```
    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"
    P   A   H   N
    A P L S I I G
    Y   I   R
    ```
* Example 2:
    ```
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:

    P     I    N
    A   L S  I G
    Y A   H R
    P     I
    ```
* 解法簡述:
    ```
    我的解法是根據給定 row 的數量可以計算出每次擺放位置的規律
    例如 numRows = 4
    規律為 [0, 1, 2, 3, 2, 1, 0, 1, 2, 3, ...]
    所以只要按照這個規律建立四個不同的字串
    將原輸入字串的每個字按照規律放在四個字串中
    最後接起來就是答案
    ```