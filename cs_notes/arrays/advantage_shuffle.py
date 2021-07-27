# 870. Advantage Shuffle
# https://leetcode.com/problems/advantage-shuffle/description/

class Solution:
    # 題目的要求如下
    # 給 2 等長 list, A & B, 將A重新排序,
    # 盡可能地使 A 的每個元素都大於 B 在同一位子上的元素
    # 要注意 B 的順序不能打亂

    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Revisit @ 20210726
        num_elements = len(nums1)
        nums1 = sorted(nums1, reverse=True)
        nums2_sorted_idx = sorted(
            [
                i for i in range(num_elements)
            ],
            key=lambda x:nums2[x],
            reverse=True
        )

        output = [None] * num_elements
        left, right = 0, num_elements - 1

        for idx in nums2_sorted_idx:
            # if current largest from nums1 > current largest from nums2
            if nums1[left] > nums2[idx]:
                output[idx] = nums1[left]
                left += 1
            else:
                output[idx] = nums1[right]
                right -= 1

        return output


    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        這邊有 greedy 的想法，簡單來說就是
        對於 B 的每個元素排序, 從大到小來比較
        只要目前A最大值 > B最大值, 那就把這個值放在這個 B 的位子
        若否，則表示這個目前 B 中最大值比 A 中最大值還大，那就給他最小的避免浪費
        """
        A.sort(reverse=True)
        C = sorted([i for i in range(len(B))], key=lambda x:B[x], reverse=True)
        ret = [None]*len(A)
        left, right = 0, len(A)-1

        for c in C:
            if A[left] > B[c]:
                ret[c] = A[left]
                left+=1
            else:
                ret[c] = A[right]
                right -=1

        return ret

    def advantageCountMe(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        不解釋了，反正很爛
        """
        A.sort(reverse=True)
        C = sorted([i for i in range(len(B))], key=lambda x:B[x], reverse=True)
        ret = [None]*len(A)
        A.append(-1)

        for c in C:
            for i in range(0, len(A)):
                if i == 0:
                    first = A[i] > B[c]
                else:
                    if (A[i] > B[c]) != first or A[i] == -1:
                        ret[c] = A[i-1]
                        A.pop(i-1)
                        break

        return ret
