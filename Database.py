import csv
import os
import datetime
from collections import defaultdict
import itertools
"""
def create_csv(day,month,location='Desktop',year='2016')
    '''Creates the CSV files'''
    with open(os.path.expanduser('~')+'//'+location+day+'-'+month+'-'+year+'.csv', 'a+') as f:
        writer = csv.writer(f)
        writer.writerow()

"""
class Item:
    def __init__(self,day=0,month=0,year=2016,buy=False,local_amount=0):
        # buy true = Buying, buy false = Selling
        self.day = day
        self.month = month
        self.year = year
        self.buy=buy
        self.absolute=local_amount
        if buy:
            self.local=self.absolute
        else:
            self.local=self.absolute*-1

        self.date = datetime.date(year,month,day)

    def date_str(self):
        """Returns the Date as a string DD-MM-YYYY"""
        return (str(self.day)+'-'+str(self.month)+'-'+str(self.year))



    def __str__(self):
        return self.date_str() + '|' + str(self.local)

    def __repr__(self):
        return '<item.Item object $' + str(self.local)+ '>'

class Database:
    def __init__(self):
        self.database = defaultdict(list)
        self.buys = defaultdict(list)
        self.sells = defaultdict(list)



    def add_item(self,item):
        '''Adds an item to the database'''
        assert type(item) == Item
        self.database[item.date].append(item)
        if item.buy is True:
            self.buys[item.date].append(item)
        else:
            self.sells[item.date].append(item)


    def sum_day(self, day=None):
        '''Returns the total money of either the whole database or one day'''
        ret = 0
        if day is None:
            for i in self.database:
                for z in self.database[i]:
                    ret += z.local

        else:
            for i in self.database[day]:
                ret += i.local

        return ret

    def items_day(self, day=None):
        '''Returns all objects of 1 day or of the whole database'''
        assert type(day) is datetime.date or day is None
        if day is None:
            return list(itertools.chain(*self.database.values()))

        else:
            return self.database[day]







x = Item(2,9,2016,True,1000)
z = Item(4,5,2020,False,400)
w = Database()
u = Item(2,9,2016,False, 200)
w.add_item(x)
w.add_item(z)
w.add_item(x)
w.add_item(u)
w.add_item(u)
w.add_item(z)

print(w.database)