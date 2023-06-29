import resource
import sys

def squares_to_gen (max):
    n = 0
    while n <= max:
        yield n**2
        n += 1

def squares_to_iter (max):
    l = []
    for n in range(max + 1):
        l.append(n**2)
    return l

if sys.argv[1] == "gen":
    print(f"{'Sum: ':>25}{sum(squares_to_gen(10**int(sys.argv[2])))}")
elif sys.argv[1] == "iter":
    print(f"{'Sum: ':>25}{sum(squares_to_iter(10**int(sys.argv[2])))}")
else:
    print("Usage: python3 generatorTest.py gen|iter exponent")
    quit()
print(f"{'Computation time: ':>25}{resource.getrusage(resource.RUSAGE_SELF).ru_utime:.2f} secs")
print(f"{'RAM used: ':>25}{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/10**6:.2f} MB")
# print(resource.getrusage(resource.RUSAGE_SELF))
