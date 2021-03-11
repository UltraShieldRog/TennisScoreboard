# TennisScoreboard
Tennis scoreboard script (command line based)

# Dependencies

```bash
pip install argparse
```

# How to run

To run the program with real-time tracking of scores:

```bash
python main.py --verbose
```

To simply run the program and view the winner player id (winner of player 1 and player 2):

```bash
python main.py --verbose
```

You may run with default inputs to view some outupts without mannually typing inputs.

```bash
python main.py --verbose < tests/inputs/basic_1.in
```

Or

```bash
python main.py --verbose < tests/inputs/basic_2.in
```

# How to run tests

```bash
python -m unittest tests/test_units.py
```