# finding second maximum in an array
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr2 = sorted (list (arr))
    max = arr2[-1]
    i = - 2
    run_up_score = arr2[i]
    while run_up_score == max:
        i-=1
        run_up_score = arr2[i]
    print (run_up_score)
    
