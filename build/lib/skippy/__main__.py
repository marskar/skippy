from argparse import ArgumentParser
from skippy import classification, regression


def main():
    """The main routine."""

    parser = ArgumentParser(
        description='Analyze one of the built-in scikit-learn datasets.')

    parser.add_argument('--data', '-d', default='digits',
                        help='The scikit-learn dataset name.')

    parser.add_argument('--type', '-t', default='linear_model',
                        help='The scikit-learn model type.')

    parser.add_argument('--name', '-n', default='LogisticRegression',
                        help='The scikit-learn model name.')

    args = parser.parse_args()

    kwargs = dict(dataset=args.data,
                  model_type=args.type,
                  model_name=args.name,
                  )

    if args.data in ('digits', 'iris', 'wine', 'breast_cancer'):
        classification(**kwargs)
    elif args.data in ('boston', 'diabetes'):
        regression(**kwargs)
    else:
        print("The dataset name must be digits, iris, wine, boston, breast_cancer, or diabetes.")


if __name__ == "__main__":
    main()
