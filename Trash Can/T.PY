from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Telegram bot token
TOKEN = "8900440841:AAHF7s73DOmuqMJJTLIMBr7D9hm_1488sf"

class TelegramBot:
    """Fast Telegram Bot with multiple commands"""
    
    def __init__(self, token):
        """Initialize the George Droid"""
        self.app = Application.builder().token(token).build()
        self.setup_handlers()
    
    def setup_handlers(self):
        """Setup command and message handlers"""
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("help", self.help_command))
        self.app.add_handler(CommandHandler("ping", self.ping))
        self.app.add_handler(CommandHandler("echo", self.echo))
        self.app.add_handler(CommandHandler("status", self.status))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send a message when /start is issued"""
        await update.message.reply_text("👋 Welcome!\nUse /help for commands (or /killme)")
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send help message with available commands"""
        await update.message.reply_text(
            "/start - Start bot\n/help - Show commands\n/ping - Pong\n/echo <text> - Echo text\n/status - Bot status"
        )
    
    async def ping(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Respond to ping command"""
        await update.message.reply_text("🏓 Pong! I shot him")
    
    async def echo(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Echo back the user's message"""
        if context.args:
            await update.message.reply_text(f"🔊 {' '.join(context.args)}")
        else:
            await update.message.reply_text("Usage: /echo <text>")
    
    async def status(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Show bot status"""
        await update.message.reply_text("✅ Online! (nope)")
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle regular text messages"""
        await update.message.reply_text(f"📝 {update.message.text}")
    
    def run(self):
        """Start the bot"""
        self.app.run_polling(allowed_updates=Update.ALL_TYPES)

# Main entry point
if __name__ == "__main__":
    bot = TelegramBot(TOKEN)
    bot.run()

