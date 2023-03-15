import heapq
# import heapq to build the heap data structure
#heap will organize the data from min to max
# can use list to build it

minheap = []
heapq.heappush(minheap, 6)
heapq.heappush(minheap, 2)
heapq.heappush(minheap, 3)
heapq.heappush(minheap,1)

while len(minheap):
    print(heapq.heappop(minheap))