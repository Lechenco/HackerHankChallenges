#!/bin/python3

import math
import os
import random
import re
import sys

positionHash = []

def linear_search(arr, val, start):
    if arr[start] > val:
        return start +1
    while(start > 0 and arr[start - 1] < val):
        start -= 1
    return max(start, 0)

def binary_search(arr, val, start, end): 
    if start >= end:
        aux = max(0, min(len(arr) -1, start))
        if arr[aux] < val:
            return aux
        else:
            return aux + 1

    mid = int((start+end)/2)
    if arr[mid] > val: 
        return binary_search(arr, val, mid+1, end) 
    elif arr[mid] < val: 
        return binary_search(arr, val, start, mid-1) 
    else: 
        return mid 

def fillPositions(scores):
    aux = 1
    prev = scores[0]
    for i in range(len(scores)):
        if scores[i] != prev:
            aux += 1
            prev = scores[i]
        positionHash.append(aux)

def updateScores(scores, newScore, position):
    size = len(scores)
    if position >= size:
        if newScore == scores[size -1]:
            positionHash.append(positionHash[size -1])
        else:
            positionHash.append(positionHash[size -1] + 1)
        scores.append(newScore)

    else:
        if position != 0 and scores[position -1] == newScore:
            positionHash.insert(position, positionHash[position -1])
        else:
            positionHash.insert(position, positionHash[position])
        scores.insert(position, newScore)
        # for i in range(position +1, size +1):
        #     positionHash[i] += 1

    return positionHash[position]

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    fillPositions(scores)

    position = len(scores) -1
    for i in range(len(alice)):
        # position = binary_search(scores, alice[i], 0, position)
        position = linear_search(scores, alice[i], position)
        # print(position)
        aux = updateScores(scores, alice[i], position)
        print(aux)

        # print("Score: ", alice[i], "Position: ", aux)
        # print("Leaderboard:")
        # for i in range(position -2, position +3):
        #     if i == position:
        #         print("> ", scores[i])
        #     elif i >= 0 and i < len(scores):
        #         print(scores[i])
        # print("")
        # input()

    return 0


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
