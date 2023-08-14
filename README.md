# corefeval - A super simple coreference evaluation tool
Defaults to the CoNLL standard (MUC, B^3 and CEAFE), but also supports LEA.

## Installation

Install the package with pip:

```bash
pip install coreference-eval
```

## Usage

You can use the package as a command-line tool or as a Python module.

### Command-line Tool
```bash
python -m corefeval -h
python -m corefeval --pred /path/to/pred.jsonl --gold /path/to/gold.jsonl
```

The --clusters option lets you specify the key under which coreference chains/clusters are stored in the JSONLine objects. By default, it's set to "clusters".

If you have a different key, you can specify it as follows:
```
python -m corefeval --pred /path/to/pred.jsonl --gold /path/to/gold.jsonl --clusters my_key
```

### As a Module

```python
from corefeval import get_metrics

# gold and pred are example inputs
gold = [[[50, 50], [27, 27], [29, 29]], [[0, 1], [7, 13]]]
pred = [[[50, 50], [27, 27], [29, 29]], [[0, 1], [42, 42], [7, 13]]]

get_metrics(pred, gold)
```

## Additional Classes and Functions

### `Document` Class

The `Document` class represents a document with predicted and gold coreference clusters.

```python
from corefeval import Document

doc = Document(predicted=pred, truth=gold)
```

### `Scorer` Class

The `Scorer` class is used to hold values from a Document object.

```python
from corefeval import Scorer

scorer = Scorer()
scorer.update(doc)

conll_f1, metrics = scorer.detailed_score(modelname="model", dataset="dataset", verbose=True)
```

### `Metric` Class

The `Metric` class calculates precision, recall, and F1 score for a given coreference evaluation metric.

```python
from corefeval.metrics import Metric, ceafe

metric = Metric(ceafe)
```
