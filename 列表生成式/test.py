L = ['Hello', 'World', 18, 'Apple', None]

print(
    [a.lower() for a in L  if isinstance(a,str)]
)