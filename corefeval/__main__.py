from argparse import ArgumentParser, Namespace
import jsonlines
from corefeval import Scorer, Document

def main(args: Namespace):
    gold, pred = [], []
    with jsonlines.open(args.gold) as gold_reader:
        for jsonl in gold_reader:
            gold.append(jsonl)
    with jsonlines.open(args.pred) as pred_reader:
        for jsonl in pred_reader:
            pred.append(jsonl)

    scorer = Scorer()
    for g, p in zip(gold, pred):
        doc = Document(predicted=p[args.clusters], truth=g[args.clusters])
        print(doc.gold_mentions)
        print(doc.pred_mentions)
        scorer.update(doc)
    
    conll_f1, metrics = scorer.detailed_score(modelname="none", dataset="dummy", verbose=True)
    return conll_f1, metrics

if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument(
        "-p",
        "--pred",
        type=str,
        help="file path containing one or multiple jsonline objects (with predictions)"
    )
    parser.add_argument(
        "-g",
        "--gold",
        type=str,
        help="file path containing one or multiple jsonline objects (with gold labels)"
    )
    parser.add_argument(
        "--clusters",
        type=str,
        default="clusters",
        help="the key which coreference chains/clusters are stored in the jsonline objects"
    )

    main(parser.parse_args())
