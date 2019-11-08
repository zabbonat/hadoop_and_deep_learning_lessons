from mrjob.job import MRJob

class MRRatingByMovie(MRJob):

    def mapper(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield movieID, float(rating)

    def reducer(self, movieID, rating_list):
        total = 0
        numElements = 0
        for x in rating_list:
            total += x
            numElements += 1
            
        yield movieID, round(float(total / numElements), 2)


if __name__ == '__main__':
    MRRatingByMovie.run()