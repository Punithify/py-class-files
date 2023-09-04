import fibb


# print(fib2(3))
# print(dir('__package__'))
from pathlib import Path
import sys
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)
