from asyncio import Runner

from core.scripts.leave_comments import leave_comments


async def main():
    await leave_comments()


if __name__ == '__main__':
    with Runner() as runner:
        runner.run(main())
