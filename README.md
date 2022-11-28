## bytes2base64

图片转base64，no import

open the picture with 'rb'

```
>>> a=bytes2base64(bytes("hello",'utf-8'))
>>> print(a)
aGVsbG8==
```

```python

from ciphers import BASE64

with open("img.png", "rb") as f:
    a = f.read()
    print(BASE64.bytes2base64(a))
```
## Vector2D
二维坐标类 Vector2D
|||
|--|--|
|实例化: | a = Vector2D(1,2) ;b = Vector2D(-3,2)|
|自反:  |  -a = <-1,-2>|
|绝对值: | abs(a) = 5**0.5|
|减法:  |  a+b = <-2,4>|
|加法:  |  a-b = <4,0>|
|数量积 | a*b=1|
|投影  |   a>>b|


```
实例化
    >>> a = Vector2D(1, 2)
    >>> b = Vector2D(2, 2)

    自反
    >>> print(-a)
    Vector2D<-1,-2>

    坐标相乘
    >>> print(a * b)
    6

    坐标与数字相乘
    >>> print(a * 4)
    Vector2D<4,8>

    与浮点数
    >>> print(a * 2.2)
    Vector2D<2.2,4.4>

    命名
    >>> qw = Vector2D(10, 2, name="Hello")
    >>> print(qw.name)
    Hello

    对应向量cos()
    >>> print(Vector2D.vcos(Vector2D(1, 0), Vector2D(0, 1)))
    0.0

    投影
    >>> print(a >> b)
    2.1213203435596424
```