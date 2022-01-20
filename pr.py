import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

FIRST, SECOND = range(2)

ONE, TWO, THREE, FOUR, TIME = range(5)


def start(update, _):
    """Вызывается по команде `/start`."""
    user = update.message.from_user
    logger.info("Пользователь %s начал разговор", user.first_name)
    keyboard = [
        [
            InlineKeyboardButton("✅  Да", callback_data=str(ONE)),
            InlineKeyboardButton("❌  Нет", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        text=f'Привет👋 {user.first_name}. Я бот "Девми". Может участвовать в проекте?',
        reply_markup=reply_markup
    )
    return FIRST


def start_over(update, _):
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("✅  Да", callback_data=str(ONE)),
            InlineKeyboardButton("❌  Нет", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='Привет👋. Я бот  "Девми". Может участвовать в проекте?',
        reply_markup=reply_markup
    )
    return FIRST


def one(update, _):
    """Показ нового выбора кнопок"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton("Любое время ( рекомендуемое )",
                              callback_data='time-Любое время')],
        [
            InlineKeyboardButton("С 18:00 до 19:00",
                                 callback_data='time-18:19'),
            InlineKeyboardButton("С 19:00 до 20:00",
                                 callback_data='time-19:20'),
        ],
        # [InlineKeyboardButton("Выбрать точное время созвона( не рекомендуется )",
        #                                 callback_data=str(FOUR))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Я рад что ты с нами 😁. Выбери удобное время для созвона",
        reply_markup=reply_markup
    )
    return FIRST


def change_query_handler(update, _):
    query = update.callback_query
    query.answer()
    _, game_state = query.data.split("-")
    if game_state in ["Любое время", "18:19", "19:20"]:
        text = 'Отлично 👌, оставайся на связи. \n' \
               'За день до проекта я пришлю тебе всю инфу о проекте  и твоей группе 😎'
        query.edit_message_text(text)
        return SECOND


def two(update, _):
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(ONE)),
            InlineKeyboardButton("3", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Второй CallbackQueryHandler", reply_markup=reply_markup
    )
    return FIRST


def three(update, _):
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("⬅ Вернуться", callback_data=str(ONE)),
            InlineKeyboardButton("Я правда не могу 😞", callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Проекты очень помогают в обучении", reply_markup=reply_markup
    )
    return SECOND


def four(update, _):
    """Показ выбора кнопок"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("С 18:00 до 18:30", callback_data=str(TIME)),
            InlineKeyboardButton("С 18:30 до 19:00", callback_data=str(TIME)),
        ],
        [
            InlineKeyboardButton("С 19:00 до 19:30", callback_data=str(TIME)),
            InlineKeyboardButton("С 19:30 до 20:00", callback_data=str(TIME)),
        ],
        [
            InlineKeyboardButton("⬅ Вернуться", callback_data=str(ONE))
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Выбери удобное время для созвона", reply_markup=reply_markup
    )
    return FIRST


def time(update, _):
    """Показ выбора кнопок"""
    query = update.callback_query
    query.answer()
    text = 'Отлично 👌, оставайся на связи. За день до проекта я пришлю тебе всю инфу о проекте  и твоей группе 😎'
    query.edit_message_text(text=text)
    return ConversationHandler.END


def end(update, _):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Очень жаль, нам будет тебя не хватать 😢")
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater("5095913199:AAF3qSCedLOGI8dC4E_kraitqBOh2Khln2E")
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [
                CallbackQueryHandler(change_query_handler, pattern='^time-'),
                CallbackQueryHandler(one, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(two, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(three, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(four, pattern='^' + str(FOUR) + '$'),
                CallbackQueryHandler(time, pattern='^' + str(TIME) + '$'),
            ],
            SECOND: [
                CallbackQueryHandler(start_over, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(end, pattern='^' + str(TWO) + '$'),
            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()
