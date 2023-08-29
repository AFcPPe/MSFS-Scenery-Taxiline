import json

from GlobalVars import *


def read(icao):
    with open(f'data/{icao}.org', 'r') as f:
        data = f.read().split('\n')
    da = []
    for i in range(len(data)):
        if len(data[i]) < 1:
            continue
        if data[i][0] == ';':
            continue
        da.append(data[i].replace(icao + ' ', '').split(' '))
    return da


def convertCord(org: str):
    parts = org.split('.')
    lis1 = float(parts[2] + '.' + parts[3]) / 60
    lis2 = float(lis1 + int(parts[1])) / 60
    lis3 = lis2 + int(parts[0][1:])
    prefix = ''
    if parts[0][0] == 'N' or parts[0][0] == 'E':
        prefix = ''
    elif parts[0][0] == 'W' or parts[0][0] == 'S':
        prefix = '-'
    return prefix + str(lis3)


def compose(data):
    pts = set()
    pats = []
    for each in data:
        pts.add(f'{convertCord(each[0])},{convertCord(each[1])}')
        pts.add(f'{convertCord(each[2])},{convertCord(each[3])}')
        # pts.add(tPoint.format(index+1,index,convertCord(each[0]),convertCord(each[1])))
        # print(tPoint.format(index+1,index,convertCord(each[0]),convertCord(each[1])))
        # index+=1
    lpts = list(pts)
    for each in data:
        # print(lpts.index(f'{convertCord(each[0])},{convertCord(each[1])}'))
        pats.append([lpts.index(f'{convertCord(each[0])},{convertCord(each[1])}'),lpts.index(f'{convertCord(each[2])},{convertCord(each[3])}')])
    with open('result.txt','w')as f:
        for i in range(len(lpts)):
            gp = lpts[i].split(',')
            f.write(tPoint.format(i+3,i+2,gp[0],gp[1]))
            f.write('\n')
        index = len(lpts)+4
        for each in pats:
            f.write(tPath.format(index,each[0]+2,each[1]+2))
            f.write('\n')
            index+=1
