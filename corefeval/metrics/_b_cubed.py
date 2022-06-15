from collections import Counter
from typing import Tuple
from corefeval.utils import CorefCluster, MentionDict

def b_cubed(clusters: CorefCluster, mention_to_gold: MentionDict) -> Tuple[float, int]:
    tp, p = 0, 0

    for c in clusters:
        if len(c) == 1:
            continue

        gold_counts = Counter()
        correct = 0
        for m in c:
            if m in mention_to_gold:
                gold_counts[tuple(mention_to_gold[m])] += 1
        for c2, count in gold_counts.items():
            if len(c2) != 1:
                correct += count * count

        tp += correct / float(len(c))
        p += len(c)

    return tp, p
