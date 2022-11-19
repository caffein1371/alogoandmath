##########################################
import io
import sys

_INPUT = """\
3
3 1 2


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
def merge(data, start, mid, end):
    data_temp = []
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if data[i] < data[j]:
            data_temp.append(data[i])
            i = i + 1
        else:
            data_temp.append(data[j])
            j = j + 1

    while i <= mid:
        data_temp.append(data[i])
        i = i + 1

    while j <= end:
        data_temp.append(data[j])
        j = j + 1

    k = start
    for val in data_temp:
        data[k] = val
        k = k + 1  

def merge_sort(data, start, end):
    if start >= end:
        return
    
    mid = (start + end) // 2
    merge_sort(data, start, mid)
    merge_sort(data, mid + 1, end)
    merge(data, start, mid, end)

N = int(input())
Alist = list(map(int,input().split()))
end = len(Alist)-1
merge_sort(Alist,0,end)
print (*Alist)
