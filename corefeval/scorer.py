'''
Accessed 13.04.20 by Tollef Jørgensen
From https://github.com/tollefj/ClEval/blob/master/metrics.py
Edited June 2022 to conform with library updates and f-printing

Original source: https://github.com/kentonl/e2e-coref/blob/master/metrics.py
Heavily based on the work by Clark Manning: https://github.com/clarkkev/deep-coref/blob/master/evaluation.py 

This metric class has been modified to support more detailed runs with both LEA and CoNLL,
as well as pretty-printing the output in the `detailed_score` function

the update function has been updated according to the original implementation by Manning.
as well as the function "print_scores"

'''
from typing import Tuple

from corefeval.metric import Metric
from corefeval.metrics import muc, b_cubed, ceafe, lea

CONLL_METRICS = [muc, b_cubed, ceafe]
ALL_METRICS = CONLL_METRICS + [lea]

class Scorer:
    def __init__(self):
        self.doc_count = 0
        self.conll = [Metric(m) for m in CONLL_METRICS]
        self.all = [Metric(m) for m in ALL_METRICS]
        
    def eval_documents(self, docs):
        for d in docs:
            for e in self.all:
                e.update(d)
        print(f"evaluated {len(docs)} documents with {len(self.all)} metrics")
        self.detailed_score("", "")

    def update(self, doc):
        self.doc_count += 1
        for e in self.all:
            e.update(doc)

    def detailed_score(self, modelname, dataset, verbose=True):
        conll_avg_f1 = 0
        detailed_metrics = {}
        if verbose:
            print(f"Evaluating {modelname} on dataset: {dataset}")
        for e in self.all:
            if verbose: 
              print(f"Running metric: {e.metric.__name__}")
            p, r, f = e.get_prf()
            detailed_metric_score = {
                "precision": p,
                "recall": r,
                "f1": f
            }
            detailed_metrics[e.metric.__name__] = detailed_metric_score
            if e.metric in CONLL_METRICS:
                conll_avg_f1 += f
            if verbose:
                print(f"Precision:\t{p}\nRecall:\t\t{r}\nF1 score:\t{f}")
                print("-----------------------------------")
        if verbose:
            print(f"\nCoNLL-2012 F1 score: {conll_avg_f1 / 3}")
            print(f"Evaluated {self.doc_count} documents total")

        return conll_avg_f1 / 3, detailed_metrics

    
    def get_conll(self) -> float:
        f1 = sum([m.get_f1() for m in self.conll])
        return f1 / len(self.conll)

    def get_prf(self, conll=True) -> Tuple[float, float, float]:
        metrics = self.conll if conll else self.all
        prec = sum(e.get_precision() for e in metrics) / len(metrics)
        rec = sum(e.get_recall() for e in metrics) / len(metrics)
        f_1 = sum(e.get_f1() for e in metrics) / len(metrics)

        return prec, rec, f_1
