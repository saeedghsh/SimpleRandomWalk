"""
Simple Random Walk - main script
"""
#!/usr/bin/env python
from __future__ import print_function

from SimpleRandomWalk.SimpleRandomWalk import SimpleRandomWalk
from SimpleRandomWalk.plotting import SlidingFigure

if __name__ == "__main__":
    
    count  = 1
    length = 100
    
    random_walks = [SimpleRandomWalk(length) for _ in range(count)]
    sf = SlidingFigure(random_walks)
