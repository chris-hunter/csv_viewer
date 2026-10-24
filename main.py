import pandas as pd
from pathlib import Path
import sys


    

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Please enter only 1 argument: CSV filename")

    csv_file = Path(sys.argv[1]).expanduser()

    df = pd.read_csv(csv_file)
    

