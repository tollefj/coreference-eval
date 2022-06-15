from typing import Tuple

import numpy as np
from corefeval.utils import CorefCluster, CorefClusters, linear_assignment


def phi4(c1: CorefCluster, c2: CorefCluster) -> float:
    return 2 * len([m for m in c1 if m in c2]) / float(len(c1) + len(c2))

def ceafe(clusters: CorefClusters, gold_clusters: CorefClusters) -> Tuple[float, int, float, int]:
    clusters = [c for c in clusters if len(c) != 1]
    scores = np.zeros((len(gold_clusters), len(clusters)))

    for i, gold_cluster in enumerate(gold_clusters):
        for j, cluster in enumerate(clusters):
            scores[i, j] = phi4(gold_cluster, cluster)

    matching = linear_assignment(-scores)
    similarity = sum(scores[matching[:, 0], matching[:, 1]])
    return similarity, len(clusters), similarity, len(gold_clusters)
