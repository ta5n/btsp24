# Live Session Examples



1. Example: 

```python
a = 5
b = 4
if a < 6: 
    print("A", end="")
if b < 5: 
    print("B", end="")
else: 
    print("C")
```



2. Example: 

```python
a = 5
b = 4
if a < 6:
    print("A", end="")
if b > 4:
    print("B", end="")
else:
    print("C", end="")
```



3. Example: 

```python
a = 5
b = 4
if a < 6 and b < 7:
    print("1", end="")
elif a > 3 or b > 1:
    print("2", end="")
else:
    print("3", end="")
```



4. Example: 

```python
a = 5
b = 4
if b < a:
    if a > 6:
        print("1", end="")
    else:
        print("2", end="")
else:
 print("3", end="")
```



5. Example: 

```python
for i in range(1, 10, 3):
    print(i, end="")
```



6. Example: 

```python
for i in range(10, 1, -1):
    if i == 10:
        print("1", end="")
        break
    print(i, end="")
print("2", end="")
```



7. Example: 

```python
i = 4
while i > 0:
    print(i, end="")
```



8. Example: 

```python
i = 3
while i > 0: 
    print(i, end="") 
    i -= 1 
    if i < 0:
        break
    else:
        continue

else:
    print("A", end="")
```



9. Example: 

```python
def func(a):
    print(a, end="")
	func(2)func(3) 
```



10. Example: 

```python
def func(a=2):
    print(a, end="")
    func(5)func()func(2)
```



11. Example: 

```python
def f(a):
    carpim = 1
    for i in range(a, 0, -1):
        carpim *= i
    return carpim

deger = f(3)
print(deger)
```



12. Example: 

```python
def func(a, b = 2):
    global N
    N = a + b
    print(N, end="")

func(1, 1)
func(1)
print(N, end="")
```