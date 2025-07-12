from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = '7742192997:AAHvYU-10L3gXDA0tn37yv8z59oZdqLNPZA'
async def only_video_notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
   
    if update.message and update.message.video_note:
        return  
   
    try:
        await update.message.delete()
    except Exception as e:
        print('Ошибка при удалении:', e)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, only_video_notes))

print('Бот запущен! Ждёт сообщений...')
app.run_polling()
