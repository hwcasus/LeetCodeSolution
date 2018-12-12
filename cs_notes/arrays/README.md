####[870. Advantage Shuffle](https://leetcode.com/problems/advantage-shuffle/description/) (Array, Greedy, Two Pointers) 
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

####[954. Array of Doubled Pairs](https://leetcode.com/problems/array-of-doubled-pairs/description/) (Array, Hash Table)
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
*  Example 3:
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
* 題目: 給一陣列 ```nums```, 其長度為 n 且值介於 ```1 ~ n-1```, 其中部分元素出現兩次, 請回傳出現次數為 2 的元素

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
* 題目: 
* 解法簡述:

#### [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/description/) (Array, Two Pointers, Binary Search)
* 題目: 
* 解法簡述:

#### [926. Flip String to Monotone Increasing](https://leetcode.com/problems/flip-string-to-monotone-increasing/description/) (Array)
* 題目: 
* 解法簡述:
#### [55. Jump Game](https://leetcode.com/problems/jump-game/description/) (Array, Greedy)
* 題目: 
* 解法簡述:
#### [378. Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/) (Binary Search, Heap)
* 題目: 
* 解法簡述:

#### [769. Max Chunks To Make Sorted](https://leetcode.com/problems/max-chunks-to-make-sorted/description/) (Array)
* 題目: 
* 解法簡述:

#### [485. Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/description/) (Array)
* 題目: 
* 解法簡述:

#### [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/description/) (Array, Dynamic Programming)
* 題目: 
* 解法簡述:

#### [918. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/description/) (Array)
* 題目: 
* 解法簡述:

#### [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/description/) (Array, Sort)
* 題目: 
* 解法簡述:

#### [945. Minimum Increment to Make Array Unique](https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/) ()
* 題目: 
* 解法簡述:

#### [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/description/) ()
* 題目: 
* 解法簡述:

#### [31. Next Permutation](https://leetcode.com/problems/next-permutation/description/) ()
* 題目: 
* 解法簡述:

#### [915. Partition Array into Disjoint Intervals]( https://leetcode.com/problems/partition-array-into-disjoint-intervals/description/) ()
* 題目: 
* 解法簡述:

#### [566. Reshape the Matrix](https://leetcode.com/problems/reshape-the-matrix/description/) ()
* 題目: 
* 解法簡述:

#### [950. Reveal Cards In Increasing Order](https://leetcode.com/problems/reveal-cards-in-increasing-order/description/) ()
* 題目: 
* 解法簡述:

#### [900. RLE Iterator](https://leetcode.com/problems/rle-iterator/description/) ()
* 題目: 
* 解法簡述:

#### [48. Rotate Image](https://leetcode.com/problems/rotate-image/description/) ()
* 題目: 
* 解法簡述:

#### [240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/description/) ()
* 題目: 
* 解法簡述:

#### [645. Set Mismatch](https://leetcode.com/problems/set-mismatch/description/) ()
* 題目: 
* 解法簡述:

#### [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/description/) ()
* 題目: 
* 解法簡述:

#### [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/description/) ()
* 題目: 
* 解法簡述:

#### [766. Toeplitz Matrix](https://leetcode.com/problems/toeplitz-matrix/description/) ()
* 題目: 
* 解法簡述:
