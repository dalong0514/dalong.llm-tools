# demo.py
import numpy as np
from typing import List, Tuple

def softmax(x: np.ndarray) -> np.ndarray:
    x = x - np.max(x)        # 数值稳定
    ex = np.exp(x)
    return ex / np.sum(ex)

class Node:
    """
    一个最小可用的“Transformer风格”节点：
    - data: 节点当前的状态向量（d_model）
    - Wq, Wk, Wv: 线性投影矩阵，把 data 投影到 query/key/value 空间
    """
    def __init__(self, d_model: int):
        self.d = d_model
        # 小随机数初始化
        self.data = np.random.randn(d_model) * 0.1
        self.Wq = np.random.randn(d_model, d_model) * (1.0 / np.sqrt(d_model))
        self.Wk = np.random.randn(d_model, d_model) * (1.0 / np.sqrt(d_model))
        self.Wv = np.random.randn(d_model, d_model) * (1.0 / np.sqrt(d_model))

    def query(self) -> np.ndarray:
        return self.data @ self.Wq

    def key(self) -> np.ndarray:
        return self.data @ self.Wk

    def value(self) -> np.ndarray:
        return self.data @ self.Wv

class Graph:
    def __init__(self, num_nodes: int = 10, num_edges: int = 40, d_model: int = 8, seed: int = 42):
        np.random.seed(seed)
        self.nodes: List[Node] = [Node(d_model) for _ in range(num_nodes)]

        randi = lambda: np.random.randint(len(self.nodes))
        # 允许自环/并行边；真实应用可去重或避免自环
        self.edges: List[Tuple[int, int]] = [(randi(), randi()) for _ in range(num_edges)]

    def run(self, steps: int = 1, inspect_node: int = 0, verbose: bool = True):
        """
        运行若干轮消息传递。
        - steps: 迭代轮数
        - inspect_node: 想查看注意力细节的目标节点 id
        - verbose: 是否打印每轮该节点的注意力权重
        """
        for step in range(steps):
            updates: List[np.ndarray] = []
            # 先为每个节点准备更新（同步更新）
            for i, n in enumerate(self.nodes):
                q = n.query()
                inputs = [self.nodes[ifrom] for (ifrom, ito) in self.edges if ito == i]
                if len(inputs) == 0:
                    # 没有入边就不更新（也可以选择加入某种自注意/自环）
                    updates.append(np.zeros_like(n.data))
                    continue

                keys = np.stack([m.key() for m in inputs], axis=0)    # (Ni, d)
                scores = keys @ q                                     # (Ni,)
                attn = softmax(scores)                                # (Ni,)

                values = np.stack([m.value() for m in inputs], axis=0)  # (Ni, d)
                update = (attn[:, None] * values).sum(axis=0)            # (d,)
                updates.append(update)

                if verbose and i == inspect_node:
                    # 打印该节点的注意力细节
                    src_idx = [ifrom for (ifrom, ito) in self.edges if ito == i]
                    print(f"\n[Step {step+1}] Node {i} has {len(src_idx)} inputs from {src_idx}")
                    print("  attention weights (sum=1):")
                    # 为了更直观，把<邻居id, 权重>排个序
                    pairs = list(zip(src_idx, attn.tolist()))
                    pairs.sort(key=lambda x: x[1], reverse=True)
                    for pid, w in pairs[:10]:
                        print(f"    from {pid:<2} -> {w:.4f}")
                    if len(pairs) > 10:
                        print("    ...")

            # 残差同步更新
            for n, u in zip(self.nodes, updates):
                n.data = n.data + u

            if verbose:
                # 打印 inspect_node 的范数变化（粗看量级是否在增长/收敛）
                norm_vals = [np.linalg.norm(nd.data) for nd in self.nodes]
                print(f"[Step {step+1}] L2 norms (min/mean/max): "
                      f"{np.min(norm_vals):.4f} / {np.mean(norm_vals):.4f} / {np.max(norm_vals):.4f}")

def main():
    g = Graph(num_nodes=10, num_edges=40, d_model=8, seed=123)
    print("Edges (first 12 shown):", g.edges[:12])
    print("Running 3 steps of message passing with attention ...")
    g.run(steps=3, inspect_node=0, verbose=True)

    # 展示一个小结：随机挑 3 个节点，打印其数据向量前 4 维
    pick = [0, 3, 7]
    for idx in pick:
        print(f"\nNode {idx} data (first 4 dims): {g.nodes[idx].data[:4]}")

if __name__ == "__main__":
    main()

