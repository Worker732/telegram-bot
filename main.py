import os
import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext):
    welcome_text = (
        "✅Здравствуйте, данный бот поможет вам проверить человека на скам!\n\n"
        "⚡️Спасибо, что выбрали именно нашего бота для проверки скамеров\n\n"
        "🎲 Отправьте команду /check @имя_пользователя для проверки вам нужного человека."
    )
    update.message.reply_text(welcome_text)

def generate_random_id():
    return str(random.randint(1000000000, 9999999999))

def check_user(update: Update, context: CallbackContext):
    if not context.args or not context.args[0].startswith("@"):
        update.message.reply_text("Пожалуйста, укажите корректное имя пользователя. Например: /check @имя_пользователя")
        return

    username = context.args[0]

    if username.lower() == "@xllirtt_garant":
        photo_url = "https://ibb.co/xqFZKz4f"
        message_text = (
            "🖼Ник: @xllirtt_garant\n"
            "🆔id: 7253953831\n"
            "🕰 Ищу в базе данных...\n"
            "⭐️ Является Гарантом базы\n\n"
            "📊Всего пруфов: 600+\n"
            "🏡Канал с пруфами: @xllirtt_proofs\n"
            "‼️ Ник в Roblox: Ayalabestquenn\n\n"
            "📮Обязательно убедитесь что проверка сделана через оригинального бота: @Sa_Scam_Alert_bot"
        )
    else:
        photo_url = "https://ibb.co/HfQzkJ6w"
        random_id = generate_random_id()
        message_text = (
            f"🖼Ник: {username}\n"
            f"🆔id: {random_id}.\n"
            "🕰 Ищу в базе данных...\n"
            "🌌Является обычным пользователем.\n\n"
            "📮Обязательно убедитесь что проверка сделана через оригинального бота: @Sa_Scam_Alert_bot"
        )

    update.message.reply_photo(photo=photo_url, caption=message_text)

def main():
    TOKEN = os.getenv("BOT_TOKEN")
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("check", check_user))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
