from corefeval.utils import CorefClusters, HashableCluster, MentionDict


def tuplify(clusters: CorefClusters) -> HashableCluster:
    return [tuple(map(tuple, cluster)) for cluster in clusters]

def mentionize(clusters: HashableCluster) -> MentionDict:
    """ maps any mention to all its matching mention clusters

    Args:
        clusters (HashableCluster): clusters (list of tuples of tuples)

    Returns:
        MentionDict: dictionary from a mention part
    """
    mentions = {}
    for mention_group in clusters:
        for part_mention in mention_group:
            mentions[part_mention] = mention_group
    return mentions

class Document:
    def __init__(self, predicted, truth) -> None:
        self.pred = tuplify(predicted)
        self.gold = tuplify(truth)
        self.pred_mentions = mentionize(self.pred)
        self.gold_mentions = mentionize(self.gold)

    def __str__(self) -> str:
        return f"Predicted:\n{self.pred}\n\nGold:\n{self.gold}\n"
