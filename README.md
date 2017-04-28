# glitzer
Pretty customizable borders around your print statements for the sake of emphasis

![Glitzer Demo](https://media.giphy.com/media/3og0ID4Eh1rSYGVNRe/giphy.gif)

### Installation
```python 
pip install glitzer
```

### Basic usage
```python 
from glitzer import glitz

glitz('Hello world!')
```

### Advanced usage
+ Configure border type
+ The default glitz border type is `'.'`. You can change this to any string of your choice.
```python
glitz('Hello world!', border='*')
```

+ Configure padding
+ The padding is the number of spaces before and after the printed text. You can easily customize this by specifying a `padding` keyword argument in `integer`
```python
glitz('Hello world', padding=5)
```

+ Configure number of borders
+ You can also configure the number of borders around your given text in `integer`.
```python
glitz('Hello world', num_borders=2)
```