from typing import Dict, List, Tuple

IndexRange = Tuple[int, int]
CorefCluster = List[IndexRange]
CorefClusters = List[CorefCluster]
HashableRange = Tuple[int, ...]
HashableCluster = List[Tuple[HashableRange, ...]]
MentionDict = Dict[HashableRange, Tuple[HashableRange, ...]]
