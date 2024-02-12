#User function Template for python3

def isSubset(a1, a2, n, m):
    sorted_a1 = sorted(a1)
    sorted_a2 = sorted(a2)
    i = 0
    j = 0
    while i < n and j < m:
        if sorted_a1[i] == sorted_a2[j]:
            j += 1
        i += 1
    return "Yes" if j == m else "No"



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends