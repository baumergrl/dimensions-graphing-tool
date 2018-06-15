import csv

def placevector(i, vec):
    vectors = []
    with open('vector.csv', 'rb') as prevVec:
        vecReader = csv.reader(prevVec, delimiter=',')
        for row in vecReader:
            vectors.append(row)
    print(vectors)
    vectors[i] = vec
    print(vectors)
