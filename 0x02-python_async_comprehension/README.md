# 0x02. Python - Async Comprehension

![meme](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/12/ee85b9f67c384e29525b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230711%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230711T042534Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a95fe8772c03b4df4487946a6833a52605499a5325b1c472f39f2399f8220e9e)

## Resources
**Read or watch:**

* [PEP 530 – Asynchronous Comprehensions](https://peps.python.org/pep-0530/)
* [What’s New in Python: Asynchronous Comprehensions / Generators](https://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/)
* [Type-hints for generators](https://stackoverflow.com/questions/42531143/how-to-type-hint-a-generator-in-python-3)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

* How to write an asynchronous generator
* How to use async comprehensions
* How to type-annotate generators

## Tasks

### Task 0. Async Generator
<Details>
Write a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.

```
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())

bob@dylan:~$ ./0-main.py
[4.403136952967102, 6.9092712604587465, 6.293445466782645, 4.549663490048418, 4.1326571686139015, 9.99058525304903, 6.726734105473811, 9.84331704602206, 1.0067279479988345, 1.3783306401737838]
```
</Details>