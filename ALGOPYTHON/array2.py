import subprocess

subprocess.run('dir', shell=True)



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
    # arr = minimumBribes(a)
    print(q)
