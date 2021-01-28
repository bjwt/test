#!/usr/bin/python

srcData = []
dstData = []

number = 10
def initSrcData(srcData):
    for num in range(number):
        srcData.append(number-num)


def bubbleSort(srcData):
    for i in range(number-1):
        for i in range(number-1-i):
			if srcData[i] > srcData[i+1]:
				temp = srcData[i]
				srcData[i] = srcData[i+1]
				srcData[i+1] = temp
    return srcData

initSrcData(srcData)
print srcData
print "------\n\n"
bubbleSort(srcData)
print srcData
