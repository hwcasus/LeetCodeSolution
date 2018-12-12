#### [870. Advantage Shuffle](https://leetcode.com/problems/advantage-shuffle/description/) (Array, Greedy, Two Pointers) 
* 題目: 給 A, B 兩個 List, 請重新排序 A 使其的每個元素都盡可能大於同位子之 B 的元素
* Example 1:
    ```
    Input: A = [2,7,11,15], B = [1,10,4,11]
    Output: [2,11,7,15]
    ```
* Example 2:
    ```
    Input: A = [12,24,8,32], B = [13,25,32,11]
    Output: [24,32,8,12]
    ```
* 解法簡述:
    1. 將 A 從大到小排序
    2. 令 C 為新陣列, 其內容為 ```[0, ..., len(B)-1]```, 並根據 B 的值從大到小排序
    3. 從頭檢索 C 的每個元素 ```C[i]``` 並與 ```max(A)``` 做比較
        1. 如果 ```B[C[i]] >= max(A)```, 則將 ```min(A)``` 也就是 ```A[-1]``` 取出放在 ```C[i]``` 的位置
        2. 如果 ```B[C[i]] < max(A)```, 則將 ```max(A)``` 也就是 ```A[0]``` 取出放在 ```C[i]``` 的位置

#### [565. Array Nesting](https://leetcode.com/problems/array-nesting/) (Array)
* 題目: 有點麻煩，請看 [LeetCode](https://leetcode.com/problems/array-nesting/)
* Example 1:
    ```
    Input: A = [5,4,0,3,1,6,2]
    Output: 4
    Explanation: 
    A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

    One of the longest S[K]:
    S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
    ```
* 解法簡述: 
    1. 對陣列中每個元素都
        1. 走完跟他連接的所有數字走過的數字就改為 -1 並紀錄目前走過的長度
    2. 每走完一個元素就檢查這次走的長度是不是最長的，如果是就更新
    3. 回傳最長的長度。

#### [954. Array of Doubled Pairs](https://leetcode.com/problems/array-of-doubled-pairs/description/) (Array, Hash Table)
* 題目: 給一陣列 A, 請回答是否能將其元素兩兩配對且每對元素都是 (n, 2n) 的倍數關係
* Example 1:
    ```
    Input: [3,1,3,6]
    Output: false
    ```
* Example 2:
    ```
    Input: [2,1,2,6]
    Output: false
    ```
* Example 3:
    ```
    Input: [4,-2,2,-4]
    Output: true
    Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
    ```
* Example 4:
    ```
    Input: [1,2,4,16,8,4]
    Output: false
    ```
* 解法簡述: 
    1. 根據 A 建立一字典 D, 其內容為 ```Key = A[i], Value = A.Count(A[i)```
    2. 先將 A 根據每個元素的絕對值從小到大排序
    3. 對 A 的每個元素 ```A[i]```
        1. 在字典 D 中尋找是否存在 ```Key = 2 * A[i]``` 且其值 > 0
           如存在則將 ```D[A[i]]``` 及 ```D[A[i]*2]``` 出現次數 -1
    4. 回傳是否整個字典 D 中所有 Key 所對應之 Value 皆為 0 (所有數字都被用光)

#### [697. Degree of an Array](https://leetcode.com/problems/degree-of-an-array/description/) (Array)
* 題目: 給一非空陣列 ```nums```, 其 ```degree``` 代表該陣列中出現最多次元素之次數, 請回傳在```degree```維持不變的情況下，其子陣列之可能最短長度
* Example 1:
    ```
    Input: [1, 2, 2, 3, 1]
    Output: 2
    Explanation: 
    The input array has a degree of 2 because both elements 1 and 2 appear twice.
    Of the subarrays that have the same degree:
    [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
    The shortest length is 2. So return 2.
    ```
* Example 2:
    ```
    Input: [1,2,2,3,1,4,2]
    Output: 6
    ```
* 解法簡述: 
    1. 先計算 ```nums``` 中所有元素的出現次數並將出現次數最多的元素放在另一陣列 ```candidates```
    2. 對 ```candidates``` 中的元素, 找到在 ```nums``` 中第一次及最後一次出現的位子並計算長度
    3. 回傳找到最長的長度

#### [442. Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/description/) (Array)
* 題目: 給一陣列 ```nums```, 其長度為 n 且值介於 ```1 ~ n```, 其中部分元素出現兩次, 請回傳出現次數為 2 的元素

* Example 1:
    ```
    Input:
    [4,3,2,7,8,2,3,1]

    Output:
    [2,3]
    ```

* 解法簡述: 
    * 提示:  ```nums``` 的每個元素 ```n``` 都可以對應到 ```nums``` 的特定位置上
    1. 走過 ```nums``` 的每個元素 ```n```, 令 ```idx = abs(n) - 1```
        1. 如果 ```nums[idx] > 0```, 則 ```nums[idx] = -nums[idx]```
        2. 如果 ```nums[idx] < 0```, 則將 ```abs(n)``` 存至另一陣列 ```ret```
    2. 回傳 ```ret```


#### [448. Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/) (Array)
* 題目: 給一陣列 ```nums```, 其長度為 n 且值介於 ```1 ~ n```, 其中部分元素出現兩次, 請找出所有介於 ```1 ~ n``` 但沒有出現在 ```nums``` 的元素
* Example 1:
    ```
    Input:
    [4,3,2,7,8,2,3,1]

    Output:
    [5,6]
    ```
* 解法簡述: 
    1. 作法與上題雷同, 對 ```nums``` 中的所有元素 ```n```, 令 ```idx = abs(n) - 1```
        1. 如果 ```nums[idx] > 0```, 則 ```nums[idx] = -nums[idx]```
    
    2. 回傳所有 ```nums``` 的元素中大於 0 的元素的位置 + 1

#### [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/description/) (Array, Two Pointers, Binary Search)
* 題目: 給一陣列 ```nums```, 長度為 ```n + 1```, 其所有元素都介於 ``` 1 ~ n ```之間, 其中有一個且只有一個元素重複，請找出該重複元素之值
* Example 1:
    ```
    Input: [1,3,4,2,2]
    Output: 2
    ```
* Example 2:
    ```
    Input: [3,1,3,4,2]
    Output: 3
    ```
* 解法簡述:
    1. 可以將上述圖題目看做一 Linked List, 其值表示指向第幾個 index
    2. 剩下解法完全與 [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) 一致

#### [926. Flip String to Monotone Increasing](https://leetcode.com/problems/flip-string-to-monotone-increasing/description/) (Array)
* 題目: 給一字串 ```S```, 其中只包含 ```0``` 及 ```1```, 請回傳若要將```S```轉為單調遞增最少需要更動幾個字元
* Example 1:
    ```
    Input: "00110"
    Output: 1
    Explanation: We flip the last digit to get 00111.
    ```
* Example 2:
    ```
    Input: "010110"
    Output: 2
    Explanation: We flip to get 011111, or alternatively 000111.
    ```
* Example 3:
    ```
    Input: "00011000"
    Output: 2
    Explanation: We flip to get 00000000.
    ```

* 解法簡述:
    ```
    這個解法的想法是，最終我們希望S變成以下三種狀況之一
    1) 全都 1
    2) 全都 0
    3) 從某個元素開始，前面全都 0, 後面全都 1
    先討論 3), 假設我們要從第 i 個元素開始把 S 翻成 ith 前面全都 0, ith 後面全都1
    而從 i 開始翻的次數必然是取決於 `i 前面有多少個 1` + `i 後面有多少個 0`
    所以下面我們使用 zs(zeroes) 及 os(ones) 來紀錄, 這兩個陣列長度都是 len(S)+1,
    zs[i]負責記錄在 ith 之後還有幾個0; os[i]則記錄 ith 之前有多少個 1, 紀錄完之後
    zs[1] 就表示第一個元素後面全都翻成1 要翻多少次, 其實也就是 (1) <---好像怪怪的
    而 os[-1] 就表示最後一個元素前面全都翻成0 要翻多少次, 其實也就是 (2)
    所以只要把這個 zs, os 相加的最小值找出來後, 再比較三者的最小值, 就可以取得答案了
    ```

#### [55. Jump Game](https://leetcode.com/problems/jump-game/description/) (Array, Greedy)
* 題目: 給一非負整數陣列 ```nums```, 陣列中的值表示最遠的跳躍距離, 請回答是否本陣列是否有辦法從起點跳到尾端.
* Example 1:
    ```
    Input: [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
    ```
* Example 2:
    ```
    Input: [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum
                jump length is 0, which makes it impossible to reach the last index.
    ```
* 解法簡述:
    ```
    這個做法的想法是從終點往回看每一個格子是不是有機會走到終點
    如果有機會，就將令 p 紀錄那個位子
    然後再繼續往回看每一個剩下的格子能不能走到更新後的 p
    如果到最後 p 點被更新到 0, 也就是起點
    就表示這個是可以從起點走到終點的, 所以最後是回傳 p == 0
    ```

#### [378. Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/) (Binary Search, Heap)
* 題目: 給一陣列 ```matrix```, 其每一行每一列都是從小到大遞增, 請找出當中第 ```k``` 大的元素
* Example 1:
    ```
    matrix = [
    [ 1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
    ],
    k = 8,

    return 13.
    ```
* 解法簡述: 
    ```
    本題可以使用二元搜尋法找出答案, 首先左上角與右下角必定為整個陣列中最小及最大的值
    然後每次計算 mid 後就確認這個 mid 是在整個陣列中屬於第幾大
    如果 mid <= 該值, 則 count += 1
    注意要每一行都檢查，因為每一行都是從小到大，但兩行之間並無直接的大小關係
    ```
#### [769. Max Chunks To Make Sorted](https://leetcode.com/problems/max-chunks-to-make-sorted/description/) (Array)
* 題目: 給一陣列 ```arr```, 其內容為亂序之後的 ```[0, 1, ..., arr.length - 1]```, 請回傳如果要將陣列拆散成大小不一的 **chunk** 進行重新排序, 最多可以拆成幾塊
* Example 1:
    ```
    Input: arr = [4,3,2,1,0]
    Output: 1
    Explanation:
    Splitting into two or more chunks will not return the required result.
    For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
    ```
* Example 2:
    ```
    Input: arr = [1,0,2,3,4]
    Output: 4
    Explanation:
    We can split into two chunks, such as [1, 0], [2, 3, 4].
    However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
    ```
* 解法簡述:
    ```
    這題的重點在於值與長度有對應關係
    排序後陣列中的每個位置的值都是固定的，必定是 arr[index] = index
    首先我們用迴圈走過整個陣列，並每看過一個元素就確認其是否為當前最大值
    假若我們遇到一個值，其位置與其值相等，這表示
    這個位置之前的所有值，都比這個值還要小，
    而且根據題目不會有重複的值，也就是說前面的每個位置的值都一定在這 Chunk 中
    如果單獨針對這個 Chunk 進行排序，每個元素都能按照要求的被排序好
    所以我們只要走過一次 array , 每看一個元素就試著更新最大值，
    並隨時檢查當前是否符合 arr[當前index] == 最大值
    假若是，我們就累計 count +=1, 最後回傳 count 即為答案
    ```

#### [485. Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/description/) (Array)
* 題目: 給一陣列 ```nums```, 其中只包含了 ```0``` 及 ```1```, 請回傳最長連續 ```1``` 的長度
* Example 1:
    ```
    Input: [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s.
        The maximum number of consecutive 1s is 3.    
    ```
* 解法簡述:
    ```
    走過整個陣列並記錄連續看了幾個 1, 
    如果遇到 0 就將記錄設為 0 並比較這次是否與之前看到最長的連續 1 還長
    如是則更新最大值, 最後回傳該最大值
    ```

#### [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/description/) (Array, Dynamic Programming)
* 題目: 給一整數陣列 ```nums```, 找出其所有的**連續**子陣列中乘積的最大值
* Example 1:
    ```
    Input: [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.
    ```
* Example 2:
    ```
    Input: [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
    ```
* 解法簡述:
    ```
    本題解法有兩種 1)比較好懂但比較慢 2)比較快但是比較難懂
    1) 
    這個做法非常好懂
    其實最重要的就是負數還有0
    先討論負數，而且必須是奇數個負數，如果是偶數個負數的話會負負得正
    假設數列中有3個負數，則最大值必定存在以三個負數的其中一個作為分割點的左數列或右數列其中一個
    舉例來說 數列是 [2, 2, -3, 2, 2, -4, 2, 2, -5, 2, 2]
    若取-3為分割點則左右分別為 [2 2] [-3] [2 2 -4 2 2 -5 2 2]
    若取-4為分割點則左右分別為 [2 2 -3 2 2] [-4] [2 2 -5 2 2]
    若取-5為分割點則左右分別為 [2 2 -3 2 2 -4 2 2] [-5] [2 2]
    以這個例子的話 最大會是-3分割的右邊
    而使用下面方法的左右各pass一次，這三種分割方式的六個子數列都可以考慮到
    接著我們再來考慮 0, 因為只要經過 0 結果就一定是 0
    這邊的想法可以看做是，把0當成分割點，同時考慮左右側的最大值
    所以將 p 重設為 1, 而因為 p 會先 *= n 所以也不用擔心說 0 這個值不會被比較到
    雖然這個方法是 O(n*2), 但是我覺得好懂多了

    2) 
    之所以要用雙 dp array 似乎是因為考慮ith元素之後的最大值, 一定是來自於
    1) i-1 最小值 * i (可能是負負得正)
    2) i-1 最大值 * i (正常考慮就是這樣)
    3) i 元素 (例如 i-1 最大是 -4, 最小是 -14, 而元素 i 則是 10->這樣取 10 反而最大
    所以每次加入一個新的值，都要比叫這三者去更新 最小跟最大值
    ```

#### [918. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/description/) (Array)
* 題目: 給一循環陣列 ```C```, 找出 C 中最大的非空連續子陣列的總和值
* Example 1:
    ```
    Input: [1,-2,3,-2]
    Output: 3
    Explanation: Subarray [3] has maximum sum 3
    ```
* Example 2:
    ```
    Input: [5,-3,5]
    Output: 10
    Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
    ```
* Example 3:
    ```
    Input: [3,-1,2,-1]
    Output: 4
    Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
    ```
* Example 4:
    ```
    Input: [3,-2,2,-3]
    Output: 3
    Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
    ```
* Example 5:
    ```
    Input: [-2,-3,-1]
    Output: -1
    Explanation: Subarray [-1] has maximum sum -1
    ```
* 解法簡述:
    * 本題與 [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) 有很大的關係, 可以先看看
    ```
    本題解法僅是 53. Maximum Subarray 的延伸
    在 53 題中我們處理的是一般的陣列而不是環形
    而在本題加入環形後，可能的答案一定會屬於以下兩種狀況之一
    1) 答案與 53 題一致, 並沒有因為環型產生更大的解
    2) 因為多了環形所以頭尾相接的部分產生了更大的解
    所以我們只要比較這兩者哪個大就好了
    而狀況 2 的解法是
    假設總和最大的非空連續子陣列有通過環型
    就表示整個陣列中起點從某個值經過尾巴到頭部之後再往前走之後停下來
    這邊我們排除停下來的點與起點一致的可能性，因為那是狀況1
    所以在終點跟起點之間, 會有一個非空連續子陣列存在, 以下稱為 ss
    這個 ss 一定是因為只會降低總和，所以才沒有被排除在答案以外
    所以我們可以得知這段 ss 總和必定是一個負值
    基於此我們可以去更改第 53 題的寫法，讓他找出這個陣列中的總和最小的非空連續子陣列
    如此一來 我們只要將整個陣列的總和減去這一段就完成了
    但這有個特例就是，如果整個陣列都是負值，則會變成
    狀況 1 找到的是最小的負數，狀況 2 是 0
    所以我們先確認狀況1 是否小於0，如果是就回傳狀況1
    如果不是就只要比較狀況 1 與狀況 2 看誰比較大就找出答案
    ```

#### [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/description/) (Array, Sort)
* 題目: 給定一組區間, 將重疊的部分合併
* Example 1:
    ```
    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
    ```
* Example 2:
    ```
    Input: [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.
    ```
* 解法簡述:
    ```
    先將所有的 interval 根據其起點進行排序
    然後比較前者終點跟後者起點是否有重疊, 
    如果有就合併放到另外一個 list
    沒有的話就直接單獨的丟到另外一個 list
    ```

#### [945. Minimum Increment to Make Array Unique](https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/) (Array)
* 題目: 給一數列, 有些數字有重複有些沒有，請問若是可以以1為單位對其中元素進行增減, 需要多少次才可以使整個數列沒有數字重複
* Example 1:
    ```
    Input: [1,2,2]
    Output: 1
    Explanation:  After 1 move, the array could be [1, 2, 3].
    ```
* Example 2:
    ```
    Input: [3,2,1,2,1,7]
    Output: 6
    Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
    It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
    ```
* 解法簡述:
    ```
    核心想法是排序後的每個值，都至少要比前一個值大 1
    先將整個數列從小到大排序
    我們可以知道，如果兩個數重複，後者必須要更改為比前者大 1
    假設數列中重複的片段為 [7, 7 ,7, 10] -> 他應該要被改成 [7, 8, 9 ,10]
    才是符合規則的，而當我們看到 7 的時候就已經知道 如果下一個數小於 8 那就是不合法
    所以當走過每個數字的時候，我們都檢查她有沒有比我們目前看過的最大值 +1
    也就是上一個數 +1, 如果有那就合法，但下一個數就要比這個數還大
    也就是 最大值要變成目前這個數 +1
    如果沒有 那就是要把當前值變成上一個數 + 1, 接著把最大值再 +1
    然後過程中我們只要記錄每次比較的時候
    如果當前值比需求的最大值還小，就累計最大值-當前值，
    最後回傳這個數值就得解
    ```

#### [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/description/) (Array, Two Pointers)
* 題目: 給定一數列，請將所有 0 移至數列最後方
* Example 1:
    ```
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]
    ```
* 解法簡述: 
    ```
    我們用一個指標 idx 紀錄數列目前到哪裡為止是看過的，接著
    走過整個數列，當我們看到一個不是 0 的數字, 就把他跟 idx 上的值交換
    接著 idx += 1
    然後如果遇到 0 我們就跳過，遇到下一個不是 0 的就換位子
    如此一來我們就把所有非 0 的值按順序移至最前方了
    也就解了問題
    ```

#### [31. Next Permutation](https://leetcode.com/problems/next-permutation/description/) (Array)
* 題目: 很不好說明, 自己看
* Example 1:
    ```
    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1
    ```
* 解法簡述:
    

#### [915. Partition Array into Disjoint Intervals]( https://leetcode.com/problems/partition-array-into-disjoint-intervals/description/) (Array)
* 題目: 給一數列，將其分成左右兩個數列，左邊的值都小於右邊的值, 並使左邊數列長度越小越好
* Example 1:
    ```
    Input: [5,0,3,8,6]
    Output: 3
    Explanation: left = [5,0,3], right = [8,6]
    ```
* Example 2:
    ```
    Input: [1,1,1,0,6,12]
    Output: 4
    Explanation: left = [1,1,1,0], right = [6,12]
    ```
* 解法簡述:
    ```
    這個解法的想法是去紀錄三個數值
    1) 目前分割點
    2) 目前分割點左側最大值
    3) 目前最大值
    每次看一個新的元素就要更新目前最大值
    接著檢查目前左側最大值是不是有大過新看到的值，此處可以分成兩個情況來來分析
        a) 如果這個值比左側最大值還要小，那他必須是在分割點的左側，所以要更新目前分割點至目前的位子
        此外，因為分割點被更新目前的元素, 所以左側最大值也必須被更新為當前最大值
        b) 如果這個值比左側最大值還大，他應該在分割點右側，符合目前狀況

    簡單的解法是
    要找某個idx開始，左側的最大值 < 右側的最小值, 而此 idx 要越小越好
    所以我走過整個數列，並記錄當下的左側最大值及右側最小值
    之後回傳最小且左側的最大值 < 右側的最小值的idx
    ```
    
#### [566. Reshape the Matrix](https://leetcode.com/problems/reshape-the-matrix/description/) (Array)
* 題目: 給一陣列及指定長寬，將陣列改變成指定長寬的大小後回傳，若無法則回船員陣列
* Example 1:
    ```
    Input: 
    nums = 
    [[1,2],
    [3,4]]
    r = 1, c = 4
    Output: 
    [[1,2,3,4]]
    Explanation:
    The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
    ```
* Example 2:
    ```
    Input: 
    nums = 
    [[1,2],
    [3,4]]
    r = 2, c = 4
    Output: 
    [[1,2],
    [3,4]]
    Explanation:
    There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
    ```
* 解法簡述:
    ```
    我的作法很簡單，就是開一回傳陣列跟一暫存陣列
    持續地將原陣列的值輸入至暫存
    如果暫存達到指定長度，就丟進回傳陣列並將暫存洗白
    最後就只要回傳就好
    ```

#### [950. Reveal Cards In Increasing Order](https://leetcode.com/problems/reveal-cards-in-increasing-order/description/) (Array)
* 題目: 很複雜
* Example 1:
    ```
    Input: [17,13,11,2,3,5,7]
    Output: [2,13,3,11,5,17,7]
    Explanation: 
    We get the deck in the order [17,13,11,2,3,5,7] (this order doesn't matter), and reorder it.
    After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
    We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
    We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
    We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
    We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
    We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
    We reveal 13, and move 17 to the bottom.  The deck is now [17].
    We reveal 17.
    Since all the cards revealed are in increasing order, the answer is correct.
    ```
* 解法簡述:
    ```
    我的作法就是照著範例的順序倒著做
    先將輸入排序，然後開一個回傳陣列
    由大到小將輸入陣列的值存入回傳陣列後
    並且每次傳入一個值就將回傳陣列的最後一個值放到最前面
    ```

#### [900. RLE Iterator](https://leetcode.com/problems/rle-iterator/description/) (Array)
* 題目: 好囉嗦
* Example 1:
    ```
    Input: ["RLEIterator","next","next","next","next"], [[[3,8,0,9,2,5]],[2],[1],[1],[2]]
    Output: [null,8,8,5,-1]
    Explanation: 
    RLEIterator is initialized with RLEIterator([3,8,0,9,2,5]).
    This maps to the sequence [8,8,8,5,5].
    RLEIterator.next is then called 4 times:

    .next(2) exhausts 2 terms of the sequence, returning 8.  The remaining sequence is now [8, 5, 5].

    .next(1) exhausts 1 term of the sequence, returning 8.  The remaining sequence is now [5, 5].

    .next(1) exhausts 1 term of the sequence, returning 5.  The remaining sequence is now [5].

    .next(2) exhausts 2 terms, returning -1.  This is because the first term exhausted was 5,
    but the second term did not exist.  Since the last term exhausted does not exist, we return -1.
    ```
* 解法簡述:
    ```
    解法的想法是，只要記錄目前走到第幾步就好了
    儲存 A 的時候將連續出現的次數變換成最後一次出現的位置
    當 next 被呼叫的時候，將 n 累計起來
    然後就只要查閱 n 介於那兩個數字的最後一次出現位置之間
    ```

#### [48. Rotate Image](https://leetcode.com/problems/rotate-image/description/) (Array)
* 題目: 給定一個陣列，將其向右轉 90 度
* Example 1: 
    ```
    Given input matrix = 
    [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ],

    rotate the input matrix in-place such that it becomes:
    [
    [7,4,1],
    [8,5,2],
    [9,6,3]
    ]
    ```
* Example 2:
    ```
    Given input matrix =
    [
    [ 5, 1, 9,11],
    [ 2, 4, 8,10],
    [13, 3, 6, 7],
    [15,14,12,16]
    ], 

    rotate the input matrix in-place such that it becomes:
    [
    [15,13, 2, 5],
    [14, 3, 4, 1],
    [12, 6, 8, 9],
    [16, 7,10,11]
    ]
    ```
* 解法簡述:
    ```
    有兩種解法
    1) 將陣列直的讀取，並橫著放，例如 example 1 的第一個 column 接再第一個 row 後
       會變成 [1, 2, 3, 1, 4, 7], 然後再把原本的 row 給 pop()出去
    2) 先上下翻，可以用 reverse 或是 [::-1], 再來對角翻, 也就是m[i][j] = m[j][i]
    ```

#### [240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/description/) (Binary Search, Divide and Conquer)
* 題目: 給一陣列, 其中每一行每一列都是從左上遞增到右下, 給一數字, 回傳該數字是否在這陣列中
* Example 1:
    ```
    Consider the following matrix:

    [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
    ]

    Given target = 5, return true.
    Given target = 20, return false.
    ```
* 解法簡述:
    ```
    本題解法為從右上角開始找
    如果 target 和目前的值一樣就回傳 True
    如果目前的值比 target 小, 那就往下面找, 就會有更大的
    如果目前的值比 target 大, 那就往左邊找, 就會有更小的
    如果最後找到最左下角還是沒有, 那就回傳 False
    ```

#### [645. Set Mismatch](https://leetcode.com/problems/set-mismatch/description/) (Hash Table, Math)
* 題目: 給一陣列表示 set, 其中的值應該要介於 ```1 ~ n``` 之間且不重複, 現在有一個值被另外一個值取代了，請回傳 ```(重複的值, 被取代的值)```
* Example 1:
    ```
    Input: nums = [1,2,2,4]
    Output: [2,3]
    ```
* 解法簡述:
    ```
    解法有兩種, 
    1 是利用其值範圍的性質, 也就是 1~n, 其總和必定是 (n * (n+1))/2
    用 1~n 總和減去當前總和就可以找出兩者之間的差值 Diff
    接著使用之前在 442. Find All Duplicates in an Array 使用過的方法
    走過整個數列, 令 index  = abs(n)-1
        如果 nums[index] > 0: nums[index] = -nums[index]
        如果 nums[index] < 0: 表示我們走過了，這個值就是重複的值
    接著只要回傳重複值跟 重複值+Diff 就好了
    2 是使用 set 過濾掉重複值, 可以更快一點
    ```

#### [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/description/) (Array)
* 題目: 給一陣列，請以順時針螺旋的方式讀取成另一陣列並輸出
* Example 1:
    ```
    Input:
    [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
    ]
    Output: [1,2,3,6,9,8,7,4,5]
    ```
* Example 2:
    ```
    Input:
    [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
    ]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    ```
* 解法簡述:
    ```
    解法跟 48. Rotate Image 有點類似, 有兩個步驟
    1) 建立一新回傳陣列並將 matrix[0] pop出來並放進回傳陣列中
    2) 將 matrix 向左邊轉 90 度
    直到 matrix == None
    ```

#### [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/description/) (Array, Greedy, Queue)
* 題目: 有點複雜
* Example 1:
    ```
    Input: tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8
    Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
    ```
* 解法簡述:
    ```
    方法有兩種, 一個是認真的模擬這個系統
    也就是紀錄每個 task 的數量以及冷卻時間
    然後用一個變數去紀錄包含休息目前總共跑了幾個行程
    重點是要盡可能先消耗工作量數量較高的工作
    二是比較快也聰明的作法
    使用方塊法, 可以看 solution 3
    或 https://leetcode.com/problems/task-scheduler/discuss/104507/Python-Straightforward-with-Explanation
    可以分成兩種情況討論
    1. 休息時間太短，工作種類太多，也就是可以一直做不一樣的工作都不用休息
        這種狀況就是 task 的數量決定工作的總 intervals 數
    2. 休息時間太長，工作種類太少，也就是每種工作都做過還是需要休息
        這種狀況下，所有工作中數量最大的工作會影響休息的次數
        令 k = 最大工作量, 你至少需要休息 k 次才有機會在第 k 輪做完最後一次的工作
        基於這點我們就可以確定至少需要 (n+1) * (k-1) 的intervals (n+1 是因為休息兩次代表第三次才能再執行該工作)
        除此之外，假設最大工作量 k 的工作種類不只一種(但必定小於 n 種，不然就是狀況1)，
        那麼我們就還需要在第 k 輪時把最後的工作做完，而最後的工作數量 = 工作量為k的工作種類
        所以就得到 (n+1) * (k-1) + (數量為 k 的工作種類)
    基於兩種狀況我們就可以得到 max(len(task), (n+1) * (k-1) + (數量為 k 的工作種類))
    ```

#### [766. Toeplitz Matrix](https://leetcode.com/problems/toeplitz-matrix/description/) (Array)
* 題目: 給一數列，檢查她是不是一個常對角矩陣, 也就是要求每一條斜角線上的元素都是一樣的
* Example 1:
    ```
    Input:
    matrix = [
    [1,2,3,4],
    [5,1,2,3],
    [9,5,1,2]
    ]
    Output: True
    Explanation:
    In the above grid, the diagonals are:
    "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
    In each diagonal all elements are the same, so the answer is True.
    ```
* Example 2:
    ```
    Input:
    matrix = [
    [1,2],
    [2,2]
    ]
    Output: False
    Explanation:
    The diagonal "[1, 2]" has different elements.
    ```
* 解法簡述:
    ```
    針對每一行跟其下一行檢查是否 row[i][0:n-1] == row[i+1][1:n]
    只要跑完沒有錯就是可以的
    ```
