# Reverse Read

## installation

install :

```bash
pip install reverse-read
```

import :

```python
from reverse_read.reverse_read import reverse_read
```

## reverse_read()

Returns reversed text.

```python
# only the text-parameter is required

print(reverse_read(
    "text",
    "side" # <0 or 1>
))
```

## Example

```python
print(reverse_read("اثممخ")) # returns "hello"
```
