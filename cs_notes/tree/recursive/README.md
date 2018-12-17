#### [623. Add One Row to Tree](https://leetcode.com/problems/add-one-row-to-tree/description/) (Tree)
* 題目: 給一樹之根結點及兩個正整數 ```v``` & ```d```, 請在樹的第 ```d``` 層插入一層值為 ```v``` 的點, 並回傳根結點.
* Example 1:
    ```
    Input: 
    A binary tree as following:
         4
       /   \
      2     6
     / \   / 
    3   1 5   

    v = 1

    d = 2

    Output: 
          4
         / \
        1   1
       /     \
      2       6
     / \     / 
    3   1   5   
    ```
* Example 2:
    ```
    Input: 
    A binary tree as following:
        4
       /   
      2    
     / \   
    3   1    

    v = 1

    d = 3

    Output: 
          4
         /   
        2
       / \    
      1   1
     /     \  
    3       1
    ```
* 解法簡述:
    ```
    一開始的想法是
    用 BFS 走到要被取代的層, 並記錄上一層
    然後依序將新增層和上一層跟下一層接起來, 但超時了
    以下是改善的方向
    1) fake root 的想法, 如此就可以避免 d = 1 要寫例外狀況的處理
    2) 只取到要被取代的層的上一層, 下稱 last
        然後將新的一層接在 last 下面, 把 last 的左右孩子再往下接
        原本以為這樣會有 None 的問題要處理, 但好像不會
        因為如果 Node 沒有在 last 就不會往下接
        如果 Node 在 last 中, 就代表一定有孩子可以存取,
        至於孩子到底是 None 還是 TreeNode 都不影響程式運作
    ```
#### [863. All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/) (Tree, DFS, BFS)
* 題目:給一樹之根結點```root```及其中一節點```target```, 請回傳所有跟```target```相隔 ```k``` 條邊的節點
* Example 1:
    ![pic](./pics/863.png)
    ```
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

    Output: [7,4,1]

    Explanation: 
    The nodes that are a distance 2 from the target node (with value 5)
    have values 7, 4, and 1.

    Note that the inputs "root" and "target" are actually TreeNodes.
    The descriptions of the inputs above are just serializations of these objects.
    ```
* 解法簡述:
    ```
    這題有兩種解法
    1) DFS + BFS
        DFS 將 Tree 轉為無向圖 (新增一變數紀錄自己的 parent node)
        BFS 從 target 開始往外走 K 步, 因為可以往 parent node 走, 所以沒問題
    2) Recursion
        要往三個方向探索
        a) target 的子樹
        b) 和 target 同側, 但是但比 target 更靠近 root 的部分
        c) 和 target 不同側
        a 的情況就只要找出用 dfs 找出離 target 距離為 k 的點就好
        而 b, c 情況套用 dfs 解, 請直接去看 code 吧
    ```
#### [894. All Possible Full Binary Trees](https://leetcode.com/problems/all-possible-full-binary-trees/description/) (Tree, Recursion)
* 題目: 給一正整數 ```N```, 請回傳所有使用了 N 個節點的滿二元樹 (每個節點的孩子數必為 0 或 2)
* Example 1:
    ![](./pics/894.png)
    ```
    Input: 7
    Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
    Explanation:
    ```
* 解法簡述:
    ```
    本題解法使用 top-down 的 DP
    首先一個滿二元樹的左右子樹必定也要是滿二元樹
    所以當我們想要知道 7 個節點的滿二元樹的種類
    簡單來說 就是要知道她左右子樹有多少變化
    例如說 左1 右5, 左2 右4,  左3 右3, ...等
    這個種類數量其實就是 dp[1]*dp[5] + dp[2]*dp[4] + dp[3]*dp[3] + ...
    但因為題目要求回傳整個樹的架構， 所以我們的 DP 必須是 dictionary
    並儲存 N = 1..6 的所有子架構, 才能算出所有的變化
    要注意的是, N = 0, 2, 4, 6 是無法建構滿二元樹的
    這時候在 dict 中要儲存空的陣列, 如此一來在 for 迴圈時就會直接跳出
    ```
#### [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/) (Tree, DFS)
* 題目: 給一樹之根節點, 請問此樹是否為均衡二元樹 (均衡二元樹中每個節點的左右子樹高度差都小於等於 1)
* Example 1:
    ```
    Given the following tree [3,9,20,null,null,15,7]:

      3
     / \
    9  20
      /  \
     15   7
    Return true.
    ```
* Example 2:
    ```
    Given the following tree [1,2,2,3,3,null,null,4,4]:

          1
         / \
        2   2
       / \
      3   3
     / \
    4   4
    eturn false.
    ```
* 解法簡述:
    ```
    本題解法跟深度有很大的關係, 基於計算深度的方法上
    首先先看看當前節點的左邊深度跟右邊深度
    假設兩邊深度差大於 1, 就回傳 -1
    如果看到其左或右邊深度為 -1 就接著也回傳 -1
    但如果兩邊深度差小於等於 1, 那就
    回傳 max(左邊深度, 右邊深度) + 1 給他的父節點繼續運作
    ```
#### [814. Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/description/) (Tree)
* 題目:給一二元樹, 其節點值必為 0 或 1, 請將不包含 1 的子樹全部修剪掉
* Example 1:
    ```
    Example 1:
    Input: [1,null,0,0,1]
    Output: [1,null,0,null,1]
    
    Explanation: 
    Only the red nodes satisfy the property "every subtree not containing a 1".
    The diagram on the right represents the answer.
    ```
* Example 2:
    ```
    Example 2:
    Input: [1,0,1,0,0,0,1]
    Output: [1,null,1,null,1]
    ```
* Example 3:
    ```
    Example 3:
    Input: [1,1,0,1,1,0,1,0]
    Output: [1,1,0,1,1,null,1]
    ```
* 解法簡述:
    ```
    解法很簡單, 用 DFS 往下走到葉節點
    只要滿足兩個條件就可以把該點拔掉, 回傳 None 給父節點取代當前節點
    1) 左右都沒有孩子
    2) 自己的值為 0
    這樣拔掉這個點就是安全的, 然後從葉子開始往回拔就沒問題了
    ```
#### [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/) (Array, Tree, DFS)
* 題目: 給一樹之前序與中序, 請重新建構該樹
* Example 1:
    ```
    For example, given

    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    Return the following binary tree:

      3
     / \
    9  20
      /  \
     15   7
    ```
* 解法簡述:
    ```
    本題核心在於如何理解 inorder 及 preorder
    inorder 是 (左)(中)(右)
    preorder 是 (中)(左)(右) 
    所以只要透過 preorder[0] 知道當前中間點是哪個元素
    接著在 inorder 中找到該點, 就知道左邊是哪些元素, 右邊有哪些元素
    在來就只要把 root.left 用遞迴的方式往下傳就好了
    ```
#### [889. Construct Binary Tree from Preorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/) (Tree)
* 題目: 給一樹之前序與後序, 請重新建構該樹
* Example 1:
    ```
    Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
    Output: [1,2,3,4,5,6,7]
    ```
* 解法簡述:
    ```
    本題解法同上, 只要知道前後序的差別就可以了
    前序為 (中)(左)(右)
    後序為 (左)(右)(中) 而且會是倒序
    所以只要從後序中找出從前序的第二個元素的位置, 假設為 idx
    則 pre[0], pre[1:idx+1] pre[idx+1:] 就對應了中左右
    而 post[:idx], post[idx:-1], post[-1] 就是 左右中
    然後就只要建立 root, 遞迴 root.left 跟 root.right 就好了
    ```
#### [109. Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/) (Linked List, DFS)
* 題目: 給一排序後的 Linked List, 將其建立成 BST
* Example 1:
    ```
    Given the sorted linked list: [-10,-3,0,5,9],

    One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

         0
        / \
      -3   9
      /   /
    -10  5
    ```
* 解法簡述:
    ```
    本題若先將 LL 轉換成 List 就是一個非常簡單的題目
    只要選正中間做為 root ,左邊的陣列遞迴回傳為 root.left, 右邊的陣列遞迴回傳為 root.right
    但如果要使用 LL, 就需要使用快慢指針找出 LL 的中間點
    ```
#### [222. Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/description/) (Binary Search, Tree)
* 題目: 給一完整二元樹, 請計算有多少個節點
* Example 1:
    ```
    Input: 
        1
       / \
      2   3
     / \  /
    4  5 6

    Output: 6
    ```
* 解法簡述:
    ```
    本題重點在於完整二元樹的結構
    首先計算左右兩子樹的最左側節點深度
    之所以是最左側是因為完整二元樹的結構中, 最左側的點一定是最深的
    接著比較左右子樹的深度, 一定只會有兩種狀況
    1) l_depth == r_depth, 這表示左側是完美的完整二元樹, 而右側可能有未填滿的部分
    2) l_depth == r_depth+1, 這表示右側是完美的完整二元樹, 而左側可能有未填滿的部分
    對於完美的完整二元樹, 節點數量必定為 (2 ** depth)-1
    而不完美的部分, 就再次帶入函數進行遞迴
    以上面的左側為完美, 右側未填滿為例的話
    數量就是 [根節點] + [完美左側] + [未填滿右側]
    也就是  1 + pow(2, l_depth)-1 + func(root.right)
    ```
#### [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/description/) (Tree)
* 題目: 給一二元樹, 請回傳其中兩節點間最長的距離 (也就是經過的邊的數量)
* Example 1:
    ```
    Given a binary tree 
        1
       / \
      2   3
     / \     
    4   5    
    Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
    ```
* 解法簡述:
    ```
    本題解法也是跟深度有很大的關係
    對某一根節點, 其最長的距離必定是左子樹中最深的點到右子樹中最深的點
    所以本題可以用 dfs 走遍所有節點
    並記錄每個節點的最深左子節點到最深右子節點的距離, 並用另外一個變數更新最大值
    要注意的是, 要將目前的節點的最大深度回傳至父節點的時候, 只能回傳
    當前節點的左右子葉深度中比較大的那方, 也就是 max(l_depth, r_depth) + 1
    ```
#### [652. Find Duplicate Subtrees](https://leetcode.com/problems/find-duplicate-subtrees/description/) (Tree)
* 題目: 給一二元樹, 找出其中結構完全相同的子樹並回傳重複的結構
* Example 1:
    ```
    Example 1:

          1
         / \
        2   3
       /   / \
      4   2   4
     /
    4
    The following are two duplicate subtrees:

      2
     /
    4
    and

    4
    Therefore, you need to return above trees' root in the form of a list.
    ```
* 解法簡述:
    ```
    這題的想法很特別, 是將 Tree 的轉成字串的感覺
    要注意的是, 如果只是單純轉換成前序或後序
    會發生字串一樣但是架構其實不一樣的狀況
    所以要把 None 的部分也填上, 例如填上 '#' 或是 '.'
    如此一來就可以完整保存當前點作為 root 時的樹的結構
    此外就是用 dict 來記錄每個樹字串出現的次數
    由於輸出只要重複的部份的其中一邊
    所以只需要在出現次數為 2 的時候將其放進 answer
    最後回傳 answer 即可
    ```
#### [515. Find Largest Value in Each Tree Row](https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/) (Tree, DFS, BFS)
* 題目: 給一二元樹, 回傳每一行的最大值
* Example 1:
    ```
    Input: 

        1
       / \
      3   2
     / \   \  
    5   3   9 

    Output: [1, 3, 9]
    ```
* 解法簡述:
    ```
    本題只要使用 BFS 就可以
    要注意的是, 只要回傳最大的值就好
    所以 BFS 的每次迴圈, 都用另外一個陣列將被pop的節點的值存起來
    然後找出最大值之後放在最後要回傳的陣列就好
    ```
#### [114. Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/) (Tree, DFS)
* 題目:將一二元樹轉換成 Linked List (請將 right 作為 next 使用)
* Example 1:
    ```
    given the following tree:
        1
       / \
      2   5
     / \   \
    3   4   6
    The flattened tree should look like:

    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6
    ```
* 解法簡述:
    ```
    解法有2
    1) 用前序全部裝到list中
       然後將後面的Node當成前面Node的右邊孩子
    2) 使用一額外變數 prev 紀錄上一次看過的點
       並使用右左中的順序來執行 DFS
       先進去右邊孩子, prev 變成右邊孩子
       在來進去左邊孩子, 左邊孩子的 right 變成右邊孩子, prev 變成左邊孩子
       最後當右邊跟左邊都探索完之後
       將父節點的右邊孩子變成替換成原本的左邊孩子, 最後 prev 變成自己在回傳給自己的父節點
    ```
#### [951. Flip Equivalent Binary Trees](https://leetcode.com/problems/flip-equivalent-binary-trees/description/) (Tree)
* 題目: 給兩個二元樹, 請回答兩樹的差異是否只是在某些節點上進行左右對調而已
* Example 1:
    ```
    Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
    Output: true
    Explanation: We flipped at nodes with values 1, 3, and 5.
    ```
* 解法簡述:
    ```
    作法很簡單, 使用遞迴往下檢查
    首先對 root1, root2 的左右孩子的值做檢查
    如果 l1 == l2 and r1 == r2, 表示這個節點應該沒有被反轉
    所以往下檢查 flipEquiv(root1.left, root2.left) 及 flipEquiv(root1.right, root2.right)
    但如果 l1 == r2 and r1 == l2, 表示這個節點應該是被反轉
    所以往下檢查 flipEquiv(root1.left, root2.right) 及 flipEquiv(root1.right, root2.left)
    而如果不符合這兩種狀況, 那兩者差異就一定不只是反轉, 就回傳 False
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