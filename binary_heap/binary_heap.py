"""
binary max heap implementation
input ---
        the first line --- number of operations
        other lines --- Insert <number> or GetMax
output --- list of the biggest elements (element adds to the list after calling GetMax)
"""


class MaxHeap:
    def __init__(self):
        self.heap = []  # contains heap elements
        self.result = []  # contains the biggest elements

    # is used after extracting max element of the heap to fix heap properties if it is violated
    def shift_down(self, index):
        # for example we have tree
        #          30[0]
        #     15[1]    18[2]
        #  10[3]
        # and index == 1
        # 2 * index + 1 = 3 and 3 < 4 (heap size)
        while 2 * index + 1 < len(self.heap):
            left = 2 * index + 1  # left = 3
            right = 2 * index + 2  # right = 4
            max_l_r = left  # left "node" necessarily exists but right one may not
                            # in our examle heap[4] does not exist
            # if right "node" exists, find max value from them
            # and assign its index
            if right < len(self.heap) and self.heap[right] > self.heap[left]:
                max_l_r = right
            # we don't need to swap elements if "parent" >= its biggest "child"
            # it means that further "descendants" are in right order
            if self.heap[index] >= self.heap[max_l_r]:
                break
            # but when "parent" < its biggest "child", we need to swap
            # and check next further, because heap properties could be violated
            self.heap[index], self.heap[max_l_r] = self.heap[max_l_r], self.heap[index]
            index = max_l_r

    def shift_up(self, index):
        # (index - 1) // 2 --- "parent" index
        # while "parent" < "child" and our index >= 1 (level >= 1)
        # or if index = 0 (level 0) we will get
        # (0 - 1) // 2 = -1
            # and we have chance swap the first and the last elements
            # in case of small tree
            # for example
            # insert 10 (heap[0])
            # insert 30 --- 10 -> 30 --- bad (heap[0] < heap[1]), index = 1
            # change to 30 -> 10, index = (1 - 1) // 2 = 0
            # then it checks heap[-1] < heap[0]? (and its true, because heap[0] == 30 and heap[-1] == 10)
            # and change them and properties are violated
        while index >= 1 and self.heap[(index - 1) // 2] < self.heap[index]:
            self.heap[index], self.heap[(index - 1) // 2] = self.heap[(index - 1) // 2], self.heap[index]
            index = (index - 1) // 2

    def insert_heap(self, value):
        self.heap.append(value)  # add value at the end of the heap-list
        self.shift_up(len(self.heap) - 1)  # not using self.heap[-1] for correct work of shift_up

    def extract_max(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]  # change the last and the first elements
        self.result.append(self.heap.pop())  # delete the last element (our max value) and add to result
        self.shift_down(0)  # and fix tree


def parser(command, heap):
    if command[0] == "Insert":
        heap.insert_heap(int(command[1]))
    else:
        heap.extract_max()


def main():
    heap = MaxHeap()
    iteration = int(input())
    for i in range(iteration):
        command = list(input().split())
        parser(command, heap)

    for obj in heap.result:
        print(obj)


if __name__ == "__main__":
    main()
