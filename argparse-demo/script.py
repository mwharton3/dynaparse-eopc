from argparse import ArgumentDefaultsHelpFormatter
from argparse import ArgumentParser
import sys


class TrainingSessionArgumentParser(ArgumentParser):
    """Example argument parser for a script."""

    def __init__(self):
        super().__init__(
            prog="training_session",
            description="Train a machine learning model",
            formatter_class=ArgumentDefaultsHelpFormatter,
        )

        self.add_argument(
            "--learning_rate",
            type=float,
            default=1e-4,
            help="Learning rate for training loop",
        )


if __name__ == "__main__":
    parser = TrainingSessionArgumentParser()
    args = parser.parse_args()
    print("COMMAND LINE ARGUMENTS:")
    print(sys.argv)
    print()
    print("PARSED ARGUMENTS:")
    print(args)
