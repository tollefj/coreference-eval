from typing import Dict, Tuple
from corefeval import Scorer, Document
from corefeval.utils import CorefClusters

# Tuple of precision, recall and F1 for each metric
Metrics = Dict[str, Tuple[float, float, float]]

def get_metrics(
    predicted: CorefClusters,
    gold: CorefClusters,
    verbose=True,
    modelname="Undefined model",
    dataset="Undefined data",
    ) -> Tuple[float, Metrics]:
    scorer = Scorer()
    doc = Document(
        predicted=predicted,
        truth=gold,
    )
    scorer.update(doc)

    conll_f1, metrics = scorer.detailed_score(
        modelname, dataset, verbose=verbose)

    return conll_f1, metrics