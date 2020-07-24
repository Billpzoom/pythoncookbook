from collections import namedtuple

Subscriber = namedtuple('Suscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')

print(sub)

print(sub.addr, sub.joined)

addr, joined = sub

print(len(sub), addr, joined)

Stock = namedtuple('Stock', ['name', 'shares', 'price']) 

def compute_cost(records): 
    total = 0.0 
    for rec in records: 
        s = Stock(* rec) 
        total += s.shares * s.price 
    return total

s = Stock('ACME', 100, 123.45)
print(s, s._replace(shares=75))

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

stock_prototype = Stock('', 0, 0.0, None, None)

def  dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name':'ACME', 'shares':100, 'price':123.45}
print(dict_to_stock(a))

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))