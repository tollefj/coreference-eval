from typing import Tuple
from corefeval.utils import CorefClusters, MentionDict
def importance(entity):
    return len(entity)

def lea(clusters: CorefClusters, mention_to_gold: MentionDict) -> Tuple[float, int]:
    tp, p = 0, 0


    for c in clusters:
        if len(c) == 1:
            continue

        common_links = 0
        all_links = len(c) * (len(c) - 1) / 2.0
        for i, m in enumerate(c):
            if m in mention_to_gold:
                for m2 in c[i + 1:]:
                    if m2 in mention_to_gold and mention_to_gold[m] == mention_to_gold[m2]:
                        common_links += 1

        resolution_score = common_links / float(all_links)
        tp += importance(c) * resolution_score
        p += importance(c)

    return tp, p