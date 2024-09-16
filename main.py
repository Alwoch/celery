from tasks import add

result=add.delay(4,4)
print(result.ready())
print(result.get(timeout=10))
#print(result.get(propagate=False))
