from aiogram import Bot, Dispatcher, executor, types
import python_weather
import random

API_TOKEN = '5790287476:AAGwge8L6D4bfdtJqbQN6spLP00Qxvfit4k'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
client = python_weather.Client(format=python_weather)

# echo
@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.get("Almaty, Kazakhstan")

    if weather.current.temperature > 0:
        cond = 'тепла'
    else:
        cond = 'холода'

    resp_msg = f'Сейчас в Алматы {weather.current.temperature}°C {cond}.\n{weather.current.description}\n'

    if weather.current.uv_index <= 3:
        uv = 'Низкий'
    elif weather.current.uv_index <= 6:
        uv = 'Средний'
    elif weather.current.uv_index <= 9:
        uv = 'Высокий'
    else:
        uv = 'Экстремальный'

    resp_msg += f'УФ-Индекс равняется {weather.current.uv_index}. {uv} класс опасности.'

    names = ["Ты сегодня выглядишь лучше всех :*", "Ты прекрасна!", "У тебя все получится!", "Я тебя люблю!", "Я скучаю по тебе!"]
    while True:
        a = (random.choice(names))
        resp_msg += f'\n\n{a}'
        break

    # Random horoscope frases
    first = ["Сегодня — идеальный день для новых начинаний.",
             "Оптимальный день для того, чтобы решиться на смелый поступок!",
             "Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.",
             "Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.",
             "Плодотворный день для того, чтобы разобраться с накопившимися делами."]
    second = ["Но помните, что даже в этом случае нужно не забывать про",
              "Если поедете за город, заранее подумайте про",
              "Те, кто сегодня нацелен выполнить множество дел, должны помнить про",
              "Если у вас упадок сил, обратите внимание на",
              "Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]
    second_add = ["отношения с друзьями и близкими.",
                  "работу и деловые вопросы, которые могут так некстати помешать планам.",
                  "себя и своё здоровье, иначе к вечеру возможен полный раздрай.",
                  "бытовые вопросы — особенно те, которые вы не доделали вчера.",
                  "отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]
    third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.",
             "Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.",
             "Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.",
             "Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.",
             "Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]


    resp_msg += f'\n\n{random.choice(first)}, {random.choice(second)}, {random.choice(second_add)}, {random.choice(third)}'


    await message.answer(resp_msg)

# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
