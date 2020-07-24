# Python Cookbook 数据结构与算法

## 1. 序列分解为单独变量

```Python
p = (4, 5)
x, y = p
```

## 2. 分解任意长度

```Python
items = [1, 10, 7, 4, 5, 6]
head, *tail = items

tail = [10, 7, 4, 5, 6]
```

## 3. 保存最后N个元素

deque( maxlen = N)创建了一个固定长度的队列。

如果不指定大小，可以在两端执行添加和弹出操作。

## 4. 找最大或最小N个元素

`heapq.heapify(list)`堆排序。nlargest() 和 nsmallest()求最大或最小N个元素。

## 5. 优先级队列

```Python
(prioroty, index, item)

heapq.heappop()
heapq.heappush()
```

## 6. 一键多值字典

```Python
d = defaultdict(list)
for key, value in pairs:
  d[key].append(value)
```

## 7. 保持字典有序

OrderedDict内部维护了一个双向链表。

```Python
json.dumps(d)

#输出有序json串
```

## 8. 字典计算

利用zip()将字典的键和值反转过来。

```Python
min(zip(prices.values(), prices.keys()))
max(zip(prices.values(), prices.keys()))
sorted(zip(prices.values(), prices.keys()))
```

zip()创建了一个迭代器，只能消费一次。

## 9. 两个字典找相同

字典的keys()方法会返回keys-view对象，keys支持常见的集合操作。

字典的items()方法返回由(key, value)对组成的items-view对象。这个对象支持类似的集合操作。

字典的values()方法并不支持集合操作。

## 10. 移除重复项

集合 + 生成器

## 11. 对切片命名

`slice(start, stop, step)`函数会创建一个切片对象，可以用在任何允许进行切片操作的地方。

## 12. 出现次数最多

在底层实现中，Counter是一个字典，在元素和它们出现的次数间做了映射。

```Python
Counter

most_common()

update()

+/-/*//
```


