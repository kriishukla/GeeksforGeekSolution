<h2><a href="https://www.geeksforgeeks.org/problems/three-sum-closest/1?page=1&category=Hash&company=Microsoft,Google&difficulty=Medium,Hard&sortBy=submissions">Three Sum Closest</a></h2><h3>Difficulty Level : Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an array,&nbsp;<strong>Arr</strong>&nbsp;of <strong>N</strong> integers, and another number <strong>target</strong>, find three integers in the array such that their sum is closest to the target. Return the sum of the three integers.<br></span><span style="font-size: 18px;">Note: If there are multiple solutions, print the maximum one.</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>N = 6, target = 2
Arr[] = {-7,9,8,3,1,1}
<strong>Output: </strong>2<strong>
Explanation: </strong>There is one triplet with sum2 in the array. Triplet elements are -7,8,1 whose sum is 2.</span>
</pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>N = 4, target = 13
Arr[] = {5,2,7,5}
<strong>Output: </strong>14<strong>
Explanation: </strong>There is one triplet with sum 12 and other with sum 14 in the array. Triplet elements are 5, 2, 5 and 2, 7, 5 respectively. Since abs(13-12) ==abs(13-14) maximum triplet sum will be preferred i.e 14.</span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>Complete&nbsp;<strong>threeSumClosest()</strong> function, which takes an integer array&nbsp;<strong>Arr&nbsp;</strong>and an integer <strong>target </strong>as input, and returns the expected answer.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:&nbsp;</strong>O(N*N).<br><strong>Expected Auxiliary Space:&nbsp;</strong>O(1).</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>3 ≤ N ≤ 10<sup>3</sup><br>-10<sup>5</sup> ≤ A[i] ≤ 10<sup>5</sup><br>1 ≤ target&nbsp;≤ 10<sup>5</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>Google</code>&nbsp;<code>Apple</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Hash</code>&nbsp;<code>Data Structures</code>&nbsp;