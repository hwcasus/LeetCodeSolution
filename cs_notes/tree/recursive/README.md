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
#### [337. House Robber III](https://leetcode.com/problems/house-robber-iii/description/) (Tree, DFS)
* 題目: 給一二元樹表示房屋建築, 不能搶鄰近層, 請問最多可以搶多少錢
* Example 1:
    ```
    Input: [3,2,3,null,3,null,1]

      3
     / \
    2   3
     \   \ 
      3   1

    Output: 7 
    Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
    ```
* Example 2:
    ```
    Input: [3,4,5,1,3,null,1]

        3
       / \
      4   5
     / \   \ 
    1   3   1

    Output: 9
    Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
    ```
* 解法簡述:
    ```
    本題解法在於對於每個節點都存在著兩種搶法
    1) 要搶自己這層
    2) 不搶自己這層
    而每個節點在作為一個子節點的時候
    這兩種搶法正好表示了一個父節點是要搶孩子還是不搶孩子
    1) 如果搶父親自己, 就兩個孩子都不能搶
    2) 如果不搶自己, 就表示可以從左右孩子中都選最大的
    以下把 root_val 作為父親節點的值
    l_child_root_val, l_child_child_val 就是左邊孩子的包含自己搶法, 跟不包含自己搶法
    r_child_root_val, r_child_child_val 就是左邊孩子的包含自己搶法, 跟不包含自己搶法
    所以兩種搶法分別對應
    1) root_val + l_child_child_val + r_child_child_val, 也就是絕對不能搶到自己孩子那間房子
    2) max(l_child_root_val, l_child_child_val) + max(r_child_root_val, r_child_child_val)
    將這兩者回傳給自己的父節點時
    就會變成 child_root_val, child_child_val, 對應到不搶自己跟搶自己的最大搶法
    最後從 root 回傳之後就只要從兩者挑選大者就可以了
    ```
#### [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/description/) (Tree)
* 題目: 給一二元樹, 請將其完全反轉
* Example 1:
    ```
    Input:

         4
       /   \
      2     7
     / \   / \
    1   3 6   9
    Output:

         4
       /   \
      7     2
     / \   / \
    9   6 3   1
    ```
* 解法簡述:
    ```
    本題解法很簡單, 可以用 iterative 或 recursive
    recursive 解法就是用 dfs 往下走
    只要 root 非空, 就將其孩子互換
    然後接著 recursive 其兩個孩子
    也可以讓 recursive 回傳 root
    然後在每個節點呼叫 l, r = func(r), func(l)
    iterative 則用 bfs
    每一個節點被pop出來後, 只要有任一個孩子就先左右互換
    l, r = r, l
    接著在將左右孩子 append 進到 queue
    ```
#### [687. Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/description/) (Tree, Recursion)
* 題目: 給一二元樹, 請回傳當中最長只有單一值的路徑長度 (路徑中邊的數量)
* Example 1:
    ```
    Input:

        5
       / \
      4   5
     / \   \
    1   1   5
    Output:

    2
    ```
* Example 2:
    ```
    Input:

        1
       / \
      4   5
     / \   \
    4   4   5
    Output:

    2
    ```
* 解法簡述:
    ```
    本題解法如下, 
    首先因為是要找路徑, 所以最小的長度單位畢竟是介於父子之間
    所以我們首要尋找的一定是父跟子的值相同與否
    接著就要注意到, 如果左右孩子都跟父親同值, 則長度要加再一起
    所以我們統整出這樣的規則
    1) 如果父子同值, 長度 + 1
    2) 如果父與左右子皆同值, 左右長度相加
    3) 若父子不同值, 則長度為 0
    所以這邊可以用 DFS 往下走, 只要 root 非空
    則檢查其左右子的最大同值長度, 要注意這裡回傳的不會是底下的最大值
    而會是和左右子同值的最大值, 得出之後
    檢查左右子是否與父親同值, 如是則 +1, 如否則為 0
    然後將左右子的長度相加後, 就可以得到跟目前父親同值的最長路徑長度
    每次算出當節點最長路徑時, 都去檢查是否是目前看過最大的並進行紀錄
    最後要離開當前節點, 回到父節點的時候, 記得只能回傳左右中最大的那個
    因為當前節點的父節點, 就算同值也只能取當前節點下最長的路徑往下走, 不能分岔
    從 root 離開後就回傳所有看過路徑長度中最大的即可
    ```
#### [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/) (Tree)
* 題目:給一二元樹及當中任兩節點, 請回傳此二節點的最低共同祖先 (最低表深度越大越好)
* Example 1:
    ![](pics/236.png)
    ```
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3
    Explanation: The LCA of nodes 5 and 1 is 3.
    ```
* Example 2:
    ```
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5
    Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
    ```
* 解法簡述:
    ```
    本題可以使用 DFS + recursion 解
    由於題目給的是樹中的節點, 所以當進入到一個新節點的迴圈時, 有三種狀況要回傳當前節點
    1) 如果當前節點為空, 也就是回傳 None
    2) 如果當前節點為 p, 也就是我們找到了
    3) 如果當前節點為 q, 一樣找到了
    接著當我們往下探索的時候, 必須對當前節點的左側及右側探索, 探索的結果必定屬於以下2者之一
    1) 左右分別找到 p 跟 q
    2) 其中一側先找到 p 或 q 其一就回傳了, 另一邊回傳 None (走到底都沒找到)
    先從 1 開始討論
    如果在當前節點分別在左右找到了 p 跟 q, 就表示當前節點就是 LCA, 可以直接回傳
    再來如果是狀況 2, 由於本題定義的最低共同祖先可以包含自己
    而且另外一邊是回傳 None, 這表示 p, q 一定都在同一側
    且其中一者比較高, 這表示該節點必定是兩者的 LCA
    要注意的是, 執行順序很重要
    每次進入新節點時, 必須要以後序(左右中)的方式往下探索
    大概像是
        1) 如果root是 p, q, None, 回傳root
        2) left = func(root.left)
        3) right = func(root.right)
        4) 如果左右側都非空, 表示本節點就是 LCA
        5) 如果只有左側有值, 表示該值就是 LCA   
        6) 如果兩側都空, 則回傳空  
    ```
#### [654. Maximum Binary Tree](https://leetcode.com/problems/maximum-binary-tree/description/) (Tree)
* 題目: 給一數列, 請使用當前數列建立一二元數, 並符合以下規則
    * 當前數列中最大的值作為 root, 該最大值左側的值作為當前左子樹的候選值, 該最大值右側的值作為右子樹的候選值
* Example 1:
    ```
    Input: [3,2,1,6,0,5]
    Output: return the tree root node representing the following tree:

       6
     /   \
    3     5
     \    / 
      2  0   
        \
         1  
    ```
* 解法簡述:
    ```
    本題解法很簡單, 可以用遞迴的 DFS 解決
    首先找出最大值及最大值的 index
    將最大值設為根節點的值, 並使用 index
    將 root.left = func(nums[:index])
    將 root.right = func(nums[index+1])
    要注意若傳入 nums 為空, 則回傳 None
    ```
#### [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/) (Tree, DFS)
* 題目: 給一二元樹, 請回傳其最深節點之深度
* Example 1:
    ```
    Given binary tree [3,9,20,null,null,15,7],

      3
     / \
    9  20
      /  \
     15   7
    return its depth = 3.
    ```
* 解法簡述:
    ```
    本題非常基礎, 使用 DFS + Recursion 往下走
    當遇見 root 為空值時, 回傳 0
    若當前 root 非空, 則探索左右子樹的深度
    例如 l_d, r_d = func(root.left), func(root.right)
    如此若自己孩子已經是 None, 就會回傳 0
    當root要離開並回傳時, 回傳 max(l_d, r_d)+1
    就可以讓自己的父節點知道自己正確的深度
    ```
#### [662. Maximum Width of Binary Tree](https://leetcode.com/problems/maximum-width-of-binary-tree/description/) (Tree)
* 題目: 給一二元數, 找出此樹中最寬的寬度為多少
* Example 1:
    ```
    Input: 

         1
       /   \
      3     2
     / \     \  
    5   3     9 

    Output: 4
    Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
    ```
* Example 2:
    ```
    Input: 

        1
       /  
      3    
     / \       
    5   3     

    Output: 2
    Explanation: The maximum width existing in the third level with the length 2 (5,3).
    ```
* Example 3:
    ```
    Input: 

        1
       / \
      3   2 
     /        
    5      

    Output: 2
    Explanation: The maximum width existing in the second level with the length 2 (3,2).
    ```
* Example 4:
    ```
    Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
    Output: 8
    Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
    ```
* 解法簡述:
    ```
    本題想法如下
    馬上就想到要用 BFS
    一開始是把 None 也放在 queue 裡面, 想說計算裡面非None的頭尾的距離
    但後來想想, root 的左右孩子必定是在 2*root_idx, 2*root_idx+1
    所以不需要放 None, 只要順便把 idx 跟 Node 一起放在queue就好
    然後就計算 queue 的第一個元素跟最後一個元素的 index 差值 +1
    總結一下
    本題使用 BFS + queue 來探索
    基本上探索的架構沒有變化, 但在初始跟新增元素的時候
    都要加入該元素在目前這個 row 的 index
    例如 queue = [[root, 0]]
    而後續的元素一定是藉由存取其父元素的 left 及 right 才會被加到 queue
    假設一元素在當前 row 的 index 為 j, 
    則其左右子在下一 row 的 index 必定為 2*j, 2*j+1
    如此一來就可以確保每一層我們都可以正確知道元素的位置
    接著只要每次開始 pop queue 之前, 我們計算當前 row 第一個元素及最後一個元素的 index 差+1
    就知道當前 row 的寬度, 每次計算出寬度, 就檢查是否為當前最大值並更新
    最後當我們探索完整棵樹, 就可以知道當前樹最大的寬度為多少
    ```
#### [617. Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/description/) (Tree)
* 題目: 給兩棵樹, 將兩樹融合
* Example 1:
    ```
    Input: 
        Tree 1                     Tree 2                  
            1                         2                             
           / \                       / \                            
          3   2                     1   3                        
         /                           \   \                      
        5                             4   7                  
    Output: 
    Merged tree:
            3
           / \
          4   5
         / \   \ 
        5   4   7
    ```
* 解法簡述:
    ```
    本題使用 DFS + Recursion
    首先我們定義更新的規則
    1) 如果兩節點都為空, 回傳空
    2) 如果有一節點為空, 回傳非空節點
    3) 若兩節點都非空, 回傳一新節點, 其值為兩節點之值總和
    再來我們用前序的方式探索 (中左右), 簡單來說就是
    if not (t1 and t2): return t1 or t2
    root = TreeNode(t1.val + t2.val)
    root.left = func(t1.left, t2.left)
    root.right = func(t1.right, t2.right)
    最後要把自己回傳上去給父節點
    ```
#### [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/description/) (Tree, DFS, BFS)
* 題目: 給一二元樹, 請回傳最淺的子葉之深度
* Example 1:
    ```
    Given binary tree [3,9,20,null,null,15,7],

     3
     / \
    9  20
      /  \
     15   7
    return its minimum depth = 2.
    ```
* 解法簡述:
    ```
    本題可以用 dfs 或 bfs 解, bfs 比較簡單
    用 bfs + queue 去檢索整個樹, 並用 counter 紀錄當前深度
    每結束一次迴圈就 counter += 1
    如果遇到一個節點, 其左右孩子皆為空值, 則表示他是葉節點, 就直接回傳 counter
    而 dfs 的話, 回傳規則如下
    1) 如果當前為空, 回傳 0, 表示走到葉節點
    2) 若非空, 則探索繼續其左右子樹深度
       要注意的是回傳的機制
       如果左右子樹的深度間最小值是 0, 要回傳非 0 的值 + 1, 表示只有一個孩子, 另一個為 None
       如果左右子樹的深度都是 0, 則回傳 0 + 1, 表當前為葉節點
    這樣寫的原因是因為, 如果當前節點沒有右子樹, 只有左子樹, 必須要回傳左子樹的深度而不是右子樹
    而如果右子樹是單一葉節點, 也應該會回傳 1, 而不是 0
    我個人建議使用 bfs 比較好懂
    ```
#### [508. Most Frequent Subtree Sum](https://leetcode.com/problems/most-frequent-subtree-sum/description/) (Hash Table, Tree)
* 題目: 給一二元樹, 根據每個節點計算出所有子樹的總和值, 回傳出現次數最多的總和值, 若有複數個也一併回傳
* Example 1:
    ```
    Input:

      5
     /  \
    2   -3
    return [2, -3, 4], since all the values happen only once, return all of them in any order.
    ```
* Example 2:
    ```
    Input:

      5
     /  \
    2   -5
    return [2], since 2 happens twice, however -5 only occur once.
    ```
* 解法簡述:
    ```
    本題想法來自於 652. Find Duplicate Subtrees
    其中使用字典並將樹結構轉換成字串作為 key 進行計數, 並以此來偵測重複結構
    本題是使用當前總和作為 key, 以記錄重複出現的總和值
    此外使用了 nonlocal 以方便更新, 也可以直接使用 Counter, 應該會更輕鬆
    總結一下, 用 DFS 以後序的方式探索整棵樹中的每個節點
    從根結點開始走回 root
    若探索到空值, 則回傳 0
    若當前節點非空, 則回傳root.val + func(left) + func(right)
    回傳前, 要將當前的總和放在一個 dictionary 中記錄每個總和出現的次數
    最後收尾的部分有兩種寫法
    一個是隨著探索的過程中, 每當更新 dictionary 時就注意這個總和的出現次數是否比我目前看過的最多次還多
    如果更多, 我就拿一個 list 把總和值裝起來, 更希目前我看過最多次的次數
    如果一樣, 就把這個總和放進該 list
    另外一種方法是最後離開 dfs 後, 所有數值都記錄在 dictionary 了
    找出其中出現次數最多的次數, 回傳 dictionary 中, 所有出現次數為該次數的總和值
    ```
#### [112. Path Sum](https://leetcode.com/problems/path-sum/description/) (Tree, DFS)
* 題目: 給一二元樹及一數字 ```n```, 試問此二元樹的任一葉節點到根節點的總和內是否包含 ```n```
* Example 1:
    ```
    Given the below binary tree and sum = 22,

          5
         / \
        4   8
       /   / \
      11  13  4
     /  \      \
    7    2      1
    return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
    ```
* 解法簡述:
    ```
    本題可以使用 DFS + Recursion 解
    作法大致相同, 但有些小技巧可以讓我們比較好寫
    首先以範例來說, 當 sum = 22 , root.val = 5, 我們要往下找
    這其實也把題目抽換成 
        sum = sum - root.val, root = root.left 然後 DFS 往下找
        sum = sum - root.val, root = root.right 然後 DFS 往下找
    如此一來, 當我們遇到以下狀況
        當前節點為葉節點, 也就是沒有 right 及 left, 且 sum == root.val
        這個時候我們又可以回傳 True, 但為求方便我們可以直接回傳 sum == root.val\
    這樣我們只要用 DFS 往下走, 然後沿路將 sum 減去當前的 root.val
    只要最後我們遇到任一葉節點是回傳 True, 就可以回傳 True 了
    所以我們只要回傳 func(root.left, sum-root.val) or func(root.right, sum-root.val) 就可以
    ```
#### [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/description/) (Tree, DFS)
* 題目: 題目和上題類似, 不同的是要求回傳所有符合條件的數列
* Example 1:
    ```
    Given the below binary tree and sum = 22,

          5
         / \
        4   8
       /   / \
      11  13  4
     /  \    / \
    7    2  5   1
    Return:

    [
        [5,4,11,2],
        [5,8,4,5]
    ]
    ```
* 解法簡述:
    ```
    本題解法和上一題很像, 但是這次要記錄目前走過的值的數列
    我的解法在 dfs 中傳遞一個 current 陣列
    對每個節點, 
    如果這個節點是葉節點, 確認 sum(current) + root.val 是否就是指定的 sum
    若是則將其加入另一陣列 ret, 若否則離開
    若此節點不是葉子節點, 則將當前值加入 current 繼續往下探索, 可以寫成這樣
        if root.left: go(current+[root.val], root.left)
        if root.right: go(current+[root.val], root.right)
    這邊有很多方法可以減少運算量, 像是
    1) 如果當前節點只有一個孩子, 就只需要往那邊探索
    2) 如果sum(current)已經超過指定 sum, 就可以不用往下探索...等
    總之等到 DFS 探索完所有葉節點後, 
    ret 就會包含所有總和等同指定 sum 的 從root 到 leaf 之路徑數列
    ```
#### [437. Path Sum III](https://leetcode.com/problems/path-sum-iii/description/) (Tree)
* 題目:延續上兩題, 但這次路徑不需要經過 root 及 leaf, 找出所有總和為指定整數的路徑之數量
* Example 1:
    ```
    root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

          10
         /  \
        5   -3
       / \    \
      3   2   11
     / \   \
    3  -2   1

    Return 3. The paths that sum to 8 are:

    1.  5 -> 3
    2.  5 -> 2 -> 1
    3. -3 -> 11
    ```
* 解法簡述:
    ```
    有兩種解法, 一個是很慢的 dfs + recursion, 另外一個是結合 dictionary 來解
    1) 解法很直覺, 因為現在不需要從 root 開始
       可以用 DFS 往下走的過程中, 把每個點都當成 root, 重新呼叫一次
       這邊我們要有兩個函數, 
       1) 一個負責把現在的點當成 root, 
          找出從該點往下是否有符合指定 sum 的路徑, 若有就 + 1
          基本上就是 112. PathSum 的作法, 只是不需要檢查是否當前為葉節點
          最後回傳以當前節點為 root 的時候, 下面出現過幾次指定 sum
       2) 一個負責 DFS 往下走過所有點, 在每一個節點都呼叫 
          func1(root) 然後往左右孩子繼續探索
          也就是 func2(root.left), func2(root.right)
          由於 func1 會回傳出現次數, 而 func2 會往下呼叫 func1
          所以這個函數最後應該就直接回傳
          func1(root) + func2(root.left) + func2(root.right)
    2) 用 dictionary 紀錄當前路徑上看過了那些 sum
       想法是這樣的, 由於已經不限定 root 跟 leaf
       所以在使用 DFS 往下探索時, 只要知道一路上走來我們總共看過了那些 sum
       就好, 用上面的範例來說, 我們接下來要沿著最左邊的 [10, 5, 3, 3] 走
       每走一步, 我們就在 dict 中增加當前 sum 值出現的次數, 也就是 d[current_sum] += 1
       所以當我走到 10, 5, 3 的時候
       我的字典中應該出現了 0, 10, 15, 18, 這四個數字為 key, value 為出現次數, 也就是 1
       0 就是還沒開始走的時候的初始值, 接著重點來了, 當我每次 d[current_sum] += 1 的時候
       我就去檢查當前的 d[current_sum - sum] 是否存在, 這表示說
       d[我目前的總和 - 指定總和], 也就是說
       如果我目前的總和扣去指定總和存在於我之前看過的總和
       就表示我如果我目前的總和中之前看過的某一段拔掉, 其實就是指定總和了
       回到範例, 當我走到 10, 5, 3 的時候 , d.keys = [0, 10, 15, 18]
       而指定總合為 8, 我去檢查 18-8 = 10 是否存在於 d, 也發現的確之前有出現過一次
       也就是說我目前走的路徑中 [10, 5, 3] 扣掉之前看過的某段總和 [10]
       也就是 [5, 3] 其實就是我要找的總合為 8 的路徑, 也就是所求
       這個想法有點像數列任兩點之間的總和
       可以藉由把 0~0 ~ 0~n 的總和先求出來, 然後如果要求 i, j 之間的和
       就回傳 sum(0~i-1) 和 sum(0~j) 相減就可以了
       如此一來我們只要一次 dfs 就可以找到所有符合指定 sum 的數量了
    ```
#### [671. Second Minimum Node In a Binary Tree](https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/) (Tree)
* 題目: 給一特別二元樹, 此二元樹的每個節點必定只有 0 或 2 個孩子, 當其有 2 個孩子時, 其值必小於等於其兩孩子的值, 請找出此樹中第二小的值
* Example 1:
    ```
    Input: 
      2
     / \
    2   5
       / \
      5   7

    Output: 5
    Explanation: The smallest value is 2, the second smallest value is 5.
    ```
* Example 2:
    ```
    Input: 
      2
     / \
    2   2

    Output: -1
    Explanation: The smallest value is 2, but there isn't any second smallest value.
    ```
* 解法簡述:
    ```
    解法可以用 DFS 或 BFS
    簡單來說就是先將 root 設為 first_min
    接著往下尋找, 只要比 first_min 還大, 就放到另外一個 list
    最後從 list 找出最小的, 就一定是第二小的值
    如果 list 為空, 就表示所有值都跟 first_min 一樣大, 回傳 -1
    ```
#### [865. Smallest Subtree with all the Deepest Nodes](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/) (Tree)
* 題目: 給一二元樹, 請回傳包含所有最深節點的最小子樹
* Example 1:
    ![](pics/865.png)
    ```
    Input: [3,5,1,6,2,0,8,null,null,7,4]
    Output: [2,7,4]
    Explanation:
    We return the node with value 2, colored in yellow in the diagram.
    The nodes colored in blue are the deepest nodes of the tree.
    The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
    The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
    Both the input and output have TreeNode type.
    ```
* 解法簡述:
    ```
    本題解法有二, 1 是先標註各點的深度, 2 是直接遞迴
    方法 1 重點在於先用 DFS 找出最深的 Node 有多深
    這邊用 dictionary 紀錄每個走過的點的深度 -> d[Node] = d[Parent]+1
    然後我們找出dict中最深的深度, 下記 max_depth, 接著進入第二個 DFS
    若當前點為空, 或是當前點深度為 max_depth, 回傳 root
    如果不符合上述狀況, 就繼續往下探索 left, right
    此時 left, right 的回傳只會有 3 種狀況:
    1) left, right 都非空, 這表示這兩個子樹下面都有深度最深的點
       所以回傳 root 就可以包含這兩邊的最深葉節點
    2) left, right 其中一個為空, 這表示只有 left 或 right 包含到最深葉節點, 故回傳非空者
    3) left, right 都是空值, 這表示這兩個子樹下面都沒有最深葉節點, 所以回傳 None
    如此一來, 當前節點回傳至父節點時, 會有 2 種狀況
    1) 回傳有值, 當前表示子樹下有最深的點
    2) 回傳 None, 表這個子樹下無最深的點
    ```
#### [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/description/) (Tree)
* 題目: 給兩二元樹 ```s``` 及 ```t```, 請回答 t 是否可能就是 s 的子樹
* Example 1:
    ```
    Given tree s:

        3
       / \
      4   5
     / \
    1   2
    Given tree t:
      4 
     / \
    1   2
    Return true, because t has the same structure and node values with a subtree of s.
    ```
* Example 2:
    ```
    Given tree s:

        3
       / \
      4   5
     / \
    1   2
       /
      0
    Given tree t:
      4
     / \
    1   2
    Return false.
    ```
* 解法簡述:
    ```
    本題問題是要問t完美符合s的子樹, 不能夠只是中間的部分
    需要問結構是否相同的題目都可以用將樹結構轉換成字串的方式來解
    需要注意的是, 因為一般的字串表示會跳過空值, 也不會明確顯示根節點, 左子樹及右子樹的差別
    所以需要在字串中穿插一些符號使其能表達更多資訊
    用範例來說的話, s 如果不加上額外符號就會是 34125
    如果補上 None 的話就會是 341##2##5##
    如果再補上左右樹以及 root 就是 ^3/^4/^1/#\#\^2/#/#\^5/#\#
    而 t 會是 ^4/^1/#\#\^2/#\#
    這樣只要檢查是否 t 字串是否為 s 字串的子字串就好了
    當然符號可以自己隨便定義, 只要可以
    1) 區分左右樹
    2) 區分一般值跟None
    應該就可以了
    ```
#### [404. Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/description/) (Tree)
* 題目: 給一二元樹, 找出所有左邊葉節點的值之總和
* Example 1:
    ```
    Example:

      3
     / \
    9  20
      /  \
     15   7

    There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
    ```
* 解法簡述:
    ```
    本題重點在於, 節點本身沒辦法區分自己是左孩子還是右孩子
    所以必須在 root 的時候檢查左邊孩子是否為葉節點還是一般節點
    檢查的方法很簡單, 就是確認 root.left.left and root.left.right
    這題也是使用 DFS 解, 對每個節點
    如果當前為空, 回傳 0
    如果當前左孩子為葉節點, 則回傳 root.left.val + func(root.right)
    若左孩子是一般節點 則回傳 func(root.left) + func(root.right)
    如此一來就可以確保不會進到左葉節點但是可以取值, 同時又繼續往右節點探索
    ```
#### [129. Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/description/)
* 題目: 給一二元樹, 將所有從 root 到 leaf 的路徑轉換成十進位的數字, 回傳所有葉的總和
* Example 1:
    ```
    Input: [1,2,3]
      1
     / \
    2   3
    Output: 25
    Explanation:
    The root-to-leaf path 1->2 represents the number 12.
    The root-to-leaf path 1->3 represents the number 13.
    Therefore, sum = 12 + 13 = 25.
    ```
* Example 2:
    ```
    Input: [4,9,0,5,1]
      4
     / \
    9   0
       / \
      5   1
    Output: 1026
    Explanation:
    The root-to-leaf path 4->9->5 represents the number 495.
    The root-to-leaf path 4->9->1 represents the number 491.
    The root-to-leaf path 4->0 represents the number 40.
    Therefore, sum = 495 + 491 + 40 = 1026.
    ```
* 解法簡述:
    ```
    本題可以使用 DFS + recursion 來解
    使用前序的方式來找, 對每個節點
    呼叫 dfs 時傳入當前累計的數值
    進入函式後先將 num = num * 10 + root.val
    接著若當前節點為葉節點, 則將累計的 num 加入到另一個陣列 ret
    但如果當前節點非葉節點, 則往其孩子繼續探索
    當離開 dfs, ret 就保存了所有葉節點到 root 的數值
    最後只要回傳 sum(ret) 即可
    ```
#### [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/description/) (Tree, DFS, BFS)
* 題目: 給一二元樹, 請回答此二元樹是否為左右對稱
* Example 1:
    ```
    this binary tree [1,2,2,3,4,4,3] is symmetric:

        1
       / \
      2   2
     / \ / \
    3  4 4  3
    ```
* Example 2:
    ```
    the following [1,2,2,null,3,null,3] is not:
      1
     / \
    2   2
     \   \
      3   3
    ```
* 解法簡述:
    ```
    本題解法非常直覺, 應該可以用 DFS 或 BFS 解
    這邊我的解法是 BFS
    在探索每一層的時候, 都將當中每個節點的值取出放在另一個陣列 val
    接著檢查 val == val[::-1], 只有前後順序相同才會是對稱的
    如果不同就回傳 False
    接著就照普通的 BFS, 更新下一層的節點
    最後如果離開迴圈, 就回傳 True
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