## bytes2base64

图片转base64，no import

```python
import BASE64

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


```python
from vector import Vector2D

a = Vector2D(1, 2)
b = Vector2D(2, 2)
x = b
c = Vector2D(2, 2)
z = Vector2D(0, 0)

z.x = 1
print(-a, a * b, a * 4, a * 2.2, a * 2, a * a)

qw = Vector2D(10, 2, name="A")
print(qw.name)

print(Vector2D.vcos(Vector2D(0, 1), Vector2D(0, 1)))
print(a >> b)
```