# coreference evaluation
### Metrics and evaluation code for coreference resolution
Defaults to the CONLL standard (MUC, B^3 and CEAFE), but also supports LEA.

# run options
## 1. as a command-line tool:
`python -m corefeval -h`
with support for prediction- and gold label files.

## 2. as a module
```
from corefeval import get_metrics
gold = [[[50, 50], [27, 27], [29, 29]], [[0, 1], [7, 13]]]
pred = [[[50, 50], [27, 27], [29, 29]], [[0, 1], [42, 42], [7, 13]]]
get_metrics(pred, gold)
```

You can also use the `Scorer` and `Document` classes to produce the same result, with more flexibility:
```
scorer = Scorer()
doc = Document(
    predicted=predicted,
    truth=gold,
)
scorer.update(doc)

conll_f1, metrics = scorer.detailed_score(
    modelname, dataset, verbose=verbose)
```

The `.update` procedure iterates the total documents in the scorer, so make sure not to create a new scorer in every iteration if you have multiple documents.

More documentation to come.

