# BST

## Strategy

注意一點 如果題目有提到跟順序有關的話, 可以先試試看 Inorder

>  BST 用 inorder traversal 會照大小順序走過

## The List

|Id|Name|Difficulty|Similar Problems|Comments|
|-|-|-|-|-|
|98|Validate Binary Search Tree|★★|530|inorder|
|700|Search in a Binary Search Tree|★★|701|binary search|
|230|Kth Smallest Element in a BST|★★★||inorder|
|99|Recover Binary Search Tree|★★★||inorder|
|108|Convert Sorted Array to Binary Search Tree|★★★||build BST|
|501|Find Mode in Binary Search Tree|★★★||inorder|
|450|Delete Node in a BST|★★★★||binary search|

## Memorable

99
450

---

### 98. Validate Binary Search Tree

本題考的是 BST 的基本概念
簡單來說就是 left_child.val < root.val < right_child.val

值得注意的是 這個順序其實就是 inorder (root in the middle)
很快想到的就是 inorder dfs 走下去看看是否為遞增就好
可以先全部走過把值存起來
也可以用一個 self.prev 紀錄上一個點的值
只要上一個點的值比現在的大, 就違反了 BST

---

### 530. Minimum Absolute Difference in BST
本題跟 98 一樣 使用 inorder + prev node 的作法
要注意的是他並沒有限定相鄰的Node
但是他要找的是最小的 difference of value
而 bst 裡面這個東西只會來自相鄰的 node
所以可以額外用一個 self.diff 去存最小的值

---

### 700. Search in a Binary Search Tree

本題很簡單 pre-order 走下去,
遇到 None 回傳 None
遇到 node.val 比所求大, 遞迴回傳往左邊走的結果, 反之右邊
遇到所求 Node 回傳該 Node

---

### 701. Insert into a Binary Search Tree

注意這題不只一種正解

題目本身很簡單, dfs 走下去
插入值若比 node 大往右邊走, 反之左邊
如果有孩子, 表示還要往下走
如果遇到 None, 就直接把 Node 插入在那裏

---

### 230. Kth Smallest Element in a BST

本題我有點小作弊但基本概念一樣就是

>  bst 用 inorder traversal 會照順序排列

可以用 count 去處理走過幾個節點
但我這邊是用一個 list 把每個走過的 Node 存一個 reference
最後在直接拿 list[k-1]

---

### 99. Recover Binary Search Tree

本題有先定義這邊只有兩個節點互換, 所以其實沒那麼困難
我的解法跟 230 一樣

1. 先 inorder 走過 bst, 找出正確情況下節點的順序
2. 然後再把每個節點的值拿出來檢查 看看哪兩個節點的順序不對
3. 最後在直接把兩個節點的 val 互換

如果你的解法要走完整個 tree 要注意的是第二步, 這邊是影響速度的關鍵
最好是能用 O(n) 走完所有 node, 這邊列出我參考別的人結果
有點難解釋 但簡單來說就是這是考慮兩種狀況
1. 相鄰互換
   如果是相鄰 應該只會遇到一次錯誤
   當遇到錯誤時, x, y 分別會紀錄 i, i + 1

2. 非相鄰互換
   如果是非相鄰, 那就表示一定會遇到兩次錯誤
   第一次會 x 會記錄住 i,
   第二次的時候 y 會記錄 j + 1

```python
val = [node.val for node in self.node]

n = len(val)
x = y = -1

for i in range(n - 1):
    if val[i + 1] < val[i]:
        y = i + 1
        if x == -1:
            x = i
        else:
            break
```

---

### 108. Convert Sorted Array to Binary Search Tree
本題題目有提到 必須是一個 height-balanced 的 Tree, 表示左右 child 高度差必須小於 1
而解法很簡單 就是每次都取正中間的點當 root, 然後把該點左半邊拿去建 left child tree
右邊拿去建 right child tree

要注意你可以只傳 index, 也可以傳真的切好的 array, 如果是只傳 index (如我)
大概這樣寫

```python

def helper(left, right):
    # 切到最後一定會會變成 left > right, 回傳 None 就好
    # 若 left == right, 其實是表示剩下一個節點
    if left > right:
        return None

    mid = (left + right) // 2
    root = TreeNode(nums[mid])

    # 要注意 mid 不要傳到已經用掉了
    root.left = helper(left, mid - 1)
    root.right = helper(mid + 1, right)

    return root

```

---

### 501. Find Mode in Binary Search Tree

本題是要找出最常見的 element, 如果有不同數字出現次數一樣最多
則都要回傳

我的解法很簡單 dfs 走過 tree, 用 counter 記錄出現次數
最後取得 counter 最大出現次數, 再回頭檢查 counter 裡面誰出現過這麼多次

---

### 450. Delete Node in a BST

注意一下這題跟 701 一樣, 可能有不只一種答案

但解法其實很簡單
1. 先 dfs 找到你真的要刪除的點 (以下稱 target)
2. 找到之後檢查一下 target 左右 child
3. 如果有一方為 None, 將僅存的孩子指派給 target 的 father 取代 target
4. 若兩方都非 None, 則要找一個其中一個取代 target

這邊開始會出現分歧, 我的做法是
讓 右邊孩子 去當 左邊孩子 的最右邊孩子 (左右反過來也可以)
這樣才會符合 BST

```python
# 左孩子取代 root, 右孩子溶入左孩子
succ = root.left
attach = root.right

if succ and attach:
    # 找到左孩子最右邊的點, 且其右孩子為空
    while succ.right:
        succ = succ.right

    # 將右孩子黏上去
    succ.right = attach
    return root.left
```
