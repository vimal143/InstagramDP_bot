from tokenize import Token
from telegram.ext import *
import tokenKey 
from instaloader import Instaloader, Profile
from traceback import format_exc

print("Bot Started....")
L=Instaloader()
def start_command(update,context):
    update.message.reply_text("Enter profile Url to get dp downloaded")


def help_command(update,context):
    update.message.reply_text("To get Url just google it")

def handle_message(update,context):
    msg = update.message.reply_text("Downloading...")
    query = update.message.text
    chat_id = update.message.chat_id
    try:
        dp=Profile.from_username(L.context,query).profile_pic_url
        context.bot.send_photo(chat_id=chat_id,photo=dp,caption="Thank You for using InstaDp_BOt made by Vimal_Pandey")
        msg.edit_text("finished.")
    except Exception as E:
        print(format_exc())
        msg.edit_text("Try again 😕😕 Check the username correctly")    
    

def error(update,context):
    print(f"Update {update} caused the error {context.error}")


def main():
    update= Updater(tokenKey.API_KEY,use_context=True)
    disp=update.dispatcher
    disp.add_handler(CommandHandler("Start",start_command))
    disp.add_handler(CommandHandler("Helo",help_command))
    disp.add_handler(MessageHandler(Filters.text,handle_message))
    disp.add_error_handler(error)

    update.start_polling()
    update.idle()


main()



