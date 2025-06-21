import numpy as np
from bisect import bisect_left

# ユーティリティ: ベクトルを正規化
def normalize(v):
    norm = np.linalg.norm(v)
    return v / norm if norm != 0 else v

# 前処理クラス
class CMYVectorSearch:
    def __init__(self, vectors):
        self.original_vectors = np.array(vectors)
        self.unit_vectors = np.array([normalize(v) for v in vectors])

        # ソート基準として球面上の座標（球面座標の1軸投影）
        self.angles = np.array([np.arctan2(v[1], v[0]) for v in self.unit_vectors])
        sorted_indices = np.argsort(self.angles)

        self.unit_vectors = self.unit_vectors[sorted_indices]
        self.original_vectors = self.original_vectors[sorted_indices]
        self.angles = self.angles[sorted_indices]

    # クエリ：最も内積が小さいベクトルを返す
    def query(self, A):
        A_unit = normalize(np.array(A))
        target_angle = np.arctan2(A_unit[1], A_unit[0])

        # 二分探索で近い方向を探す
        idx = bisect_left(self.angles, target_angle)

        # 前後数点を比較して内積最小を探す（近似）
        candidates = []
        for offset in [-2, -1, 0, 1, 2]:
            i = (idx + offset) % len(self.unit_vectors)
            dot = np.dot(A_unit, self.unit_vectors[i])
            candidates.append((dot, i))

        # 最小の内積（= 最大の反対方向）を選ぶ
        min_dot, min_idx = min(candidates, key=lambda x: x[0])
        return self.original_vectors[min_idx], min_dot

# ベクトル群（CMY値）
vectors = [
    [0.9, 0.1, 0.2],
    [0.2, 0.8, 0.3],
    [0.1, 0.2, 0.9],
    [0.5, 0.5, 0.5],
    [0.0, 0.0, 1.0]
]

# 検索オブジェクト作成
searcher = CMYVectorSearch(vectors)

# クエリベクトル
query_vector = [0.2, 0.8, 0.3]

# 最も内積が小さいベクトルを検索
result_vector, dot_value = searcher.query(query_vector)
print("内積最小ベクトル:", result_vector)
print("内積値:", dot_value)
