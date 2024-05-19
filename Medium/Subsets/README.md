<h2><a href="https://www.geeksforgeeks.org/problems/subsets-1613027340/1?page=2&category=Recursion&company=Microsoft,Google&sortBy=submissions">Subsets</a></h2><h3>Difficulty Level : Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given a set of positive integers, find <strong>all its subsets</strong>.</span></p>
<p><strong><span style="font-size: 18px;">Example 1 :</span></strong></p>
<pre><span style="font-size: 18px;"><strong>Input :</strong> </span>
<span style="font-size: 18px;">array = {1, 2, 3}</span>
<strong><span style="font-size: 18px;">Output :</span></strong>
<span style="font-size: 18px;">// this space denotes null element. 
1
1 2
1 2 3
1 3
2
2 3
3</span>
<strong><span style="font-size: 18px;">Explanation: </span></strong>
<span style="font-size: 18px;">The following are the subsets 
of the array {1, 2, 3}.</span></pre>
<p><strong><span style="font-size: 18px;">Example 2 :</span></strong></p>
<pre><strong><span style="font-size: 18px;">Input :</span></strong>
<span style="font-size: 18px;">array = {1, 2}</span>
<strong><span style="font-size: 18px;">Output :
</span></strong><span style="font-size: 18px;">
1 
1 2
2</span>
<strong><span style="font-size: 18px;">Explanation :</span></strong>
<span style="font-size: 18px;">The following are the 
subsets of {1, 2}.</span></pre>
<div><strong><span style="font-size: 18px;">Your task :</span></strong></div>
<div><span style="font-size: 18px;">You don't have to read input or print anything. Your task is to complete the function <strong>subsets()</strong> which takes the array of integers as input and returns the list of lists containing the subsets of the given set of numbers in lexicographical order.</span></div>
<div>&nbsp;</div>
<div><span style="font-size: 18px;"><strong>Expected Time Complexity :</strong> O(2<sup>n</sup>)</span></div>
<div><span style="font-size: 18px;"><strong>Expected Auxiliary Space :</strong> O((</span><span style="font-size: 18px;">2</span><sup>n</sup><span style="font-size: 18px;">)</span><span style="font-size: 18px;">*length of each subset)</span></div>
<div>&nbsp;</div>
<div><strong><span style="font-size: 18px;">Constraints :</span></strong></div>
<div><span style="font-size: 18px;">1 &lt;= n &lt;= 15</span></div>
<div><span style="font-size: 18px;">1 &lt;= arr[i] &lt;=10<sup>4</sup></span></div></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Microsoft</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Recursion</code>&nbsp;<code>Backtracking</code>&nbsp;<code>Algorithms</code>&nbsp;