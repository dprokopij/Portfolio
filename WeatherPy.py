import python_weather
import asyncio
import os


async def getweather():
    async with python_weather.Client(format=python_weather) as client:

        weather = await client.get("Almaty, Kazakhstan")

        if weather.current.temperature > 0:
            cond = 'тепла'
        else:
            cond = 'холода'

        print(f'Сейчас в Алматы {weather.current.temperature}°C {cond}.\n{weather.current.description}')

        if weather.current.uv_index <= 3:
            uv = 'Низкий'
        elif weather.current.uv_index <= 6:
            uv = 'Средний'
        elif weather.current.uv_index <= 9:
            uv = 'Высокий'
        else:
            uv = 'Экстремальный'

        print(f'УФ-Индекс равняется {weather.current.uv_index}. {uv} класс опасности.')

if __name__ == "__main__":
    # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
    # for more details
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())
