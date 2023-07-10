# 0x01. Python - Async
---
![meme](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/12/4aeaa9c3cb1f316c05c4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230710%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230710T064816Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=36dce2a1fdc6c967d8ec75ad74af587a32f70eeb4eeb13603293de8a8d45eeae)

## Resources
**Read or watch:**

* [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
* [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
* [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

* async and await syntax
* How to execute an async program with asyncio
* How to run concurrent coroutines
* How to create asyncio tasks
* How to use the random module

## Tasks
### Task 0. The basics of async
<Details>
Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.

Use the random module.

```
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))

bob@dylan:~$ ./0-main.py
9.034261504534394
1.6216525464615306
10.634589756751769
```
</Details>

