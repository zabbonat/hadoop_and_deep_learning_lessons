from mrjob.job import MRJob

class MRRatingByUser(MRJob):

    def mapper(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield userID, float(rating)

    def reducer(self, userID, rating_list):
        total = 0
        numElements = 0
        for x in rating_list:
            total += x
            numElements += 1
            
        yield userID, round(float(total / numElements), 2)


if __name__ == '__main__':
    MRRatingByUser.run()