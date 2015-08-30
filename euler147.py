#Project Euler 147: Rectangles in cross-hatched grids

def number_of_rectangles(N, M):
    """Returns the number of different rectangles which can be situated in
       a cross-hatched N x M grid"""
    result = (M*(M+1)*N*(N+1))// 4 #The rectangles parallell with the grid itself.
    result += 0
 
