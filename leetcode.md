- [1. 滑动窗口](#1-滑动窗口)
- [2. 双指针](#2-双指针)
- [3. 快慢指针/ 链表题目](#3-快慢指针-链表题目)
- [4. 原地链表翻转](#4-原地链表翻转)
- [5. 区间合并](#5-区间合并)
- [6. 无序限定范围的数组元素查找O(N）](#6-无序限定范围的数组元素查找on)
- [7. BFS](#7-bfs)
- [8. 树的DFS](#8-树的dfs)
- [9. DFS/递归/回溯法](#9-dfs递归回溯法)
- [10. 双堆模式](#10-双堆模式)
- [11. 2分变种](#11-2分变种)
- [12. 前K大的数模式HEAP](#12-前k大的数模式heap)
- [13. K路归并](#13-k路归并)
- [14. DP 动态规划](#14-dp-动态规划)
- [15. 排序算法](#15-排序算法)
- [16. 树和链表结合](#16-树和链表结合)
- [17. 树的重新构建](#17-树的重新构建)
- [18. 位运算](#18-位运算)
- [19. 字符串](#19-字符串)
- [20. stack](#20-stack)
- [21. math](#21-math)
- [22. array](#22-array)
- [23. 二叉搜索树](#23-二叉搜索树)
- [ref](#ref)
# 1. 滑动窗口

[53. 大小为 K 的子数组的最大和](https://leetcode.com/problems/maximum-subarray/)

[121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

[3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

[239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

[剑指 Offer 57 - II. 和为s的连续正数序列](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/shi-yao-shi-hua-dong-chuang-kou-yi-ji-ru-he-yong-h/)

# 2. 双指针

双指针通常用在**排好序**的数组或是链表中寻找对子, 或者是merge 或者是排序，或者去除element，反正一般都是头尾各一个指针，然后根据条件移动。【参考[Jaylen's Blog](https://linzhenglearn.github.io/2017/03/29/TwoPointer/#常见题型)】
[1. Two Sum](https://leetcode.com/problems/two-sum/)（# 也可以用map的方式做）

[167. Two Sum II - Input array is sorted](https://leetcode.com/submissions/detail/299213003/)

[977. Squares of a Sorted Array (很像merge sort里的merge）](https://leetcode.com/problems/squares-of-a-sorted-array/)

[283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)

[27. Remove Element](https://leetcode.com/problems/remove-element/)

[26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

[16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/)

[18. 4Sum](https://leetcode.com/problems/4sum/)

[86. Partition List](https://leetcode.com/problems/partition-list/)

[11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

[42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

[75. Sort Colors](https://leetcode.com/problems/sort-colors/)

[剑指 Offer 04. 二维数组中的查找](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/)

[剑指 Offer 21. 调整数组顺序使奇数位于偶数前面](https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/)
# 3. 快慢指针/ 链表题目
快慢指针是处理linked list常用的套路，通常是用来判断成环以及环的入口，或者是寻找 list中第k个元素。

[141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

[142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

[234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

[61. Rotate List](https://leetcode.com/problems/rotate-list/)

[剑指 Offer 18. 删除链表的节点](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/)

[JZ56 删除链表中重复的结点](https://www.nowcoder.com/practice/fc533c45b73a41b0b44ccba763f866ef?tpId=13&&tqId=11209&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking)

[剑指 Offer 22. 链表中倒数第k个节点](https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/)

[剑指 Offer 35. 复杂链表的复制](https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/)

[剑指 Offer 52. 两个链表的第一个公共节点](https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/)

# 4. 原地链表翻转

[234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

[206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

[25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)

[92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)

# 5. 区间合并
区间合并的问题，通常是重新把区间按照start和end排序，重新组合区间。

[56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)

[986. Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)

[57. Insert Interval](https://leetcode.com/problems/insert-interval/)

# 6. 无序限定范围的数组元素查找O(N）

要求 inplace， 通常是采用正负反转的做法

[41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/)

[448. Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)

[剑指 Offer 03. 数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/)

# 7. BFS

BFS 通常采用queue 来实现

[102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

[103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

[297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

[127. Word Ladder I ](https://leetcode.com/problems/word-ladder/)

[207. Course Schedule](https://leetcode.com/problems/course-schedule/)【拓扑排序】


# 8. 树的DFS
通常采用递归
[111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

[112. Path Sum](https://leetcode.com/problems/path-sum/)

[113. Path Sum II](https://leetcode.com/problems/path-sum-ii/)（和[剑指 Offer 34. 二叉树中和为某一值的路径](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/)一样）

[437. Path Sum III](https://leetcode.com/problems/path-sum-iii/submissions/)

[100. Same Tree](https://leetcode.com/problems/same-tree/)

[101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

[104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

[110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

[剑指 Offer 26. 树的子结构](https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/)

[剑指 Offer 33. 二叉搜索树的后序遍历序列](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/)


[剑指 Offer 54. 二叉搜索树的第k大节点](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/)(inorder)

# 9. DFS/递归/回溯法

对于排列和组合的题目，需要主要判断是否会有重复数字，如有重复，需要先进行sort，而且需要进行剪枝。

[78. Subsets](https://leetcode.com/problems/subsets/)

[90. Subsets II](https://leetcode.com/problems/subsets-ii/)

[46. Permutations](https://leetcode.com/problems/permutations/)

[47. Permutations II](https://leetcode.com/problems/permutations-ii/)

[39. Combination Sum](https://leetcode.com/problems/combination-sum/)

(区别 [322. Coin Change](https://leetcode.com/problems/coin-change)

[518. Coin Change 2](https://leetcode.com/problems/coin-change))

[40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)

[131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) !

[17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) (differ from [91. Decode Ways](https://leetcode.com/problems/decode-ways/))

[79. Word Search](https://leetcode.com/problems/word-search/)(same as 剑指 Offer 12. 矩阵中的路径)

[剑指 Offer 13. 机器人的运动范围](https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/)

# 10. 双堆模式

通常是查找中位数，构建一个最小堆和最大堆。
以及查找数据流中最小的或者最大的数。

[295 Find-Median-from-Data-Stream](https://leetcode.com/problems/find-median-from-data-stream/)

[480. Sliding Window Median](https://leetcode.com/problems/sliding-window-median/)

[155. Min Stack](https://leetcode.com/problems/min-stack/)

[剑指 Offer 09. 用两个栈实现队列](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/)

# 11. 2分变种

> 当你需要解决的问题的输入是排好序的数组，链表，或是排好序的矩阵，要求咱们寻找某些特定元素。这个时候的不二选择就是二分搜索。这种模式是一种超级牛的用二分来解决问题的方式。
对于一组满足上升排列的数集来说，这种模式的步骤是这样的：
首先，算出左右端点的中点。最简单的方式是这样的：middle = (start + end) / 2。但这种计算方式有不小的概率会出现整数越界。因此一般都推荐另外这种写法：middle = start + (end — start) // 2
如果要找的目标改好和中点所在的数值相等，我们返回中点的下标就行
如果目标不等的话：我们就有两种移动方式了
如果目标比中点在的值小（key < arr[middle]）：将下一步搜索空间放到左边（end = middle - 1）
如果比中点的值大，则继续在右边搜索，丢弃左边：left = middle + 1
图示该过程的话，如下图所示：
我习惯的循环结束条件是 $start + 1 < end$, 然后在分别判断start 和 end 的结果
[参考Jaylen's Blog](https://linzhenglearn.github.io/2017/03/20/BinarySearch/)
[参考模版](https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/)

[35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)

[34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

[33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/)

[153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

[154. Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/submissions/)(same as [剑指 Offer 11. 旋转数组的最小数字])

[162. Find Peak Element](https://leetcode.com/problems/find-peak-element/?utm_source=LCUS&utm_medium=ip_redirect_q_uns&utm_campaign=transfer2china)

[540. Single Element in a Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array/)

[剑指 Offer 16. 数值的整数次方](https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/)(2分法)

# 12. 前K大的数模式HEAP

采用priority queue 或者 说在python 中的heapq
求top k 采用最小堆（默认）
采用最大堆的时候可以采用push 负的value

[215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

[347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

[373. Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)

# 13. K路归并

K路归并能帮咱们解决那些涉及到多组排好序的数组的问题。

每当你的输入是K个排好序的数组，你就可以用堆来高效顺序遍历其中所有数组的所有元素。你可以将每个数组中最小的一个元素加入到最小堆中，从而得到全局最小值。当我们拿到这个全局最小值之后，再从该元素所在的数组里取出其后面紧挨着的元素，加入堆。如此往复直到处理完所有的元素。

特殊情况：2路并归 （mergesort 中的merge， 双指针就可以完成）

[23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

[21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)


# 14. DP 动态规划
参考：https://zhuanlan.zhihu.com/p/91582909
参考：https://zhuanlan.zhihu.com/p/126546914

[300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

[1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)

[72. Edit Distance](https://leetcode.com/problems/edit-distance/)

[44. Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)

[10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)

[120. Triangle](https://leetcode.com/problems/triangle/)

[53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

[152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)

[887. Super Egg Drop](https://leetcode.com/problems/super-egg-drop/)[ref](https://leetcode-cn.com/problems/super-egg-drop/solution/dong-tai-gui-hua-zhi-jie-shi-guan-fang-ti-jie-fang/)

[198. House Robber](https://leetcode.com/problems/house-robber/)

[213. House Robber II](https://leetcode.com/problems/house-robber-ii/) (两个dp）

[121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

[122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)


[188. Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

[123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)   [ref](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39743/Python-DP-solution-120ms) 

[714. Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

[309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/76040/Share-my-python-solution-with-explanation)

[516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) !

[5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

[416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/submissions/)


[322. Coin Change](https://leetcode.com/problems/coin-change)

[518. Coin Change 2](https://leetcode.com/problems/coin-change-2/)

[91. Decode Ways](https://leetcode.com/problems/decode-ways/)

[139. Word Break](https://leetcode.com/problems/word-break/)

[剑指 Offer 10- I. 斐波那契数列](https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/)

[剑指 Offer 10- II. 青蛙跳台阶问题](https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/)

[矩形覆盖](https://www.nowcoder.com/practice/72a5a919508a4251859fb2cfb987a0e6?tpId=13&&tqId=11163&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking)

[变态跳台阶](https://www.nowcoder.com/practice/22243d016f6b47f2a6928b4313c85387?tpId=13&&tqId=11162&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking)

[剑指 Offer 14- I. 剪绳子](https://leetcode-cn.com/problems/jian-sheng-zi-lcof/)

[剑指 Offer 46. 把数字翻译成字符串](https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/)

[剑指 Offer 47. 礼物的最大价值](https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/)

[剑指 Offer 49. 丑数](https://leetcode-cn.com/problems/chou-shu-lcof/)

[剑指 Offer 60. n个骰子的点数](https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/)

# 15. 排序算法
[Selection Sort](#ss)
[Heapsort](#hs)
[Mergesort](#ms)
[Insertion Sort](#is)
[Shell's Sort](#shell)
[Quicksort](#qs)
[Bubblesort](#bs)
[Linear Sorting](#ls)

# 16. 树和链表结合

[剑指 Offer 36. 二叉搜索树与双向链表](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/)


[109. Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)

[114. Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

# 17. 树的重新构建
[105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal)

[106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

[606. Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree/)

[1008. Construct Binary Search Tree from Preorder Traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/)

[889.	Construct Binary Tree from Preorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal)


# 18. 位运算
[136. Single Number](https://leetcode.com/problems/single-number/)

[540. Single Element in a Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array/)

[190. Reverse Bits](https://leetcode.com/problems/reverse-bits/)

[剑指 Offer 15. 二进制中1的个数](https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/)

[剑指 Offer 56 - I. 数组中数字出现的次数](https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/)

[剑指 Offer 56 - II. 数组中数字出现的次数 II](https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/)

# 19. 字符串
一般都有很多corner cases 需要考虑
[8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)

[剑指 Offer 20. 表示数值的字符串](https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/)

[剑指 Offer 58 - I. 翻转单词顺序](https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/)(2次翻转）

[剑指 Offer 58 - II. 左旋转字符串](https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/)
# 20. stack
[剑指 Offer 31. 栈的压入、弹出序列](https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/)

# 21. math
[172. Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/)

[470. Implement Rand10() Using Rand7()](https://leetcode.com/problems/implement-rand10-using-rand7/)

# 22. array
[剑指 Offer 66. 构建乘积数组](https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/)

# 23. 二叉搜索树
[剑指 Offer 68 - I. 二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/)

[剑指 Offer 68 - II. 二叉树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/)

[二叉树的下一个结点](https://www.nowcoder.com/practice/9023a0c988684a53960365b889ceaf5e?tpId=13&&tqId=11210&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking)

# ref
[basketwangCoding Youtube link ](https://www.youtube.com/channel/UCE35PnPX7EZi8nHSegjMn6Q)

[剑指offer](https://leetcode-cn.com/problemset/lcof/)