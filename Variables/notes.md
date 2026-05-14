# Variables & Data Types

## Variables

A variable is used to store data in memory.

```python
a = 2505
print(a)
```
---

## Checking Data Type

Use `type()` to know the type of a variable.

```python
print(type(a))
```
---

## Basic Data Types

### 1. Integer (`int`)

Whole numbers (no decimal)

```python
a = 2505
```
---

### 2. Float (`float`)

Decimal numbers

```python
a1 = 8.5
```
---

### 3. String (`str`)

Text data (inside quotes)

```python
b = "AMAR"
```
---

### 4. Boolean (`bool`)

True or False values

```python
c = True
```
---

### 5. None Type (`NoneType`)

Represents no value / empty

```python
d = None
```
---

## Collections

### 6. List (`list`)

* Ordered collection
* Can store multiple data types
* Mutable (can change)

```python
list = [12, 34, ["Apple", "Banana"]]
```
---

### 7. Tuple (`tuple`)

* Ordered collection
* Immutable (cannot change)

```python
tuple = (25, 45, ["Variables, Datatypes"])
```
### 8. Dictionary (key-value pair)
* Data stored in key format

```python
student = {
    "name": "Amar",
    "age": 20,
    "course": "BTech"}
```

---

### Typecasting
```python
 Problem:
a = "2.1"
b = "3"
print(a + b)

 Output: "2.13" (string concatenation, NOT addition)
``` 
#### 1. Implicit Typecasting
Python automatically converts type
Example:
```python
print(5 + 2.0)  # int → float 
```
#### 2. Explicit Typecasting
Manually convert type
```python
print(float(a) + int(b))

 Output: 5.1
 ```
 ---

## ⚠️ Important Notes

* Use `()` for tuple, not `[]`
* `[]` always creates a list
* Avoid using names like `list`, `tuple` as variable names (they are built-in)
---
