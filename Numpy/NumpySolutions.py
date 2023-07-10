import numpy


class numpy:
        n, m = map(int, input().split())
        numpyArray = numpy.array([input().split() for _ in range(n)], int)
            #get the minimal value in axis 1
        #array = numpy.min(numpyArray, axis=1)
                #get mean value
        print(numpy.mean(numpyArray, axis=1))
            #get var value
        print(numpy.var(numpyArray, axis=0))
            #get std value
        print(numpy.std(numpyArray, axis=None))
