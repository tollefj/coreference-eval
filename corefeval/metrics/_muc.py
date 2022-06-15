from typing import Tuple
from corefeval.utils import CorefClusters, MentionDict

def muc(clusters: CorefClusters, mention_to_gold: MentionDict) -> Tuple[float, int]:
    tp, p = 0, 0
    for c in clusters:
        p += len(c) - 1
        tp += len(c)
        linked = set()
        for m in c:
            if m in mention_to_gold:
                linked.add(mention_to_gold[m])
            else:
                tp -= 1
        tp -= len(linked)
    return tp, p
