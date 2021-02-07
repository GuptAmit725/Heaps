class Heap:
    def heapify(self, arr, n, i):
        #step1: find the index of largest node value for the given parent node at index i
        #check that i, l_c or r_c should not be greater than the total nodes that is n
        #because max_heap is done only for none leaf or internal nodes.
        l_c =  2*i+1
        r_c = 2*i+2
        largest = i
        if ((l_c < n) and (arr[i]<arr[l_c])):
            largest = l_c
        if ((r_c < n) and (arr[largest]<arr[r_c])):
            largest = r_c
        #step2: if the parent node index i != largets that means max value index and parent index is not same, So we will swap
        # arr[largets],arr[i]
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i]
            self.heapify(arr,n,largest)
        return arr

    def build_heap(self,arr, n):
        for j in range(n//2, -1,-1):
            self.heapify(arr,n,j)
        return arr
    
    def heapsort(self,arr):
        n = len(arr)
        arr=self.build_heap(arr,n)
        for i in range(n-1,0,-1):
            arr[i], arr[0] = arr[0], arr[i]
            arr = self.heapify(arr,i,0)
        return arr    
            
        
        
arr = [4,1,3,2,16,9,10,14,8,7]
heap = Heap()
#arr = heap.build_heap(arr,len(arr))
arr = heap.heapsort(arr)
print(arr)