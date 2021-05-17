from telegram import *
from telegram.ext import *
import time
import keys as keys
import Responses as Responses
import Link_giving as LG

#printing output to make sure that bot is working
print("bot started")

#Creating all the commands for users
def start_command(update, context):
    update.message.reply_text("Type something to get started!\nIf you need help type /help")

def help_command(update, context):
    update.message.reply_text("Do you really need help? Use google then!")

def Link_calculus(update, context):
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = LG.Calculus.give_link()
    )

def Link_Tirkish(update, context):
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = LG.Turkish_OTH.give_link()
    )
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = LG.Turkish_KTL.give_link()
    )

def Link_Dmath(update, context):
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = LG.Dmath.give_link()
    )

def Link_LF(update, context):
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = LG.life_safety.give_link()
    )

def Link_OOP(update, context):
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = LG.OOP.give_link()
    )

def Link_English(update, context):
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = LG.English.give_link()
    )

def Link_Algebra(update, context):
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = LG.Algebra.give_link()
    )

def Link_Russian(update, context):
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = LG.Russian_Suralan.give_link()
    )
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = LG.Russian_Gulina.give_link()
    )

def Link_Physical_Training(update, context):
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = LG.Phy_girls.give_link()
    )
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = LG.Phy_boys.give_link()
    )

#Creating Massege handler to work trought user masseges
def hanndle_massage(update, context):
    text = str(update.message.text).lower()
    response = Responses.smart_responses(text)

    update.message.reply_text(response)

#Creating function to display all errors 
def error(update, context):
    print(f"Update \n{update} caused error \n{context.error}")

#Main function
def main():
    #setting up bot
    updater = Updater(keys.API_KEY, use_context= True)
    bot = updater.bot
    dp = updater.dispatcher

    #adding all commands to CommandHandler
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("Calculus",Link_calculus))
    dp.add_handler(CommandHandler("Turkish",Link_Tirkish))
    dp.add_handler(CommandHandler("Dmath", Link_Dmath))
    dp.add_handler(CommandHandler("Life_safety", Link_LF))
    dp.add_handler(CommandHandler("OOP", Link_OOP))
    dp.add_handler(CommandHandler("English", Link_English))
    dp.add_handler(CommandHandler("Algebra", Link_Algebra))
    dp.add_handler(CommandHandler("Russian", Link_Russian))
    dp.add_handler(CommandHandler("Physical", Link_Physical_Training))

    dp.add_handler(MessageHandler(Filters.text, hanndle_massage))

    dp.add_error_handler(error)

    #Letting bot get all the inputs from the users
    updater.start_polling()
    updater.idle()

#Initializing bot
if __name__ == '__main__' :
    main()