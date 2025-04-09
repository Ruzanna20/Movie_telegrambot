import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

load_dotenv()
telegram_bot_token = os.getenv("telegram_bot_token")
OMDB_API_key = os.getenv("OMDB_API_key")

async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi👋! ՈՒղարկիր ֆիլմի անունը։")

async def movie_info(movie_name:str):
    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={OMDB_API_key}"

    response=requests.get(url)
    data=response.json()

    if data["Response"] == "False":
        return "Այդ ֆիլմը չի գտնվել։"
    
    return f"Ֆիլմի անուն: {data['Title']}\nՏարի: {data['Year']}\nՆկարագրություն: {data['Plot']}"

async def handle_message(update:Update,context):
    movie_name=update.message.text
    movie_info_text=await movie_info(movie_name)
    await update.message.reply_text(movie_info_text)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Բարի գալուստ! Գրիր ֆիլմի անունը, ես կասեմ դրա մասին տեղեկություններ։")

app = Application.builder().token(telegram_bot_token).build()
app.add_handler(CommandHandler("start", start))  
app.add_handler(CommandHandler("help", help)) 
app.add_handler(MessageHandler(filters.TEXT, handle_message)) 
app.run_polling()

