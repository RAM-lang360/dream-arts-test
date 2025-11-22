from index import Main
def test_dps_initialization():
    dps = Main()
    assert dps is not None
    
def test_dps_get_text(monkeypatch):
    dps = Main()
    dps.get_text()
    assert dps.graph is not None

def test_dps_dfs():
    dps = Main()
    dps.graph = {
        1: [(2, 1.0), (3, 2.0)],
        2: [(4, 3.0)],
        3: [(4, 1.0)],
        4: []
    }
    dps.all_nodes = {1, 2, 3, 4}
    dps.dfs(1, 0.0, [1], {1})
    assert dps.max_distance == 4.0
    assert dps.best_path == [1, 2, 4]

def test_dps_solve_example():
    print("\n例データの検証\n")
    dps = Main()
    dps.get_text()
    dps.solve()
    assert dps.best_path == [1,2,3,4]
    
def test_solve_loop_graph():
    print("\nループ（閉路）がある場合の検証\n")
    dps = Main()
    dps.graph = {
        1: [(2, 10.0)],
        2: [(3, 10.0)],
        3: [(1, 10.0)]
    }
    # solveはall_nodesを使って始点を決めるため設定必須
    dps.all_nodes = {1, 2, 3}
    
    dps.solve()
    
    # 期待値: 1->2->3 (距離20) など、3つのノードを通るのが最長
    assert dps.max_distance == 20.0
    assert len(dps.best_path) == 3

