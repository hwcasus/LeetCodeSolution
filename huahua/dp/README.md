# DP

## Strategy

太多種題型了

## The List

|Id|Name|Difficulty|Similar Problems|Comments|
|-|-|-|-|-|
|70|Climbing Stairs|★|746,1137|I: O(n), S = O(n), T = O(n)|
|303|Range Sum Query – Immutable|★|1218|~~|
|53|Maximum Subarray|★★|121|~~|
|62|Unique Paths|★★|63,64,120,174,931 |I: O(mn), S = O(mn), T = O(mn)|
|85|Maximal Rectangle|★★★|221,304,1277|~~|
|198|House Robber|★★★|213,309,740,790,|I: O(n), S = O(3n), T = O(3n)|
|279|Perfect Squares|★★★||I: n, S = O(n), T = O(n*sqrt(n))|
|139|Word Break|★★★|140,818|I: O(n), S = O(n), T = O(n^2)|
|300|Longest Increasing Subsequence|★★★|673,1048|~~|
|96|Unique Binary Search Trees|★★★||~~|
|1105|Filling Bookcase Shelves|★★★||I: O(n) + t, S = O(n), T = O(n^2)|
|131|Palindrome Partitioning|★★★||I: O(n), S = O(2^n), T = O(2^n)|
|72|Edit Distance|★★★|10,44,97,115,583,712,1187,1143,1092,|I: O(m+n), S = O(mn), T = O(mn)|
|1139|Largest 1-Bordered Square|★★★||I: O(mn), S = O(mn)  T = O(mn*min(n,m))|
|688|Knight Probability in Chessboard|★★★|576,935|I: O(mn) + k  S = O(kmn), T = O(kmn)|
|322|Coin Change|★★★|377,416,494,1043,1049,1220,1230,1262,|I: O(n) + k, S = O(n), T = O(kn)|
|813|Largest Sum of Averages|★★★★|1278,1335,|I: O(n) + k S = O(n*k), T = O(kn^2)|
|1223|Dice Roll Simulation|★★★★||I: O(n) + k + p S = O(k*p), T = O(n^2kp)|
|312|Burst Balloons|★★★★|664,1024,1039,1140,|I: O(n), S = O(n^2), T = O(n^3)|
|741|Cherry Pickup|★★★★||I: O(n^2), S = O(n^3), T = O(n^3)|
|546|Remove Boxes|★★★★★||I: O(n), S = O(n^3), T = O(n^4)|
|943|Find the Shortest Superstring|★★★★★|980,996,|I: O(n) S = O(n*2^n), T = (n^2*2^n)|


## Memorable

| Title | Difficulty |
| - | - |
| 174. Dungeon Game | |
| 221. Maximal Square | |
| 85. Maximal Rectangle | |
| 84. Largest Rectangle in Histogram | |
| 304. Range Sum Query 2D - Immutable | |
| 1277. Count Square Submatrices with All Ones | |
| 213. House Robber II | |
| 740. Delete and Earn | |
| 1143. Longest Common Subsequence | |
| 583. Delete Operation for Two Strings | |
| 712. Minimum ASCII Delete Sum for Two Strings | |
| 718. Maximum Length of Repeated Subarray | |
| 300. Longest Increasing Subsequence | |
| 279. Perfect Squares | |
| 673. Number of Longest Increasing Subsequence (NLIS) | |
| 1048. Longest String Chain | |
| 96. Unique Binary Search Trees | |
| 1105. Filling Bookcase Shelves | |
| 131 Palindrome Partitioning | |
| 1139. Largest 1-Bordered Square | |

---

### 174. Dungeon Game

---

### 221. Maximal Square

---

### 85. Maximal Rectangle

本題有夠難, 我的解法也跟 dp 沒啥關係,
基本上參照 84 題解法, 而差別在於我們每個 row 都跑一次
但這不是最好的解法, 最好的是這招配上 DP

---

### 84. Largest Rectangle in Histogram

本題雖然是上一題的前身, 但也是難到靠北

題目輸入為 heights (list of integers), 代表不同高度的 histogram,
將這些不同高度的 histogram 排列再一起, 求最大的長方形 (建議看個圖片, 比較能夠理解)

因為我也是看答案的, 所以這邊就直接先大概講一下原理

迭代過 heights 並依序放入 stack
然後維持一個 monotonic stack , (單調遞增/減)

但如果當我們放入一個元素, 會導致這個 stack 不再是 monotonic stack 時
就要開始計算 rectangle 面積

從結果來看, 可以將這個動作解釋為
當我們單調上升的時候, 每一個 histogram 的高度, 都還有機會變成更大的 rectangle
而一但開始下一個 height 沒有比目前最大的還大, 就表示對於目前最大的那個 histogram
他已經不可能在同樣高度下找到更大的 rectangle 了, 舉例來說

heights = [1, 5, 6, 8, 3, 4, 8]

當我們 iterate 到 3 時, stack = [1, 5, 6, 8]

這時候我們把 8 拿出來, 我們知道他前面一定比她小, 所以

height = 8
width = distance from 8 to 3
      = (index of 3) - (index of 8)
      = 4 - 3 = 1
area = 8 * 1 = 8

再來我們發現, stack 最上面的 6 還是比 3 大, 所以

height = 6
width = distance from 6 to 3 = 4 - 2 = 2
area = 6 * 2 = 12

以此類推直到, 最後 stack = [1], 這時候我們在把 3 放進去 stack = [1, 3]
然後直到最後, 根據我們的例子, 當我們走完所有元素, stack = [1, 3, 4, 8]
這時候我們再來回過頭來計算剩下的部分.
透過事先將一個虛擬的元素 0 放到 height 的最後面來模擬 monotonic stack 被破壞的情況

height = 8
width = = (index of 0) - (index of 8) = 7 - 6 = 1
area = 8 * 1 = 8

height = 4
width = = (index of 0) - (index of 4) = 7 - 5 = 2
area = 4 * 2 = 8

height = 3
width = = (index of 0) - (index of 3) = 7 - 4 = 3
area = 3 * 3 = 9

height = 1
width = = (index of 0) - (index of 1) = 7 - 0 = 7
area = 1 * 7 = 7

如此一來 我們的 stack 最後就是空的, 而我們也算過
以每個 histogram 高度來看, 其最大的長方型的面積

---

### 304. Range Sum Query 2D - Immutable


### 1277. Count Square Submatrices with All Ones


### 213. House Robber II


### 740. Delete and Earn

本題看起來很複雜, 但轉換一下, 其實是跟 house robber 一樣的題目

大意如下
給定 list of int, 值可能重複出現, 例如 [2, 2, 3, 3, 3, 4]
並重複執行以下操作

1, 取出其中一值 i 並獲得 list 中, 並獲得 i 分
   但你必須刪除掉 list 中所有 i+1 以及 i-1 的數字
   例如 [2, 2, 3, 3, 3, 4] -> 取 3 -> 刪除所有 2 and 4
   剩下 [3, 3]　-> 重複取3 -> 重複取3 , 最後得到 9 分

可以理解成 每次拿分數 都要考慮要不要取這個數字,
而我們這個問題可以化簡為 [(2 * 2), (3 * 3), (4 * 1)]
當我們取 2 (\*2) 分, 就會失去  3(\*3) 分

以此我們可以先將 list of int 中所有同樣數字的總分算起來
points = [4, 9, 4], 然後問題就回歸到 House robber
要取第一個數字, 還是取第二個數字, 回歸成 DP 問題

```python
    prev1 = prev2 = 0
    for p in points:
        prev2, prev1 = prev1, max(prev2 + p, prev1)

    return max(prev1, prev2)
```

### 1143. Longest Common Subsequence

本題想法適用 2D dp table - bottom up

text1 = "abccde"; text2 = "ace"

```python
for idx1, char1 in enumerate(text1):
    for idx2, char2 in enumerate(text2):
        # 如果兩個字元一樣
        if char1 == char2:
            # 則目前 LCS 長度為 兩邊各減一個字元的時候的長度 + 1
            # 例如 "abcc" 的 "c" 跟 "ac" 的 "c" 一樣
            # 長度就是用 "abc" + "a" 的 LCS 長度 + 1
            # 這樣才能避免連續重複字元的問題
            dp[idx1 + 1][idx2 + 1]  = dp[idx1][idx2] + 1
        else:
            # 反之如果兩個字元不同
            # 例如 "abcc" 的 "c" 跟 "ace" 的 "e" 不一樣
            # 則要從
            #   1) LCS of "abcc" & "ac"
            #   2) LCS of "abc" & "ace"
            #   中挑一個比較長的, 也就是 LCS of "abcc" & "ac" = 1
            dp[idx1 + 1][idx2 + 1] = max(
                dp[idx1 + 1][idx2], dp[idx1][idx2 + 1]
            )
```

要注意的是 dp table 可以多一個第 0 維度, 這樣就可以避免多餘的邊緣處理

---

### 583. Delete Operation for Two Strings

本題看起來很囉唆 看其實是和 1143 很像的題目
> 找出最少要刪除幾個字才能讓兩個字串相同
其實也就是
> 找出最長(非連續)共通子序列, 然後再拿原字串長度減掉該共通子序列長度

例如 word1 = "sea", word2 = "eat"

LCS = "ea"
output = 2 = len("sea") + len("eat) - (2 * len("ea)) = 3 + 3 - 2 * 2

這樣就馬上解了

---

### 712. Minimum ASCII Delete Sum for Two Strings

本題也是 1143 的改造題目之一, 基本上跟 583 完全一樣
> 刪除某些字讓兩字串完全相同 且刪除某些字的總和 cost 要是最低的
也就是
> 找出所有可能的 LCS, 回傳其中沒有 matched 的部分的字元 cost 總和最低

例如  s1 = "delete", s2 = "leet"
LCS 包括了 eet, let, lee...等
計算 sum("delete) + sum("leet") - 2 * sum(LCS) for LCS from ALL_LCS
找出最小的就是了
實際上眼算法大概是dp table 是計算當前最大的 LCS cost 總和
最後的 dp[-1][-1] 就會是 LCS (which have maximum cost)
而這樣反過來理解就是就是最小的刪除 cost

```python
for row, char2 in enumerate(s2):
    for col, char1 in enumerate(s1):
        # 若字元相同
        if char1 == char2:
            # 增加新的字元的 cost
            dp[row+1][col+1] = (
                dp[row][col] + ord(char2)
            )
        else:
            # 選比較大的 cost
            dp[row+1][col+1] = max(
                dp[row][col+1],
                dp[row+1][col]
            )
```

---

### 718. Maximum Length of Repeated Subarray

這題跟 1143 也是超像
差別在於他要找的是連續的, 所以
1. dp table [i][j] 的意思就是
   > nums1[:i-1] 以及 nums2[:j-11] 兩者的最長連續重複子陣列
2. dp table 的預設值必須是 0, 表示最長連續重複子陣列長度是 0
3. 當字元不同時, 直接不更新, 其含意是最長連續重複子陣列長度就是 0
4. 要注意因為是要求連續, 所以 dp table[-1][-1] 不會是最大值
   簡單作法就是每次更新都檢查是否是目前最大值

```python
ret = 0
for row, num2 in enumerate(nums2):
    for col, num1 in enumerate(nums1):
        if num2 == num1:
            dp[row+1][col+1] = dp[row][col] + 1
            ret = max(ret, dp[row+1][col+1])

```

---

### 300. Longest Increasing Subsequence

這題雖然可以用 dp 解, 但最好的解法不是 dp
dp 解法是用 bottom up
用 dp array [i] 去紀錄到這個號碼 nums[0:i] 裡面最大的 LIS
而辦法也很簡單
```python
# 每個數字只考慮自己的情況下 最短 LIS 也會是 1
dp = [1 for _ in nums]
# 走過每個數字
for idx, n in enumerate(nums):
    # 檢查手上的數字前面, 有幾個小於自己
    cand = [dp[i] for i in range(idx) if nums[i] < n]
    # 只要有任何一個小於自己, 就找出裡面最長的LIS +1
    # 表示目前以前的 LIS, 配上自己可以形成一個更長的 LIS
    if cand:
        dp[idx] = max(cand) + 1
```

而更好的解法是很難描述
```python
# seq 就是最後答案, 先把第一個元素放進去
seq = [nums[0]]

# 走過第二個開始的所有元素
for n in nums[1:]:
    # 如果我遇到一個比最大元素還大的, 放進去
    if n > seq[-1]:
        seq.append(n)
    # 若非則
    else:
        # 找出這個元素應該放在seq 的哪個位子才合適
        i = 0
        while n > seq[i]:
            i += 1
        # 覆蓋掉
        seq[i] = n

return len(seq)
```
之所以可以這樣做是因為, 即便覆蓋掉了, LIS長度還是一樣的
```
The length remains correct because the length only changes when a new element is larger than any element in the subsequence. In that case, the element is appended to the subsequence instead of replacing an existing element.
```
```
[10,9,2,5,7,3,101,18]
>>> n = 10,   seq = [10]
>>> n = 9,    seq = [9]
>>> n = 2,    seq = [2]
>>> n = 5,    seq = [2, 5]
>>> n = 7,    seq = [2, 5, 7]
>>> n = 3,    seq = [2, 3, 7] # 注意這個 LIS 不存在, 但長度一樣, 不影響後續新增
>>> n = 101,  seq = [2, 3, 7, 101]
>>> n = 18,   seq = [2, 3, 7, 18] # 注意這個 LIS 不存在, 但長度一樣, 不影響後續新增
```
```
[1, 6, 7, 8, 2, 3, 4, 5]
>>> n = 1, seq = [1]
>>> n = 6, seq = [1, 6]
>>> n = 7, seq = [1, 6, 7]
>>> n = 8, seq = [1, 6, 7, 8]
>>> n = 2, seq = [1, 2, 7, 8]
>>> n = 3, seq = [1, 2, 3, 8]
>>> n = 4, seq = [1, 2, 3, 4]
>>> n = 5, seq = [1, 2, 3, 4, 5]
```
---

### 279. Perfect Squares

本題不難, 解法有 bfs & dp
有幾個小重點

1. 可使用的 完全平方數 必定 <= n ** 0.5 , 這個可以有效縮小搜尋空間
2. dp 時, 初始值可就直接設為 n, 代表 n 個 squares, 也就是全部拿 1 組成
3. dp 更新時, 假設目前是 i, 就是去找出 dp[i - n ** 2] for all available n 的最小值 + 1, 因為從這些數字只要加一個 n**2 就可以到 i

---

### 673. Number of Longest Increasing Subsequence (NLIS)

本題要從 300. LIS 這題的解法延伸

> 整理之後我發現跟 huahua 的解法很像, 而他把題目拆得更好, 可以看
[這個](https://www.youtube.com/watch?v=SFCiuIJu17Y&ab_channel=HuaHua)複習

先描述我的解法, 想法是這樣
使用兩個 dp table (dp_count, dp_len) 紀錄
> 以 nums[i] 為結尾時的 LIS 長度跟數量

實際上的算法會是

```python
candidate = Counter() # key: len, val: count

# 對所有 j which 0 < j < i
for j in range(i):
    # 如果 nums[j] < nums[i], 表示我可以把這個新的 nums[i] 接上去形成更長的 LIS,
    # dp_len[j] 就是以 nums[j] 結尾時 LIS 長度, 而 dp_count[j] 就是到底有幾種不同的 LIS
    # 這邊使用 Counter 紀錄不同長度的新 LIS 到底各有幾個
    if nums[i] > nums[j]:
        candidate[dp_len[j]+1] += dp_count[j]

    # 要注意也是有可能 nums[i] 比所有的 nums[j] 還小, 這樣 candidate 就會為空
    # 但只要非空, 就表示一定有以 nums[i] 結尾的更長的 LIS, 就要寫回去 dp[i]
    if candidate:
        dp_len[i] = max(candidate.keys())
        dp_count[i] = candidate[dp_len[i]]
```

當我們對所有元素都走過一次上述流程之後, 我們就
dp_len -> 以各元素為結尾的 LIS 長度
dp_count -> 以各元素為結尾的 LIS 有幾個

最後我們在只要用 max(dp_len), 找出長度為最長的 index
對應到 dp_count, 算個總和就好了

---

### 1048. Longest String Chain

這題也是 dp 解, 但有分 top-down | bottom up

核心概念是
給定一個 word, 我們先逐步拆解 word,
每個 word 的長度 == max(所有從 word 拆解出來的 subword 的 LSC) + 1
但如果 word 本身不存在於 words 的字就回傳 0

舉例來說 LSC(bda) -> max(LSC(bd), LSC(ba), LSC(da)) + 1

接著解釋 top-down 解法
```
words = ["bda","bdca","a","b","ba","bca"]

bda -> ba -> a
          -> b
    -> bd -> b(x)
          -> d
    -> da -> d(x)
          -> a(x)

LSC(a) = 1
LSC(b) = 1
LSC(d) = 0
LSC(ba) = 2 = max(LSC(a), LSC(b)) + 1 (ba in word)
LSC(bd) = 0 (bd not in words)
LSC(da) = 0 (da not in words)
LSC(bda) = 2 = max(LSC(ba), LSC(bd), LSC(da)) + 1 (bda in word)
```

而 bottom up 解法其實非常像
但重點在於要先從短字串開始解
只要這樣, 我們就不需要 DFS 走到最底部
因為短字串會先被全部看過
如果 dba -> db 不存在於 hash map, 那就表示他就是不存在於 words
從而減少非常多的 recursive

---

### 96. Unique Binary Search Trees

本題看起來很複雜, 其實很簡單

dp table 存的是 dp[i] == i 個 node 的排列方式數量

而更新方式的想法是
首先一個 BST, 左右 child 一定都是 BST
這表示給定 n 個 node, root 就有 n 種選擇
而左右 child 被分配的 node 也會被決定好
也就代表 child 有 dp[i] 種排列方式的 BST, 所以
```python
dp[0] = 1
dp[1] = 1
...
dp[n] = sum(
    dp[i] * dp[n-(i+1)]
    for i in range(n)
)
```

---

### 1105. Filling Bookcase Shelves

幹超難的, 這題也是 DP,

```python
# dp[i] means that the best ordering when ith book is put into shelf
# and the answer will be the minimum of
#     dp[i-1] + max height of i and i-1 th books (since we put them in the next layer)
#     dp[i-2] + max height of i ~ i-2 th books
#     ...
#     until we can't put a new book since the limitation of width
```

> dp[i] 存的是 當把第 i 本書放進書櫃時最好的(最矮)排列方式的高度

要注意這邊講得最好其實是最矮, 而這個 dp[i] 的求法是

> dp[i-1] + height[i] ->  前 0 ~ i-1 本書已經排好的情況下, 把第 i 本書放在新一層的高度
> dp[i-2] + max([height[i-1], height[i]] -> 前 0 ~ i-2 本書已經排好的情況下, 第 i-1 ~ i 本書放在新一層的高度
...
> 直到所有你選的書本的寬度超過題目寬度上限

當你選的書超過寬度上限時, 你就變成一定要放兩排, 舉例來說 當你選了最後5本書重新排列 其實已經剛好超過了寬度限制
這時候就會得放兩排, 但當你把第五本書的第一本放在新的一排的時候, 這個情況已經在之前的 dp 被考慮過了
> 如同 dp[i-1] + height[i] 的情況
所以即便真的這樣是最好的 算出來的結果也早就被考慮在 dp table 中, 所以只要看寬度限制內的就好
而當你這樣走過可能的 i 之後, 你就探究了所有可能, 然後取最小的值就是 dp[i]

要注意的是, 你要考慮的是高度, 最小的排法

```python
# 從總共有 i 本書開始的情境開始
for i in range(1, len(books) + 1):
    w = h = 0
    j = i - 1
    # j 的意思是 j 之前的書都被排列好了 也就是上面解釋的 i-1 開始
    # 只要寬度沒有超過上限就計算新的一層的高度, 跟已經排好的部分的高度加總, 找最小值
    while j >= 0 and (w := w + books[j][0]) <= shelfWidth:
        h = max(h, books[j][1])
        dp[i] = min(dp[i], dp[j] + h)
        j -= 1
```

---

### 131 Palindrome Partitioning


---

### 1139. Largest 1-Bordered Square


---
