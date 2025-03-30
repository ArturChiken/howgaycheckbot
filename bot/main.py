from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import random
import TOKEN

bot = Bot(token=TOKEN.BotToken)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Ты можешь вызвать меня в любом чате через @howgaycheckbot")

@dp.inline_query()
async def handle_inline_query(inline_query: types.InlineQuery):
    query = inline_query.query.strip()
    gaynumber = random.randint(0, 102)
    results = []

    if not query:
        if gaynumber == 101:
            results.extend([
                types.InlineQueryResultArticle(
                    id='Im101',
                    title='Check how gay are you?',
                    input_message_content=types.InputTextMessageContent(
                        message_text=f'🏳️‍🌈 I am {gaynumber}% gay! WTF!?!?!??!'
                    )
                )
            ])
        elif gaynumber == 102:
            results.extend([
                types.InlineQueryResultArticle(
                    id='Im1488',
                    title='Check how gay are you?',
                    input_message_content=types.InputTextMessageContent(
                        message_text=f'🏳️‍🌈 I am 1488% gay!'
                    )
                )
            ])
        else:
            results.extend([
                types.InlineQueryResultArticle(
                    id='HowIm',
                    title='Check how gay are you?',
                    input_message_content=types.InputTextMessageContent(
                        message_text=f'🏳️‍🌈 I am {gaynumber}% gay!'
                    )
                )
            ])
    else:
        if gaynumber == 101:
            name = query.strip()
            results.append(
                types.InlineQueryResultArticle(
                    id="You101",
                    title=f"Check how gay is {name}?",
                    input_message_content=types.InputTextMessageContent(
                        message_text=f'🏳️‍🌈 {name} is {gaynumber}% gay! WTF!?!?!??!'
                    ),
                )
            )
        elif gaynumber == 102:
            name = query.strip()
            results.append(
                types.InlineQueryResultArticle(
                    id="You1488",
                    title=f"Check how gay is {name}?",
                    input_message_content=types.InputTextMessageContent(
                        message_text=f'🏳️‍🌈 {name} is 1488% gay!'
                    ),
                )
            )
        else:
            name = query.strip()
            results.append(
                types.InlineQueryResultArticle(
                    id="HowYou",
                    title=f"Check how gay is {name}?",
                    input_message_content=types.InputTextMessageContent(
                        message_text=f'🏳️‍🌈 {name} is {gaynumber}% gay!'
                    ),
                )
            )
    await bot.answer_inline_query(
        inline_query.id,
        results=results,
        cache_time=0
    )



if __name__ == "__main__":
    dp.run_polling(bot)