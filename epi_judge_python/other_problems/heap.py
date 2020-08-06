# algoexpert: continuous median from a stream
import heapq


class heap:
    def __init__(self, arr=None):
        self.arr = arr
        pass

    def push(self, x):
        pass

    def pop(self):
        pass

    def heapify(self):
        pass


def heapify(arr, index):
    parent_index = index
    left_child = 2 * parent_index + 1
    right_child = 2 * parent_index + 2
    smallest_index = index

    if left_child <= len(arr) - 1 and arr[left_child] < arr[parent_index]:
        smallest_index = left_child
    if right_child <= len(arr) - 1 and arr[right_child] < arr[parent_index]:
        smallest_index = right_child
    if smallest_index != index:
        arr[smallest_index], arr[parent_index] = arr[parent_index], arr[smallest_index]
        heapify(arr, smallest_index)


class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.min_heap = []  # heap containing larger half of stream
        self.max_heap = []  # heap containing smaller half of stream


def insert(self, number):
    if not len(self.max_heap) or number < -self.max_heap[0]:
        heapq.heappush(self.max_heap, -number)
    else:
        heapq.heappush(self.min_heap, number)

    if len(self.min_heap) - len(self.max_heap) > 1:
        heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
    elif len(self.max_heap) - len(self.min_heap) > 1:
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    if len(self.min_heap) > len(self.max_heap):
        self.median = self.min_heap[0]
    elif len(self.max_heap) > len(self.min_heap):
        self.median = -self.max_heap[0]
    else:
        self.median = (self.min_heap[0] + -self.max_heap[0]) / 2


def getMedian(self):
    return self.median


if __name__ == '__main__':
    # x = [4, 2, 1, 0, 5, 0]
    # heapify(x, 0)
    # print(x)
    import heapq

    x = []
    heapq.heappush(x, 4)
    heapq.heappush(x, 2)
    heapq.heappush(x, 1)
    heapq.heappush(x, 0)
    heapq.heappush(x, 5)

    print(x[0])
