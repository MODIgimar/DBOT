from telegram import Update, BotCommand
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7583325295:AAEVkxxcSLzCzAQJP0Z-aZkL4cH12Fv5WuU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Welcome! Use /help to see available commands.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show help menu\n"
        "/steamtools - Steam tools\n"
        "/tutorial_video - Watch the tutorial video\n"
        "/lua_files - Lua files\n"
        "/credit - View my wallet\n"
        "/mygithub - View my GitHub profile"
    )

async def steam_tools(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = "🔧 Download SteamTools / Password Winrar: `retchX`\n[Click here](https://www.mediafire.com/file/c8inrqa50xeteth/SteamTools.rar/file)"
    await update.message.reply_text(message, parse_mode="Markdown")

async def tutorial_video(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = "🎥 Watch the tutorial video here:\n[Click here to watch](https://youtu.be/Twqa-sPbxqQ)"
    await update.message.reply_text(message, parse_mode="Markdown")

async def lua_files(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = "📝 Download Lua Files:\n[Click here for Lua files](https://www.mediafire.com/file/42s6l768qfdktrs/Lua+Files.txt/file)"
    await update.message.reply_text(message, parse_mode="Markdown")

async def credit(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = "My wallet USDT → `!!!` (Click to copy)"
    await update.message.reply_text(message, parse_mode="Markdown")

async def my_github(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    github_link = "https://github.com/m9wdSsyber?tab=repositories"  # ضع رابط حسابك الفعلي هنا
    message = f"🌐 Check out my GitHub profile:\n[Click here]({github_link})"
    await update.message.reply_text(message, parse_mode="Markdown")

async def set_menu_commands(app: Application) -> None:
    commands = [
        BotCommand("start", "Start the bot"),
        BotCommand("help", "Show help menu"),
        BotCommand("steamtools", "Steam tools"),
        BotCommand("tutorial_video", "Watch the tutorial video"),
        BotCommand("lua_files", "Download Lua files"),
        BotCommand("credit", "View my wallet"),
        BotCommand("mygithub", "View my GitHub profile")  # ✅ تعديل اسم الأمر ليكون بحروف صغيرة
    ]
    await app.bot.set_my_commands(commands)

def main():
    app = Application.builder().token(TOKEN).post_init(set_menu_commands).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("steamtools", steam_tools))
    app.add_handler(CommandHandler("tutorial_video", tutorial_video))
    app.add_handler(CommandHandler("lua_files", lua_files))
    app.add_handler(CommandHandler("credit", credit))
    app.add_handler(CommandHandler("mygithub", my_github))  # ✅ تعديل هنا أيضًا

    print("✅ Bot is running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
