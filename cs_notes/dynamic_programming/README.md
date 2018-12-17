#### [413. Arithmetic Slices](https://leetcode.com/problems/arithmetic-slices/description/) (Math, Dynamic Programming)
* 題目: 給一數列, 請回傳子數列中是等差數列之數量
* Example 1:
    ```
    A = [1, 2, 3, 4]

    return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
    ```
* 解法簡述:
    ```
    本題的最重要的是等差數列的增加規則, 等差數列最短至少要 3 個元素
    一個長度為 3 的等差數列, 如果又增加了一個元素且仍是等差數列
    則會額外增加 2 個不同的等差數列, 舉例
    [1, 2, 3] -> 等差數列有 [1, 2, 3]
    [1, 2 ,3 ,4] -> 等差數列有 [1, 2, 3], [2, 3, 4], [1, 2, 3, 4]
    [1, 2 ,3 ,4, 5] -> 等差數列有 
            [1, 2, 3], [2, 3, 4], [3, 4, 5],
            [1, 2, 3, 4], [2, 3, 4 ,5], [1, 2, 3, 4, 5]
    解析到此, 真正的解法就呼之欲出. 有兩種做法
    1) 公式解
        長度為 n 的等差數列, 其所有等差子數列之數量為 (n-1) * (n-2) / 2
        所以我們只要走過整個數列, 看看當前元素與前兩個元素是否為等差
        並記住等差數列的長度, 當發現不是, 就將長度帶入公式, 存到另一變數
        再繼續往後看, 重新計算長度.
    2) DP 解
        DP 的規律為
            長度=3, 數量=1
            長度=4, 數量=1+1=2
            長度=5, 數量=2+1=3
        所以 dp[i] 所代表的資訊就是, 到元素i為止的子陣列, 有多少個是等差數列
        所以我們只要檢查當前元素和前兩個元素是否為等差數列, 若是則
            dp[i] = dp[i-1]+1
        最後再將整個dp的值全部加起來即可
    ```
#### [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/description/) (Dynamic Programming)
* 題目: 給定一數字 ```n``` 表要爬的階梯數, 一次可以爬一階或兩階, 請問總共有多少種不同的爬法
* Example 1:
    ```
    Input: 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
    ```
* Example 2:
    ```
    Input: 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
    ```
* 解法簡述:
    ```
    本題是類似費伯納西數列之變化題
    要爬到第 n 階, 一定是從 n-1 階或是從 n-2 階
    要注意, 從 n-2 階往上爬到 n 階的時候, 只能是爬兩階, 否則跟從 n-1 階重複
    所以可以得出 
        dp(n) = dp(n-1) + dp(n-2) with dp(1) = 1, dp(2) = 2
    另外, 這題當然可以用遞迴解.
    ```
#### [198. House Robber](https://leetcode.com/problems/house-robber/description/) (Dynamic Programming)
* 題目: 給定一數列表示不同房子中的財產價值, 若是搶了連續兩間屋子會觸發警報, 在不出觸發警報的前提下, 請問最多可以搶到多少錢
* Example 1:
    ```
    Input: [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
                Total amount you can rob = 1 + 3 = 4.
    ```
* Example 2:
    ```
    Input: [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
                Total amount you can rob = 2 + 9 + 1 = 12.
    ```
* 解法簡述:
    ```
    本題是類似費伯納西數列之變化題
    能夠搶第 n 間的前提是不搶第 n-1 間
    所以要衡量的是 dp(n-1) 以及 dp(n-2)+n, 因此規則是
        dp(n) = max(dp(n-1), dp(n-2)+n)
    ```
#### [213. House Robber II](https://leetcode.com/problems/house-robber-ii/description/) (Dynamic Programming)
* 題目: 除了上一題原先的規則外, 這次房子是首尾相接的環型設計, 所以搶第一間就不能搶最後一間. 同問最多可以搶多少錢
* Example 1:
    ```
    Input: [2,3,2]
    Output: 3
    Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
                because they are adjacent houses.
    ```
* Example 2:
    ```
    Input: [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
                Total amount you can rob = 1 + 3 = 4.
    ```
* 解法簡述:
    ```
    這題不需要額外思考規則, 只要動點巧思就好
    狀況可以分成兩種
    1) 搶第 1 家 - 倒數第 2 家
    2) 搶第 2 家 - 倒數第 1 家
    所以函數可以維持不變, 只要呼叫兩次傳入不同範圍的 nums 就好
    答案是 max(house_rob(nums[:-1]), house_rob(nums[1:])) , 取兩者中的較大者
    ```
#### [873. Length of Longest Fibonacci Subsequence](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/) (Array, Dynamic Programming)
* 題目: 
* Example 1:
    ```
    Input: [1,2,3,4,5,6,7,8]
    Output: 5
    Explanation:
    The longest subsequence that is fibonacci-like: [1,2,3,5,8].
    ```
* Example 2:
    ```
    Input: [1,3,7,11,12,14,18]
    Output: 3
    Explanation:
    The longest subsequence that is fibonacci-like:
    [1,11,12], [3,11,14] or [7,11,18].
    ```
* 解法簡述:
    ```
    本題使用動態規劃，整體算法的流程如下
    1) 建立一個字典方便查閱某個數字是否在 A 之中以及如果該元素在 A 中, 其 index 是多少
    2) 建立 n*n 的 dp array, 定義是從 ith - jth 是多長的費伯納西數列, 預設值為 2
    3) 用雙重迴圈走過所有 j = (0 ~ n-1), k = (j+1 ~ n-1)
    這邊的想法是檢查是否有一元素 i 可以跟 j, k 三個元素構成一費伯納西數列
    同時對 i 元素的限制是 i < j < k, 由於我們已經知道 j 跟 k 的數值
    所以可以推算出 i 的數值是多少，這時候就要做兩個檢查
    a ) A[k]-A[j] in dictionary
    b ) A[k]-A[j] < A[j]
    如果上述兩個條件都有符合，就表示 j, k 是可以和元素 i 構築出費伯納西數列
    當我們更新的時候要注意，必須檢查 i, j 是否可以跟一個更小的元素建構費伯納西數列
    也就是 dp[i][j] 的值，但這個值按照設計，必定會先在之前的迴圈中被更新
    所以我們可以直接更新成 dp[j][k] = dp[i][j]+1, 假若 i, j, k 是第一次被更新的費伯納西數列
    那麼值就會是 2 + 1 也就是長度為 3 的費伯納西數列.
    最後使用一個額外的變數紀錄所看過的最大的數列長度, 最後進行回傳
    ```
#### [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/description/) (Binary Search, Dynamic Programming)
* 題目: 給定一數列, 請回傳其中最長的遞增子數列之長度
* Example 1:
    ```
    Input: [10,9,2,5,3,7,101,18]
    Output: 4 
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
    ```
* 解法簡述:
    ```
    我的作法是用 dp 紀錄以元素i為起點的最長遞增子數列之長度
    每往回走一步就要檢查之前所有的元素的 dp
    找出所有比當前元素還要大的元素所對應之dp中最大值並+1
    最後回傳整個過程中看過最大的值
    實際上有 O(nlogn) 的解法, 可以看備註連結
    ```
* 備註: 
    * [O(nlogn)解法](https://github.com/CyC2018/CS-Notes/blob/master/notes/Leetcode%20%E9%A2%98%E8%A7%A3.md#%E6%9C%80%E9%95%BF%E9%80%92%E5%A2%9E%E5%AD%90%E5%BA%8F%E5%88%97)

#### [718. Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/) (Array, Hash Table, Binary Search, Dynamic Programming)
* 題目: 給兩整數陣列 ```A``` 及 ```B```, 請回傳兩陣列中最長的重複子陣列之長度.
* Example 1:
    ```
    Input:
    A: [1,2,3,2,1]
    B: [3,2,1,4,7]
    Output: 3
    Explanation: 
    The repeated subarray with maximum length is [3, 2, 1].
    ```
* 解法簡述:
    ```
    本題要使用二維 dp, 大小維 len(A)+1 * len(B)+1, 預設值為 0
    而 dp[i][j] 代表的是 A[i], B[j] 兩個子陣列的最長重複子陣列
    +1 是為了不需要特別去檢查目前是否為邊界, 例如
        if i > 0 and j > 0: dp[i][j] += dp[i-1][j-1]
    實際的想法如下:
    用 i 代表目前正在看 A 的位置; 用 j 代表目前正在看 B 的位置
    如果 A[i] == B[j] 就表示當前兩字串中分別在 i, j 的位子是一樣的字母, 所以可以確定 
        if A[i] == B[j]: dp[i][j] += 1
    但這樣沒辦法知道 A[i], B[j] 之後的狀況如 i-1:j-1, i-2:j-2, 所以要用
        if A[i] == B[j]: dp[i][j] = dp[i-1][j+1] + 1
    這樣就可以確保我們有正確記錄到最長的共通字串
    最後因為我們初始化 dp 時有額外 +1 層所以不需要特別去處理邊界的狀況, 因此我們的迴圈會是
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1)
            # 要注意我們只有在 dp 上面多加一層, 所以將 i, j 用在 A, B 的時候要 -1
            if A[i-1]==B[j-1]:            
                dp[i][j] = dp[i-1][j-1]+1
    收尾有 3 種做法
    1) 是在每更新一次 dp[i][j] 都檢查當前值是否為最大值
    2) 是最後一次找出整個 dp 中的最大值
    3) 在更新過程中, 如遇到 A[i-1]!=B[j-1], 則將 dp[i][j]=max(dp[i-1][j], dp[i][j-1])
       如此一來, dp[len(A)][len(B)] 定為最大值
    ```
#### [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/description/) (Array, Dynamic Programming)
* 題目: 給一非負整數陣列, 找出一條路徑從左上走到右下, 並使經過的數字之總和儘可能地小. 注意, 每次都只能往右或往下走
* Example 1:
    ```
    Input:
    [
    [1,3,1],
    [1,5,1],
    [4,2,1]
    ]
    Output: 7
    Explanation: Because the path 1→3→1→1→1 minimizes the sum.
    ```
* 解法簡述:
    ```
    本題想法如下
    使用一維 dp 去紀錄並以橫排為單位來更新走到橫排中特定位子所需要的最小步數
    以 example 1 為例
    當我走到 1st row -> 需要的最小步數就一定是 [1, 1+3, 1+3+1] = [1, 4, 5]
    當我走到 2ed row, 狀況就開始比較複雜
    第一格的值一定是上一層同排的加上自己 = 1+1 = 2, 所以我們知道現在會是 [2, ?, ?]
    第二格只能從上排第二格或是當排第一格走來, 而我們要取最小, 
    所以會是 min(2, 4) + 5, 得出 7. 所以現在會是 [2, 7, ?]
    第三格的規則和第二格一樣, 會是 min(7, 5) + 1 得出 6
    因此我們算出了 要走到第二排的每個位子的最小值會是 [2, 7, 6]
    如此我們就可以歸納出規則, 以下以 i 代表 row, 以 j 代表 column
    若 i == 0, 則 dp[j] = [sum(nums[i][:j+1])] 表當前位子左側所有值加總, 也就是只往右走
    若 i > 0 但 j == 0, 則 dp[j] = dp[j] + nums[i][j], 表當前位子往下走, 上一格的值加上當前位子值
    若 i > 0 且 j > 0, 則 dp[j] = min(dp[j-1], dp[j]) + nums[i][j], 因為此時 dp[j-1] 一定已經更新過了
        所以其所代表的意思為當前排的前一格的最小值
        但 d[j] 還沒更新, 所以其意思會是同一格上一排的最小值, 
        比較這兩者所代表的意思就是 從上往下走 跟 從左往右走 哪個比較小
        當然最後還是要加上當前格子的值 nums[i][j]
    最後當所有的 row 都走完了, dp[-1] 就是最左下的最小路徑總和的走法
    ```
#### [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/description/) (Dynamic Programming)
* 題目: 給定一長度為 n 之數組, 請設計一個函數可以回傳兩 index 間的數值總和
* Example 1:
    ```
    Given nums = [-2, 0, 3, -5, 2, -1]

    sumRange(0, 2) -> 1
    sumRange(2, 5) -> -1
    sumRange(0, 5) -> -3
    ```
* 解法簡述:
    ```
    題目特別要求因為這個函數會被多次使用, 所以將結果存下來會是比較好的做法
    本題核心想法是 sumRange(2, 4) = sumRange(0, 4) - sumRange(0, 1), 
    所以不需要每次都重複計算, 以下做法基於上述想法
    首先我們用一維 dp 將 sum(0, 0) 到 sum(0, n)存起來, 長度會是 n+1
    其中 dp[0] = sumRange(0, 0), dp[n] = sumRange(0, n)
    接著當被呼叫 sumRange(i, j) 的時候, 只要回傳 dp[j+1]-dp[i] 就好
    要注意, 題目中呼叫 sumRange 時, 其座標是以 0 為基準
    所以 sumRange(3, 5) 其實是第 4 及第 6 個元素
    也就是 dp[6] - dp[3] = dp[5+1]-dp[3], 所以是 dp[j+1]-dp[i]
    ```
#### [96. Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/description/) (Tree, Dynamic Programming)
* 題目: 給一正整數 ```n```, 請回答若使用 ```[1, ..., n]``` 作為輸入, 最多可以建立出多少種不同的 Binary Search Tree
* Example 1:
    ```
    Input: 3
    Output: 5
    Explanation:
    Given n = 3, there are a total of 5 unique BST's:

    1         3     3      2      1
     \       /     /      / \      \
      3     2     1      1   3      2
     /     /       \                 \
    2     1         2                 3
    ```
* 解法簡述:
    ```
    樹的問題的突破口很多都是在解析子樹的狀態
    這題的重點在於選定了某個數值作為 root 之後
    其左右子樹的深度就已經被決定了
    例如 n = 4, 則 root val 必定在 [1, 2, 3, 4] 之間
    假若選定 root.val = 1, 則其左子樹為 None
    而右子樹則的數量則是一個 n=3 子問題, 也就是繼續從 [2, 3, 4] 之間再選一個 root
    所以 n=4 可以拆成
        root.val = 1, left = [] (n = 0),        right = [2, 3, 4] (n = 3)
        root.val = 2, left = [1] (n = 1),       right = [3, 4] (n = 2)
        root.val = 3, left = [1, 2] (n = 2),    right = [4] (n = 1)
        root.val = 4, left = [1, 2, 3] (n = 3), right = [] (n = 0)
    而左右子樹的子問題完全獨立，所以左右子樹的數量相乘之後就是所有可能的左右子樹種類
    所以答案會變成
        dp[4] = dp[0]*dp[3] + dp[1]*dp[2] + dp[2]*dp[1] + dp[3]*dp[0]
    ```
#### [62. Unique Paths](https://leetcode.com/problems/unique-paths/description/) ()

* 題目: 給一陣列, 在只能往右或往下走的前提下, 請問從左上走到右下總共有多少種不同的走法
* Example 1:
    ```
    Input: m = 3, n = 2
    Output: 3
    Explanation:
    From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Right -> Down
    2. Right -> Down -> Right
    3. Down -> Right -> Right
    ```
* Example 2:
    ```
    Input: m = 7, n = 3
    Output: 28
    ```
* 解法簡述:
    ```
    本題解法和 64. Minimum Path Sum 非常相似
    我們針對每個 row 來計算, 要走到當前 row 的特定位置上, 到底有幾種走法
    以下以 i 表 row, 以 j 表 column, 用一維 dp 來記錄走到某一行的特定位置上的走法數量
    首先, 只要 j == 0, dp[j] = 1, 因為只能往右或往下走, 所以 j == 0, 一定是從上往下走的單一走法
    接著, 只要 i == 0, dp[j] = dp[j-1] 你只會是從最左邊往右邊走的單一走法
    此外的所有狀況, dp[j] = dp[j-1] + dp[j], 因為此時 dp[j-1] 一定已經更新過了
        所以其所代表的意思為左邊格子的走法數量
        但 d[j] 還沒更新, 所以其代表會是上一排同一格的走法數量, 
        而當前格子的走法數量, 就是從左往右走跟從上往下走的加總,
        所以會是 dp[j] = dp[j-1] + dp[j]
        另外, 因為 dp 初始值是 0 , 所以其實 i==0 或 i!=0 都可以套用這個公式
    最後回傳 dp[-1] 就是答案了
    ```

#### [322. Coin Change](https://leetcode.com/problems/coin-change/description/) (Dynamic Programming)
* 題目: 給一金錢總量及不同額度的硬幣, 請問最少要花多少枚硬幣才能湊到金錢總量
* Example 1:
    ```
    Input: coins = [1, 2, 5], amount = 11
    Output: 3 
    Explanation: 11 = 5 + 5 + 1
    ```
* Example 2:
    ```
    Input: coins = [2], amount = 3
    Output: -1
    ```
* 解法簡述:
    ```
    本題想法很簡單, 從 1 塊錢 -> amount 塊錢來算最少要花多少硬幣
    先假設 amount = 11, 錢幣種類有 [1, 2, 5]
    所以可以知道, 若要將 11 塊往下分, 一定只有
    1) 5 塊硬幣 + 剩下 7 塊
    2) 2 塊硬幣 + 剩下 9 塊
    3) 1 塊硬幣 + 剩下 10 塊
    也就是說我們必須只要知道 7, 9, 10 塊最少只需要多少枚硬幣, 就可以知道答案
    但這三者分別也都可以往下拓展, 所以我們要從一塊錢開始往上推
    首先 dp 長度為 11+1, dp[0]設0, 對所有錢的大小我們都去檢查, 舉例來說
    1 塊錢 : 1 枚 1 塊 -> dp[1] = 1, 2塊錢跟5塊錢太大了
    2 塊錢 : 
        1 枚 1 塊 + 剩下 1 塊錢 -> dp[1] + 1 = 2 枚
        1 枚 2 塊 -> 1 枚
        1 枚 5 塊太大了
        所以得出 dp[2] = min(dp[1]+1, dp[2]) 也就是 1 枚
    所以規則會是
    對 1-n 塊錢, 都去檢查用所有貨幣扣掉之後最少要多少枚, 這樣就會知道當前的錢最少可以用多少枚
    然後不斷往上更新直到 n 就可以回傳 dp[n]
    ```
#### [518. Coin Change 2](https://leetcode.com/problems/coin-change-2/description/) (Dynamic Programming)
* 題目: 給一金錢總量及不同額度的硬幣, 請問總共有多少種不同的組合方式以湊足給定的金錢總量
* Example 1:
    ```
    Input: amount = 5, coins = [1, 2, 5]
    Output: 4
    Explanation: there are four ways to make up the amount:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1
    ```
* Example 2:
    ```
    Input: amount = 3, coins = [2]
    Output: 0
    Explanation: the amount of 3 cannot be made up just with coins of 2.
    ```
* Example 3:
    ```
    Input: amount = 10, coins = [10] 
    Output: 1
    ```
* 解法簡述:
    ```
    本題和 322. Coin Change 是類似題, 不同的是本次不問最少枚數
    而是要求你算出總共有幾種不同的組法
    這邊要求不同就隱含著順序的問題
    也就是 '2+1+1' 跟 '1+2+1' 跟 '1+1+2' 是一樣的組法
    本題有兩種解法
    1) DP
    2) DFS
    DP解法架構和 322 非常相似
    但在本題設計上, 雙迴圈的順序是非常重要, 必須是先根據錢種來迴圈
    如果先根據金額量來迴圈, 就會發生上面提到的重複問題
    舉例來說, 目標金額是 3, 金幣只有 [1, 2]
    所以應該只有3種方法 [1, 1, 1, 1], [1, 1, 2], [2, 2]
    但如果先從金額開始算(以下公式使用 dp[i] += dp[i-coin])
        dp[1] = 1 [1]
        dp[2] = 2 [1, 1], [2]
        dp[3] = 3 [1, 2], [1, 1, 1], [2, 1]
    可以看到 [1, 2] 和 [2, 1] 就會重複, 但如果先根據錢種的話
        Coin = 1
            dp[1] = 1, [1]
            dp[2] = 1, [1, 1]
            dp[3] = 1, [1, 1, 1]
        Coin = 2
            dp[1] = 1 + 0
            dp[2] = 1 + 1, [2]
            dp[3] = 1 + 1, [2, 1]
    所以順序非常重要, 其目的在於避免混亂的錢幣大小順序影響計算數量
    DFS解法可以想想 Backtracking, 想法並不難
    ```
#### [279. Perfect Squares](https://leetcode.com/problems/perfect-squares/description/) (Math, BFS, Dynamic Programming)
* 題目: 給一正整數, 請問最少要用多少個完全平方數如 ```1, 4, 9, 16...``` 才能湊出給定之正整數
* Example 1:
    ```
    Input: n = 12
    Output: 3 
    Explanation: 12 = 4 + 4 + 4.
    ```
* Example 2:
    ```
    Input: n = 13
    Output: 2
    Explanation: 13 = 4 + 9.
    ```
* 解法簡述:
    ```
    這題有兩種解法, DP or BFS
    首先不管哪個算法, 都可以先用 n 推算出可能使用到的完全平方數
    完全平方數的上限就一定是 int(sqrt(n)) ** 2
    例如 n = 15 可能會用到的就只有 [1, 4, 9]
    1) BFS 的作法
        首先將 15 放在 queue 中
        然後呼叫一 boolean 陣列來記錄 1~15 那些元素已經拜訪過了
        接著每次迴圈都把目前 queue 中所有元素 pop 出去
        要注意是目前, 因為過程中我們還會加東西進去, 所以我們要用數量控制 pop() 
        接著對所有可能的完全平方數 [1, 4, 9]
        把 15-9, 15-4, 15-1 放入 queue, 接著更新 boolean 陣列
        然後就可以進去第二迴圈, 再次進行一樣的操作直到我們走到 0
        要注意如果當前值減去可能使用的完全平方數是負值, 就跳過不放進 queue
        記得我們是要回傳數量, 所以迴圈要用另外一個變數紀錄這是第幾迴圈, 最後跳出迴圈時回傳該值
    2) DP 的作法
        呼叫一維 dp 陣列, 長度為 16 (index 從 0 ~ 15) 初始值就是 0 ~ 15(對應最糟情況就是用 1 湊出該數)
        後續作法跟 322. Coin Change 雷同
        假設我需要湊出 15, 可能的完全平方數就是 [1, 4, 9]
        所以我要查看的就只有
            dp[15] = min(dp[15-9], dp[15-4], dp[15-1]) + 1
        但是可以看到我們要先從小開始建立dp的對應值, 所以
            dp[1] = min(dp[1-1]) + 1
            ...
            dp[4] = min(dp[4-4], dp[4-1]) + 1
            ...
            dp[9] = min(dp[9-9], dp[9-4], dp[9-1]) + 1
        如此一來, 最後就回傳 dp[-1] 就好
    ```
#### [343. Integer Break](https://leetcode.com/problems/integer-break/description/) (Math, Dynamic Programming)
* 題目: 給一正整數 n, 請將其拆成最少兩個正整數並確保其拆出數字的乘積最大.
* Example 1:
    ```
    Input: 2
    Output: 1
    Explanation: 2 = 1 + 1, 1 × 1 = 1.
    ```
* Example 2:
    ```
    Input: 10
    Output: 36
    Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
    ```
* 解法簡述:
    ```
    本題有兩種解法, DP / Math
    先講 DP
    首先定義一維 dp 陣列, 長度為 n+1, 範圍是 0~n
    其含義 dp[i] 表示元素 i 的最好切法 / 最大乘積
    假設我今天要切 dp[6], 一定是從以下幾種切法找出來
        max(1 or dp[1]) * max(5 or dp[5])
        max(2 or dp[2]) * max(4 or dp[4])
        max(3 or dp[3]) * max(3 or dp[3])
    這樣涵蓋了所有的切法, 比較 max(i or dp[i]) 的用意是也有可能不往下切比較大
    例如 2 or dp[2] 是 2 比較大
    這邊我們可以先算的就是 dp[0]=0, dp[1]=0, dp[2]=1,
    後續就可以用迴圈走過 1-n 就算出來了
    第二種做法是 Math, 根據觀察可以發現
    除了 1 -> 0, 2 -> 1, 3 -> 2, 4 -> 4,
    5 -> 3 * 2, 6 -> 3 * 3, 7 -> 3 * 4
    8 -> 3 * 3 * 2, 9 -> 3 * 3 * 3, 10 -> 3 * 3 * 4
    後續都會照這個規則, 雖沒有證明但是是對的.
    ```
#### [338. Counting Bits](https://leetcode.com/problems/counting-bits/description/) (Bit Manipulation, Dynamic Programming)
* 題目: 給一數字 n, 請回傳從 0 - n 之間所有數字在二進位制底下出現的 1 的數量
* Example 1:
    ```
    Input: 2
    Output: [0,1,1]
    ```
* Example 2:
    ```
    Input: 5
    Output: [0,1,1,2,1,2]
    ```
* 解法簡述:
    ```
    首先本題 DP 的規律是最關鍵的部分, 舉幾個例子
    10 = 1010, 5 = 101
    7  =  111, 3 = 11
    可以發現 n//2 和 n 除了最後一個 bit 以外都是一樣的
    所以 dp[n] = dp[n//2] + n&1 就可以了
    ```
#### [646. Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/description/) (Dynamic Programming)
* 題目: 給 n 組數對, 若兩數對中, 一者的第二個數小於另一的第一個數, 則可成為 chain, 試問最長的 chain 長度多少
* Example 1:
    ```
    Input: [[1,2], [2,3], [3,4]]
    Output: 2
    Explanation: The longest chain is [1,2] -> [3,4]
    ```
* 解法簡述:
    ```
    本題首先要排序, 用 pairs[1] 排序
    此外, 先想到用 dp 從後往前解
    dp[i] 代表以元素 i 為起點的最長 chain 之長度
    更新方式也很直覺, i 之後的任一者 j, 只要 j[0] > i[1], 就表示 i 可以接在 j 前面形成一個 chain
    故 dp[i] = max(dp[j] for all j if j[0] > i[1])
    後來發現可以使用 greedy 的方式解, 一樣先排序
    接著用 stack 或是 end 紀錄
    如果是 stack 就檢查新元素的頭有沒有比 stack 最上面的值的尾巴還大, 有就加進去
    如果是 end 就檢查新元素的頭有沒有比 end 還大, 有的話就更新 end 為新元素的 end, counter +1
    最後回傳 len(stack) or counter 就好
    ```

#### [376. Wiggle Subsequence](https://leetcode.com/problems/wiggle-subsequence/description/) (Dynamic Programming, Greedy)
* 題目: 給一數列, 請找出最長的連續上下震盪數列 (請看範例)
* Example 1:
    ```
    Input: [1,7,4,9,2,5]
    Output: 6
    Explanation: The entire sequence is a wiggle sequence.
    ```
* Example 2:
    ```
    Input: [1,17,5,10,13,15,10,5,16,8]
    Output: 7
    Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
    ```
* Example 2:
    ```
    Input: [1,2,3,4,5,6,7,8,9]
    Output: 2
    ```
* 解法簡述:
    ```
    這題解法有四個階段
    1) 暴力解
    2) O(n**2) / O(n) DP
    3) O(n) / O(n) DP
    4) O(n) / O(1) Greedy DP
    比較重要的是第二種方法
    這邊要用兩個一維 DP 陣列, 下稱 up, down
    up[i]紀錄的是到 i 元素為止最長的震盪數列長度, 且元素 i 必須是上升的
    down[i]紀錄的是到 i 元素為止最長的震盪數列長度, 且元素 i 必須是下降的
    而兩者更新方式類似, 
    在 nums[i] > nums[j] 的前提下才可以更新up[i], 
    更新時要去檢查之前所有的 down[j] for j = 0~i 
    然後找出最大的, 也就是 up[i] = max(down[j] for j in [0..j] if nums[i]>nums[j])
    而 donw[i] 則是  = max(up[j] for j in [0..j] if nums[i]<nums[j])
    最後就回傳 max(down[-1], up[-1]) + 1, 因為這邊只記錄了上下震盪的次數而已, 長度要 + 1
    而後續的改善中, 階段3 是根據這個想法 - 如果比較 nums[i-1] 跟 nums[i], 只會有三種可能
        a) nums[i-1] > nums[i], 這表示 nums[i] 是上升, nums[i-1]處於下降
            所以 up[i] = down[i-1]+1 而 down[i] = down[i-1]
        b) nums[i-1] < nums[i], 這表示 nums[i] 是下降, nums[i-1]處於上升
            所以 down[i] = up[i-1]+1 而 up[i] = up[i-1]
        c) nums[i-1] == nums[i], 這表示不上升也不下降
            所以 up[i] = up[i-1] 而 down[i] = down[i-1]
    所以每次更新只需要看前一個, 不需要去往回看全部的
    階段 4 則是因為每次更新只需要看前一個, 所以可以將 up 和 down 當成變數就好    
    ```

#### 
* 題目:
* Example 1:
    ```
    ```
* Example 2:
    ```
    ```
* 解法簡述:
    ```
    ```