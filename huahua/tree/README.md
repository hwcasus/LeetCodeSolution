# Tree

## Strategy

大多都是用 BFS / DFS 去解

DFS 問題很明顯, 常用的解法是

* 先決定每個節點上可以回答 / 必須回答甚麼問題
* 依照 None 節點 -> Leaf 節點 -> Parent 節點的順序, 定義每個 node 該怎麼 return

## The List

|Id|Name|Difficulty|Similar Problems|Comments|
|-|-|-|-|-|
|94|Binary Tree Inorder Traversal|★|144, 145, 429, 589, 590, 987, 1302|traversal|
|100|Same Tree|★★|101,104,110,111,572,965||
|102|Binary Tree Level Order Traversal|★★|107,429,872|collecting nodes|
|814|Binary Tree Pruning|★★★|669,1325| |
|112|Path Sum|★★★|113,437| |
|129|Sum Root to Leaf Numbers|★★★|257| |
|236|Lowest Common Ancestor of a Binary Tree|★★★|235| |
|297|Serialize and Deserialize Binary Tree|★★★|449| |
|508|Most Frequent Subtree Sum|★★★|||
|124|Binary Tree Maximum Path Sum|★★★|543,687|Use both children, return one|
|968|Binary Tree Cameras|★★★★|337,979||

## Memorable

| Title | Difficulty |
| - | - |
|[987. Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/)|Hard|
|[100. Same Tree](https://leetcode.com/problems/same-tree/)|Easy|
|[101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)|Easy|
|[111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)|Easy|
|[572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)|Easy|
|[872. Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/)|Easy|
|[814. Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/)|Easy|
|[669. Trim a Binary Search Tree](https://leetcode.com/problems/trim-a-binary-search-tree/)|Medium|
|[236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)|Medium|
|[124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)|Hard|
|[687. Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)|Medium|
|[968. Binary Tree Cameras](https://leetcode.com/problems/binary-tree-cameras/)|Hard|
|[337. House Robber III](https://leetcode.com/problems/house-robber-iii/)|Medium|
|[979. Distribute Coins in Binary Tree](https://leetcode.com/problems/distribute-coins-in-binary-tree/)|Medium|

---

### 987. Vertical Order Traversal of a Binary Tree

本題想法為 BFS 走過所有節點, 可以分辨出 node 的 row 值
此外不只節點也要順便紀錄其 column 值
```python
    queue = [(0, root)]  # <--- (column, )
    while queue:
```
BFS 走過的時候, 將同一 column 的 node 用 dict 記錄起來
最後再將其同一 column 的值根據 node val 排序即可

---

### 100. Same Tree

本題想法簡單, 但一開始沒想出來就特別紀錄一下
每個節點只要考慮是否跟另外一個節點相同, 包含
* p.val == q.val
* p is None and q is None
此外的情況就是判斷子樹是否相同

---

### 101. Symmetric Tree

題目與第 100 題十分相似,
唯一差別在於判斷子樹時, 要將順序反過來
左節點的左樹應該要和右節點的右樹相比

---

### 572. Subtree of Another Tree

本題解法可以套用在很多類似的題目上
你需要做兩件事
1. 比較兩棵樹是否完全一樣
2. 對每個節點都要這樣比較一次

所以需要結合兩個 dfs
一個走過所有節點
一個比較兩個樹是否相同

但也有一個特別的做法就是 tree encoding

將樹用 inorder 的方式 encoding
```python
def to_str(n):
    return '^' + str(n.val) + '/' + to_str(n.left) +'\\'+ to_str(n.right) if n else '#'
```
這樣子樹 string 一定會是母樹 string 的 substring

---

### 872. Leaf-Similar Trees

本題特別的是雖然要找 Leaf node 但不能 BFS, 因為是要找不同層的 Leaf Node
解法本身不會很困難, DFS 用 inorder 走過 Leaf Node 時紀錄值就可以了

---

### 814. Binary Tree Pruning

本題想法為 DFS postorder 走過所有 node
只要走到 leaf node 且值為 0 就回傳 None, 若非 leaf node 或值為 1 則回傳自己
再透過 assignment
```python
root.left = helper(root.left)
```
來逐步地達到 node pruning

---

### 669. Trim a Binary Search Tree

本題主要想法為, 當一個 node 被移除時, 需要將其 child node 拉上來取代它的位置
舉例來說 若一 node A 為另一 node B 的 left child node, 當他要被移除時
需要把 A 的 child node 拉上來成為變成 B 的 left child node

其他就很簡單, dfs 走過, 當本身大於指定範圍時, 將其 left child 拉上來
反之若是小於指定範圍, 則使用 right child.

---

### 236. Lowest Common Ancestor of a Binary Tree

這題要用 dfs 走過所有 node,
但需要想一下, 當走到某一個 node 時有哪些情況可能會發生

1. 當遇到 None 時, 回傳自己 = None
2. 當左右 child 分別(是 / 包含) p and q 時 -> 回傳自己
3. 當左右孩子其中一個(是 / 包含) p or q 時 -> 回傳 p or q
4. 當左右孩子都不 (是 / 包含) p or q 時 -> 回傳 None

整理一下就會是這 4 條規則, 舉例來說
當我走到一個節點時,
1. 如果我不是 Node -> 回傳 None
2. 當我是 p or q 時 -> 回傳自己
3. 當我的其中一個孩子是 p / q 時
   -> 表示該 node 下面只有 p / q 其中一個
   -> 表示該 node 不是 LCA -> 回傳 p / q, 告訴我的父 node 這裡有 p / q
4. 當我的兩個 child node 分別有找到 p and q
   -> 找到了 LCA -> 告訴父 node 我就是答案 -> 回傳自己
   -> 同時 父節點的另外一個孩子一定找不到 p and q 所以一定回傳 None
   -> 所以父節點也會回傳目前節點

---

### 124. Binary Tree Maximum Path Sum

這題也用 dfs, 但要記住的是因為是 path, 所以只能選擇
1. 自己從左孩子連向右孩子
2. 自己從父親連向左或右孩子
所以每個節點要回答的問題是

1. 如果是子節點, 回傳自己的 val
2. 如果是父節點, 我得考慮上面兩種情況
   1. 考慮如果左右孩子互連, 這個連法在這裡就結束了
      所以得紀錄 左孩子回傳值 + 右孩子回傳值 + 自己的值
   2. 考慮自己作為父親的孩子, 若與父親相連可能最大值
      也就是 自己的值 + max(左孩子回傳值, 右孩子回傳值)

---

### 687. Longest Univalue Path

本題想法和 124 類似, 一樣必須考慮到
1. 自己從左孩子連向右孩子
2. 自己從父親連向左或右孩子

所以一個節點當擔任的是父節點的時候, 要最大可能長度為 1 + 左 + 右
而若是擔任子節點的時候, 則只能選 1 + max(左, 右)

除此之外, 在計算長度前, 也要先比對左右子樹與自己的值是否相同
若不同則可將長度設為 0

---

### 968. Binary Tree Cameras

本題相當有趣, 我的解法為定義三種狀態
(在別人的解法中 我有看過一樣三種但定義不同的狀態)
1. None 節點
2. Leaf 節點
3. Camera 節點

首先根據定義, 當一個節點被設置成 Camera, 他的父節點跟子節點就會被 Covered
所以我們可以有一個很直覺的想法就是, 設置在葉節點上面是非常浪費的, 最好是可以設置在葉節點上一層
依此我們可以整理出四個回傳規則, 根據其重要性排序為

1. 若自己為 None, 回傳自己為 None 節點
2. 若兩個孩子皆為 None 節點時, 回傳自己是Leaf 節點
3. 若任一孩子為 Leaf 節點, 則回傳自己為 Camera 節點, Camera Count ++
4. 若任一孩子為 Camera 節點, 則因自己已經被 Covered
   父節點可以不用考慮自己, 可視為 None 節點回傳

根據這四個規則, 就足以解決本題
要注意 一定要先判斷是否有孩子為 leaf 節點, 才判斷孩子是否為 Camera 節點
因為若有 leaf child 節點, 則必須設置 camera 才能 covered.
而不管設置在 leaf child 還是自己, 從數量上是沒有任何變化的

```python
left_state, right_state = helper(root.left), helper(root.right)

if left_state == IS_NONE and right_state == IS_NONE:
   return IS_LEAF
elif left_state == IS_LEAF or right_state == IS_LEAF:
   self.count += 1
   return IS_SET
elif left_state == IS_SET or right_state == IS_SET:
   # if one of leaf is set, we will take this node as none node
   return IS_NONE
```

---

### 337. House Robber III

本題與 968 類似, 都是要考慮選擇孩子還是選擇自己, 但解法不太一樣
每個節點要考慮的問題為 - 「該不該搶這間房子」
這個問題對應的選擇為
1. 搶這個房子 -> 不能搶我的孩子 -> 只能搶我孩子的孩子 -> 搶自己 + 孩子的孩子 的最大值
2. 不搶這個房子 -> 能搶我的孩子 -> 搶兩個孩子的最大值

這兩種選擇的結果是每個節點必須回傳給父節點的答案,
也就是說每個節點回傳 (搶自己+孩子的孩子的值, 搶孩子的值)
而當這兩個值回到父節點時, 就會變成 (搶孩子的值, 搶孩子的孩子的值)
要注意的是, 如果選擇搶孩子還是要比較搶孩子 / 搶孩子的孩子 哪個比較划算

```python
left_pick_self, left_pick_child = helper(root.left)
right_pick_self, right_pick_child = helper(root.right)

pick_self = root.val + left_pick_child + right_pick_child
pick_any_child = max(left_pick_self, left_pick_child) + max(right_pick_self, right_pick_child)

return pick_self, pick_any_child
```

---

### 979. Distribute Coins in Binary Tree

這題也挺有趣的, 花了我一點時間想
由於題目已經保證, 只要硬幣平均分配的話, 一定會滿足每個節點都有一枚金幣

所以每個節點要回答的問題其實是
> 把這個節點變成 1 的話需要動幾個硬幣
這個答案就等於 (node.val - 1)
同時也需要考慮到子樹的問題, 就會變成
> 把這個節點以下的子樹全部變成 1 的話要總共要動幾個硬幣

而每個節點要回傳的就是實際上滿足這個條件還需要幾個硬幣
結合兩者, 大概會是這樣
```python
def helper(root):
   if not root:
         return 0

   left = helper(root.left)
   right = helper(root.right)

   required = (root.val - 1) + left + right
   self.moves += abs(required)
   return required
```

---