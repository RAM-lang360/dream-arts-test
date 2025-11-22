import sys

FILE_PATH = "./src/data/input.txt"

class Main:
    
    def __init__(self):
        #DFS用変数の定義
        self.graph = {}
        self.all_nodes = set()
        self.max_distance = -1.0
        self.best_path = []
    
    # ファイルから入力 (ローカルテスト用)
    def get_text(self):
        try:
            with open(FILE_PATH, "r") as f:
                input_text = f.read()
            
            self._parse_input(input_text.splitlines())
        except FileNotFoundError:
            print(f"Error: {FILE_PATH} not found.")

    # 標準入力から入力 (提出用)
    def get_text_input(self):
        input_lines = sys.stdin.readlines()
        self._parse_input(input_lines)

    # 入力解析の共通処理
    def _parse_input(self, lines):
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            parts = line.split(',')
            if len(parts) != 3:
                continue

            u = int(parts[0].strip())
            v = int(parts[1].strip())
            w = float(parts[2].strip())
            
            # ノード集合に追加
            self.all_nodes.add(u)
            self.all_nodes.add(v)

            if u not in self.graph:
                self.graph[u] = []
            self.graph[u].append((v, w))
    
    def dfs(self, current_node, current_dist, path, visited):
        # 最長距離の更新チェック
        if current_dist > self.max_distance:
            self.max_distance = current_dist
            self.best_path = list(path) # 現在のパスをコピーして保存
        
        # 次の移動先を探索
        if current_node in self.graph:
            for neighbor, weight in self.graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    path.append(neighbor)
                    
                    # 再帰呼び出し
                    self.dfs(neighbor, current_dist + weight, path, visited)
                    
                    path.pop()
                    visited.remove(neighbor)

    def solve(self):
        # 全てのノードを始点として試す
        sorted_nodes = sorted(list(self.all_nodes))
        
        for start_node in sorted_nodes:
            self.dfs(start_node, 0.0, [start_node], {start_node})
        
        # 結果の出力
        for node in self.best_path:
            print(node)

if __name__ == "__main__":
    app = Main()
    
    # 提出
    #app.get_text_input()
    
    # ローカル
    app.get_text()
    
    app.solve()