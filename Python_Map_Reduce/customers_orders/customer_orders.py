from mrjob.job import MRJob
from mrjob.step import MRStep
import re

class MRCustomerOrderCounter(MRJob):
    def mapper(self, key, line):
        (custID, itemID, orderAmt) = line.split(',')
        yield custID, float(orderAmt)

    def reducer(self, custID, orders):
        yield custID, sum(orders)

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_customers,
                   reducer=self.reducer_count_orders),
            MRStep(mapper=self.mapper_make_orders_key,
                   reducer = self.reducer_output_orders)
        ]

    def mapper_get_customers(self, key, line):
        (custID, itemID, orderAmt) = line.split(',')
        yield custID, float(orderAmt)

    def reducer_count_orders(self, custID, orders):
        yield custID, sum(orders)

    def mapper_make_orders_key(self, custID, count):
        yield '%04.02f'%float(count), custID

    def reducer_output_orders(self, count, customers):
        for custID in customers:
            yield custID,float(count)

if __name__ == '__main__':
    MRCustomerOrderCounter.run()



