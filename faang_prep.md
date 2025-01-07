Full problem list: https://leetcode.com/list/x1k8lxi5


Longest Increasing Subsequence variants:
https://leetcode.com/problems/longest-increasing-subsequence/
https://leetcode.com/problems/largest-divisible-subset/
https://leetcode.com/problems/russian-doll-envelopes/
https://leetcode.com/problems/maximum-length-of-pair-chain/
https://leetcode.com/problems/number-of-longest-increasing-subsequence/
https://leetcode.com/problems/delete-and-earn/
https://leetcode.com/problems/longest-string-chain/


Partition Subset:
https://leetcode.com/problems/partition-equal-subset-sum/
https://leetcode.com/problems/last-stone-weight-ii/


BitMasking:
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/


Longest Common Subsequence Variant:
https://leetcode.com/problems/longest-common-subsequence/
https://leetcode.com/problems/edit-distance/
https://leetcode.com/problems/distinct-subsequences/
https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/


Palindrome:
https://leetcode.com/problems/palindrome-partitioning-ii/
https://leetcode.com/problems/palindromic-substrings/


Coin Change variant:
https://leetcode.com/problems/coin-change/
https://leetcode.com/problems/coin-change-2/
https://leetcode.com/problems/combination-sum-iv/
https://leetcode.com/problems/perfect-squares/
https://leetcode.com/problems/minimum-cost-for-tickets/


Matrix multiplication variant:
https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/
https://leetcode.com/problems/burst-balloons/


Matrix/2D Array:
https://leetcode.com/problems/matrix-block-sum/
https://leetcode.com/problems/range-sum-query-2d-immutable/
https://leetcode.com/problems/dungeon-game/
https://leetcode.com/problems/triangle/
https://leetcode.com/problems/maximal-square/
https://leetcode.com/problems/minimum-falling-path-sum/


Hash + DP:
https://leetcode.com/problems/target-sum/
https://leetcode.com/problems/longest-arithmetic-sequence/
https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/


State machine:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/


Depth First Search + DP:
https://leetcode.com/problems/out-of-boundary-paths/
https://leetcode.com/problems/knight-probability-in-chessboard/


Minimax DP:
https://leetcode.com/problems/predict-the-winner/
https://leetcode.com/problems/stone-game/


Misc:
https://leetcode.com/problems/greatest-sum-divisible-by-three/
https://leetcode.com/problems/decode-ways/
https://leetcode.com/problems/perfect-squares/
https://leetcode.com/problems/count-numbers-with-unique-digits/
https://leetcode.com/problems/longest-turbulent-subarray/
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/


Sample solutions for each of above problem type:
Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/
https://leetcode.com/problems/largest-divisible-subset/
https://leetcode.com/problems/russian-doll-envelopes/
https://leetcode.com/problems/maximum-length-of-pair-chain/
https://leetcode.com/problems/number-of-longest-increasing-subsequence/
https://leetcode.com/problems/delete-and-earn/
https://leetcode.com/problems/longest-string-chain/

Partition Subset Sum:
https://leetcode.com/problems/partition-equal-subset-sum/
https://leetcode.com/problems/last-stone-weight-ii/

class Solution:
    def canPartition(self, nums):
            n = len(nums)
            
            total_sum = sum(nums)
            if total_sum % 2 != 0:
                return False
            
            target = total_sum // 2
            dp = [False] * (target + 1)
            dp[0] = True
            
            for num in nums:
                for j in range(target, num - 1, -1):
                    dp[j] = dp[j] or dp[j - num]
            
            return dp[target]

BitMasking in DP:
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/


def canPartitionKSubsets(self, nums, k):
        n = len(nums)
        
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        
        target = total_sum // k
        dp = [-1] * ((1 << n) + 2)
        dp[0] = 0
        
        for mask in range(1 << n):
            if dp[mask] == -1:
                continue
            for i in range(n):
                if not (mask & (1 << i)) and dp[mask] + nums[i] <= target:
                    dp[mask | (1 << i)] = (dp[mask] + nums[i]) % target
        
        return dp[(1 << n) - 1] == 0

Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/
https://leetcode.com/problems/edit-distance/
https://leetcode.com/problems/distinct-subsequences/
https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

class Solution:
    def longestCommonSubsequenceUtil(self, text1: str, text2: str, n: int, m: int) -> int:
        if n == 0 or m == 0:
            return 0
        
        L = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif text1[i - 1] == text2[j - 1]:
                    L[i][j] = 1 + L[i - 1][j - 1]
                else:
                    L[i][j] = max(L[i][j - 1], L[i - 1][j])
        
        return L[n][m]
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        
        return self.longestCommonSubsequenceUtil(text1, text2, n, m)


Palindrome:
https://leetcode.com/problems/palindrome-partitioning-ii/
https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        res = [0] * n
        P = [[False] * n for _ in range(n)]
        
        # All substrings of length 1 are palindromes
        for i in range(n):
            P[i][i] = True
        
        # Check for substrings of length 2 and more
        for L in range(2, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1
                
                if L == 2:
                    P[i][j] = (s[i] == s[j])
                else:
                    P[i][j] = (s[i] == s[j]) and P[i+1][j-1]
        
        # Calculate minimum cuts
        for i in range(n):
            if P[0][i]:
                res[i] = 0
            else:
                res[i] = float('inf')
                for j in range(i):
                    if P[j+1][i] and res[i] > 1 + res[j]:
                        res[i] = 1 + res[j]
        
        return res[n-1] if res[n-1] != float('inf') else 1

Coin Change:
https://leetcode.com/problems/coin-change/
https://leetcode.com/problems/coin-change-2/
https://leetcode.com/problems/combination-sum-iv/
https://leetcode.com/problems/perfect-squares/
https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        if n == 0:
            return 0
        
        res = [float('inf')] * (amount + 1)
        res[0] = 0
        
        for coin in coins:
            for j in range(coin, amount + 1):
                if res[j - coin] != float('inf'):
                    res[j] = min(res[j], 1 + res[j - coin])
        
        return res[amount] if res[amount] != float('inf') else -1


Matrix multiplication:
https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/
https://leetcode.com/problems/burst-balloons/

class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        n = len(A)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for L in range(2, n):
            for i in range(n - L):
                j = i + L
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A[i] * A[k] * A[j])
        
        return dp[0][n-1]


Matrix/2D Array:
https://leetcode.com/problems/matrix-block-sum/
https://leetcode.com/problems/range-sum-query-2d-immutable/
https://leetcode.com/problems/dungeon-game/
https://leetcode.com/problems/triangle/
https://leetcode.com/problems/maximal-square/
https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        # Calculate prefix sum matrix
        sum_matrix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sum_matrix[i][j] = (sum_matrix[i-1][j] + sum_matrix[i][j-1] - 
                                    sum_matrix[i-1][j-1] + mat[i-1][j-1])
        
        # Calculate block sums
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1, c1 = max(0, i-K), max(0, j-K)
                r2, c2 = min(m-1, i+K), min(n-1, j+K)
                r1, r2, c1, c2 = r1+1, r2+1, c1+1, c2+1
                result[i][j] = (sum_matrix[r2][c2] - sum_matrix[r2][c1-1] - 
                                sum_matrix[r1-1][c2] + sum_matrix[r1-1][c1-1])
        
        return result


Hash + DP:
https://leetcode.com/problems/target-sum/
https://leetcode.com/problems/longest-arithmetic-sequence/
https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/


from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        hm = defaultdict(int)
        
        hm[0] = 1
        for num in nums:
            mp = hm.copy()
            hm.clear()
            
            for key, value in mp.items():
                hm[key + num] += value
                hm[key - num] += value
        
        return hm[S]



State machine:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        buy = [0] * n
        sell = [0] * n
        
        buy[0] = -prices[0]
        sell[0] = 0
        
        for i in range(1, n):
            buy[i] = max(buy[i-1], sell[i-1] - prices[i])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i] - fee)
        
        return sell[n-1]


Depth First Search +DP:
https://leetcode.com/problems/out-of-boundary-paths/
https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        mod = 1000000007
        dp = [[[-1 for _ in range(n+1)] for _ in range(m+1)] for _ in range(N+1)]
        
        def dfs(m, n, N, r, c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return 1
            if N == 0:
                return 0
            if dp[N][r][c] != -1:
                return dp[N][r][c] % mod
            
            moves = 0
            moves = (moves + dfs(m, n, N-1, r, c+1)) % mod
            moves = (moves + dfs(m, n, N-1, r, c-1)) % mod
            moves = (moves + dfs(m, n, N-1, r+1, c)) % mod
            moves = (moves + dfs(m, n, N-1, r-1, c)) % mod
            
            dp[N][r][c] = moves % mod
            return dp[N][r][c]
        
        return dfs(m, n, N, i, j)



Minimax DP:
https://leetcode.com/problems/predict-the-winner/
https://leetcode.com/problems/stone-game/


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        
        res = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            res[i][i] = nums[i]
        
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                a = res[i+1][j-1] if i+1 <= j-1 else 0
                b = res[i+2][j] if i+2 <= j else 0
                c = res[i][j-2] if i <= j-2 else 0
                
                res[i][j] = max(nums[i] + min(a, b), nums[j] + min(a, c))
        
        total = sum(nums)
        
        return res[0][n-1] >= total - res[0][n-1]


Miscellaneous:
https://leetcode.com/problems/greatest-sum-divisible-by-three/
https://leetcode.com/problems/decode-ways/
https://leetcode.com/problems/count-numbers-with-unique-digits/
https://leetcode.com/problems/longest-turbulent-subarray/
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

Graph Problems For Practice


Sharing some topic wise good Graph problems and sample solutions to observe on how to approach.


List: https://leetcode.com/list/x1wy4de7


Union Find:


Identify if problems talks about finding groups or components.


https://leetcode.com/problems/friend-circles/
https://leetcode.com/problems/redundant-connection/
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
https://leetcode.com/problems/number-of-operations-to-make-network-connected/
https://leetcode.com/problems/satisfiability-of-equality-equations/
https://leetcode.com/problems/accounts-merge/


All the above problems can be solved by Union Find algorithm with minor tweaks.
Below is a standard template for union find problems.


class Solution {
vectorparent;
int find(int x) {
return parent[x] == x ? x : find(parent[x]);
}
public:
vector findRedundantConnection(vector<vector>& edges) {


	int n = edges.size();

	parent.resize(n+1, 0);
	for (int i = 0; i <= n; i++)
		parent[i] = i;

	vector<int>res(2, 0);
	for (int i = 0; i < n; i++) {
		int x = find(edges[i][0]);
		int y = find(edges[i][1]);
		if (x != y)
			parent[y] = x;
		else {
			res[0] = edges[i][0];
			res[1] = edges[i][1];
		}
	}

	return res;
}
};
Depth First Search


Start DFS from nodes at boundary:
https://leetcode.com/problems/surrounded-regions/
https://leetcode.com/problems/number-of-enclaves/


class Solution {
int rows, cols;
void dfs(vector<vector>& A, int i, int j) {
if (i < 0 || j < 0 || i >= rows || j >= cols)
return;


	if (A[i][j] != 1) 
		return;

	A[i][j] = -1;
	dfs(A, i+1, j);
	dfs(A, i-1, j);
	dfs(A, i, j+1);
	dfs(A, i, j-1);
}
public:
int numEnclaves(vector<vector>& A) {


	if (A.empty()) return 0;

	rows = A.size();
	cols = A[0].size();
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			if (i == 0 || j == 0 || i == rows-1 || j == cols-1)
				dfs(A, i, j);
		}
	}

	int ans = 0;
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			if (A[i][j] == 1)
				ans++;
		}
	}

	return ans;
}
};
Time taken to reach all nodes or share information to all graph nodes:
https://leetcode.com/problems/time-needed-to-inform-all-employees/


class Solution {
void dfs(unordered_map<int, vector>&hm, int i, vector& informTime, int &res, int curr) {


	curr += informTime[i];
	res = max(res, curr);

	for (auto it = hm[i].begin(); it != hm[i].end(); it++)
		dfs(hm, *it, informTime, res, curr);
}
public:
int numOfMinutes(int n, int headID, vector& manager, vector& informTime) {


	unordered_map<int, vector<int>>hm;
	for (int i = 0; i < n; i++)
		if (manager[i] != -1) hm[manager[i]].push_back(i);

	int res = 0, curr = 0;
	dfs(hm, headID, informTime, res, curr);
	return res;
}
};
DFS from each unvisited node/Island problems
https://leetcode.com/problems/number-of-closed-islands/
https://leetcode.com/problems/number-of-islands/
https://leetcode.com/problems/keys-and-rooms/
https://leetcode.com/problems/max-area-of-island/
https://leetcode.com/problems/flood-fill/


class Solution {
void dfs(vector<vector>& grid, vector<vector>& visited, int i, int j, int m, int n) {
if (i < 0 || i >= m || j < 0 || j >= n) return;
if (grid[i][j] == '0' || visited[i][j]) return;
visited[i][j] = true;
dfs(grid, visited, i+1, j, m, n);
dfs(grid, visited, i, j+1, m, n);
dfs(grid, visited, i-1, j, m, n);
dfs(grid, visited, i, j-1, m, n);
}
public:
int numIslands(vector<vector>& grid) {
if (grid.empty()) return 0;


	int m = grid.size();
	int n = grid[0].size();
	vector<vector<bool>>visited(m, vector<bool>(n, false));

	int res = 0;
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (grid[i][j] == '1' && !visited[i][j]) {
				dfs(grid, visited, i, j, m, n);
				res++;
			}
		}
	}

	return res;
}
};
Cycle Find:
https://leetcode.com/problems/find-eventual-safe-states/


class Solution {
bool dfs(vector<vector>& graph, int v, vector& dp) {


	if (dp[v])
		return dp[v] == 1;

	dp[v] = -1;

	for (auto it = graph[v].begin(); it != graph[v].end(); it++)
		if (!dfs(graph, *it, dp))
			return false;

	dp[v] = 1;

	return true;
}
public:
vector eventualSafeNodes(vector<vector>& graph) {


	int V = graph.size();

	vector<int>res;
	vector<int>dp(V, 0);

	for (int i = 0; i < V; i++) {    
		if (dfs(graph, i, dp))
			res.push_back(i);
	}

	return res;
}
};


Breadth First Search


Shortest Path:
https://leetcode.com/problems/01-matrix/
https://leetcode.com/problems/as-far-from-land-as-possible/
https://leetcode.com/problems/rotting-oranges/
https://leetcode.com/problems/shortest-path-in-binary-matrix/


Start BFS from nodes from which shortest path is asked for.
Below is the sample BFS approach to find the path.


class Solution {
public:
vector<vector> updateMatrix(vector<vector>& matrix) {


	if (matrix.empty()) return matrix;
	int rows = matrix.size();
	int cols = matrix[0].size();
	queue<pair<int, int>>pq;
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			if (matrix[i][j] == 0) {
				pq.push({i-1, j}), pq.push({i+1, j}), pq.push({i, j-1}), pq.push({i, j+1}); 
			}
		}
	}

	vector<vector<bool>>visited(rows, vector<bool>(cols, false));
	int steps = 0;
	while (!pq.empty()) {
		steps++;
		int size = pq.size();
		for (int i = 0; i < size; i++) {
			auto front = pq.front();
			int l = front.first;
			int r = front.second;
			pq.pop();
			if (l >= 0 && r >= 0 && l < rows && r < cols && !visited[l][r] && matrix[l][r] == 1) {
				visited[l][r] = true;
				matrix[l][r] = steps;
				pq.push({l-1, r}), pq.push({l+1, r}), pq.push({l, r-1}), pq.push({l, r+1});
			}
		}
	}

	return matrix;
}
};
Graph coloring/Bipartition
https://leetcode.com/problems/possible-bipartition/
https://leetcode.com/problems/is-graph-bipartite/


Problems asks to check if its possible to divide the graph nodes into 2 groups
Apply BFS for same. Below is a sample graph coloring approach.


class Solution {
public:
bool isBipartite(vector<vector>& graph) {
int n = graph.size();
vectorcolor(n, -1);


		for (int i = 0; i < n; i++) {
			if (color[i] != -1) continue;

			color[i] = 1;
			queue<int>q;
			q.push(i);

			while (!q.empty()) {
				int t = q.front();
				q.pop();

				for (int j = 0; j < graph[t].size(); j++) {
					if (color[graph[t][j]] == -1) {
						color[graph[t][j]] = 1-color[t];
						q.push(graph[t][j]);
					} else if (color[graph[t][j]] == color[t]) {
						return false;
					}
				}
			}
		}

		return true;
	}
};
Topological Sort:
Check if its directed acyclic graph and we have to arrange the elements in an order in which we need to select the most independent node at first. Number of in-node 0


https://leetcode.com/problems/course-schedule/
https://leetcode.com/problems/course-schedule-ii/


Below is sample approach. Find if cycle is present, if not apply topological sort.


class Solution {
int V;
list*adj;


bool isCyclicUtil(int v, vector<bool>&visited, vector<bool>&recStack) {
	
	visited[v] = true;
	recStack[v] = true;
	
	for (auto it = adj[v].begin(); it != adj[v].end(); it++) {
		if (!visited[*it] && isCyclicUtil(*it, visited, recStack))
			return true;
		else if (recStack[*it])
			return true;
	}
	
	recStack[v] = false;
	return false;
}

bool isCyclic() {
	vector<bool>visited(V, false);
	vector<bool>recStack(V, false);
	
	for (int i = 0; i < V; i++) {
		if (isCyclicUtil(i, visited, recStack))
			return true;
	}
	
	return false;
}

void topologicalSortUtil(int v, vector<bool>&visited, vector<int>& res) {
	visited[v] = true;
	
	for (auto it = adj[v].begin(); it != adj[v].end(); it++)
		if (!visited[*it])
			topologicalSortUtil(*it, visited, res);
	
	res.push_back(v);
}

vector<int>topologicalSort(int v) {
	vector<int>res;
	
	vector<bool>visited(V, false);
	topologicalSortUtil(v, visited, res);
	
	for (int i = 0; i < V; i++) {
		if (!visited[i])
			topologicalSortUtil(i, visited, res);
	}
	
	return res;
}

public:
vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
	V = numCourses;
	adj = new list<int>[V];

	unordered_map<int, vector<int>>hm;
	
	for (int i = 0; i < prerequisites.size(); i++) {
		adj[prerequisites[i][0]].push_back(prerequisites[i][1]);
		hm[prerequisites[i][1]].push_back(prerequisites[i][0]);
	}
	
	if (isCyclic()) return vector<int>();
	
	int i = 0;
	for (i = 0; i < V; i++) {
		if (hm.find(i) == hm.end())
			break;
	}
	
	return topologicalSort(i);
}
};


Find Shortest Path (Dijkstra's/Bellman Ford)
https://leetcode.com/problems/network-delay-time/


Dijkstras and Bellman Ford:


class Solution {
public:
int networkDelayTime(vector<vector>& times, int N, int K) {


		priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>>pq;
		vector<int>dist(N+1, INT_MAX);
		
		pq.push(make_pair(0, K));
		dist[K] = 0;
		
		unordered_map<int, vector<pair<int, int>>>hm;
		for (int i = 0; i < times.size(); i++)
			hm[times[i][0]].push_back(make_pair(times[i][1], times[i][2]));
		
		while (!pq.empty()) {
			pair<int, int>p = pq.top();
			pq.pop();
			
			int u = p.second;
			for (auto it = hm[u].begin(); it != hm[u].end(); it++) {
				int v = it->first;
				int w = it->second;
				
				if (dist[v] > dist[u] + w) {
					dist[v] = dist[u] + w;
					pq.push(make_pair(dist[v], v));
				}
			}
		}
		
		int res = 0;
		for (int i = 1; i <= N; i++)
			res = max(res, dist[i]);
		
		return res == INT_MAX ? -1 : res;
	}
};


class Solution {
public:
	int networkDelayTime(vector<vector<int>>& times, int N, int K) {
		
		int n = times.size();
		if (!n) return 0;
		
		vector<int>dist(N+1, INT_MAX);
		int res = 0;
		
		dist[K] = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < n; j++) {
				int u = times[j][0];
				int v = times[j][1];
				int w = times[j][2];
				if (dist[u] != INT_MAX && dist[u] + w < dist[v])
					dist[v] = w + dist[u];
			}
		}
		
		for (int i = 1; i <= N; i++)
			res = max(res, dist[i]);

		return res == INT_MAX ? -1 : res;
	}
}
Complete List: Below are mostly list of problems (mostly medium level and may 1 or 2 easy) which are better to start practice with:
(Updated on 14th June '20)


Union Find:


https://leetcode.com/problems/friend-circles/
https://leetcode.com/problems/redundant-connection/
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
https://leetcode.com/problems/number-of-operations-to-make-network-connected/
https://leetcode.com/problems/satisfiability-of-equality-equations/
https://leetcode.com/problems/accounts-merge/
https://leetcode.com/problems/connecting-cities-with-minimum-cost/
DFS:
DFS from boundary:


https://leetcode.com/problems/surrounded-regions/
https://leetcode.com/problems/number-of-enclaves/
Shortest time:


https://leetcode.com/problems/time-needed-to-inform-all-employees/
Islands Variants


https://leetcode.com/problems/number-of-closed-islands/
https://leetcode.com/problems/number-of-islands/
https://leetcode.com/problems/keys-and-rooms/
https://leetcode.com/problems/max-area-of-island/
https://leetcode.com/problems/flood-fill/
https://leetcode.com/problems/coloring-a-border/
Hash/DFS:


https://leetcode.com/problems/employee-importance/
https://leetcode.com/problems/find-the-town-judge/
Cycle Find:


https://leetcode.com/problems/find-eventual-safe-states/
BFS:
BFS for shortest path:


https://leetcode.com/problems/01-matrix/
https://leetcode.com/problems/as-far-from-land-as-possible/
https://leetcode.com/problems/rotting-oranges/
https://leetcode.com/problems/shortest-path-in-binary-matrix/
Graph coloring:


https://leetcode.com/problems/possible-bipartition/
https://leetcode.com/problems/is-graph-bipartite/
Topological Sort:


https://leetcode.com/problems/course-schedule-ii/
Shortest Path:


https://leetcode.com/problems/network-delay-time/
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
https://leetcode.com/problems/cheapest-flights-within-k-stops/
Please correct the approach/solution if you find anything wrong.