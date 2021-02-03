class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 根据words建立Trie树
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = True

        # dfs：搜索 board 中是否存在与 words 列表相同的单词
        def dfs(i, j, node, pre, visited):  #(i,j)当前坐标，node当前结点，pre前面的字符串，visited已访问坐标
            if '#' in node:
                # res.add(pre)
                res.append(pre) ; node.pop('#')       #pop key去重，则res可直接用list
            for (di, dj) in ((-1, 0), (1, 0), (0, -1), (0, 1)):            #Py技巧：以元组来实现分组遍历
                _i, _j = i+di, j+dj
                if 0 <= _i < m and 0 <= _j < n:                            #Py语法：支持 a<b<c
                    _b = board[_i][_j]
                    if _b in node and (_i, _j) not in visited:
                        dfs(_i, _j, node[_b], pre+_b, visited+((_i,_j),))  #Py实践：元组比集合快5%左右
                        # dfs(_i, _j, node[_b], pre+_b, visited.union({(_i,_j)}))
                        # dfs(_i, _j, node[_b], pre+_b, visited|{(_i,_j)})

        # 对 board 遍历搜索
        # res, m, n = set(), len(board), len(board[0])
        res, m, n = [], len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie[board[i][j]], board[i][j], ((i,j),))    #Py实践：元组比集合快5%左右
                    # dfs(i, j, trie[board[i][j]], board[i][j], {(i,j)})
        # return list(res)
        return res

