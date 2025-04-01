import asyncio


async def func_q():
    print('Test text')
    await asyncio.sleep(5)


async def func_a():
    print('Timing!')


async def main():
    await asyncio.gather(func_q(), func_a())


asyncio.run(main())
