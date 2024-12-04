---

# Bit Manipulation

## Check if the ith bit is set or not

1. First, we left shift `1` by `i` times and store the result in a variable called `temp`.  
2. Then, we perform a bitwise AND operation between the given number and `temp`.  
3. If the result is equal to `temp`, it means the ith bit in the given number is set.  
4. Otherwise, the ith bit is not set.

### Example:
Check if the 2nd bit in 13 is set:  
- 13 in binary is `1101`.  
- Left shift `1` by `2` times: this gives `0100` (stored in `temp`).  
- Perform bitwise AND: `1101 & 0100 = 0100`.  
- Since the result (`0100`) equals `temp`, the 2nd bit in 13 is **set**.

### Python Implementation:
```python
def is_ith_bit_set(num, i):
    temp = 1 << i
    return (num & temp) == temp

# Example usage:
print(is_ith_bit_set(13, 2))  # Output: True
```

---

## Swap two numbers without using a third variable

1. We can swap two numbers using the XOR operation.  
2. Start with two numbers, `a` and `b`.  
3. Perform the following steps:
   - `a = a XOR b`
   - `b = a XOR b` → This simplifies to `(a XOR b) XOR b`, which results in `a`.
   - `a = a XOR b` → This simplifies to `(a XOR b) XOR a`, which results in `b`.  
4. At this point, the values of `a` and `b` have been swapped successfully without using a third variable.

### Example:
Let’s say we have `a = 5` and `b = 7`:  
- Step 1: `a = a XOR b` → `5 XOR 7 = 2`, so now `a = 2`.  
- Step 2: `b = a XOR b` → `(2 XOR 7) = 5`, so now `b = 5`.  
- Step 3: `a = a XOR b` → `(2 XOR 5) = 7`, so now `a = 7`.  

Now, the values of `a` and `b` are swapped: `a = 7`, and `b = 5`.

### Python Implementation:
```python
def swap_without_temp(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

# Example usage:
a, b = swap_without_temp(5, 7)
print(a, b)  # Output: (7, 5)
```

---
