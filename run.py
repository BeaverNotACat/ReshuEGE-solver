import sys
from ReshuEgeSolver import ReshuEgeSolver


if __name__ == "__main__" and len(sys.argv) == 3:
    solver = ReshuEgeSolver(sys.argv[1], sys.argv[2])
    solver.run()
else:
    print('Please use "python run <test url> <answers filename>"')
    