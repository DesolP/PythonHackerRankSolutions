import numpy


class DotAndCross:
    def _create_numpy_array(self, m):
        return numpy.array([input().split() for _ in range(m)], int)


    def solution(self):
        m = int(input())
        numpy_array1 = self._create_numpy_array(m)
        numpy_array2 = self._create_numpy_array(m)
        print(numpy.dot(numpy_array1,numpy_array2))



obj = DotAndCross()
obj.solution()
