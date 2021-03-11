from game_engine import MatchEngine
import argparse

def main(args):
    game_engine = MatchEngine()
    verbose = bool(args.verbose)
    game_engine.run(verbose=verbose)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="config")
    parser.add_argument(
        "--verbose",
        nargs="?",
        type=bool,
        const=True,
        default=False,
        help="Show score records verbosely"
    )
    args = parser.parse_args()

    main(args)