from telegram.ext import Updater, CommandHandler
from socket import socket, gethostbyname, AF_INET, SOCK_STREAM
from wakeonlan import send_magic_packet
message = "'Hi! Use /wol <MAC> <IP> <PORT> \n Where: <MAC> = your PC MAC-adress \n\n \n\n <IP> = your global ip. default ip address is 255.255.255.255 \n\n  <PORT> = open to world port the default port is 9 \n\n EXAMPLE: /wol 00:0a:95:9d:68 255.255.255.255  9"
def start(update, context):
    update.message.reply_text(message)




def wol(update, context): 
    chat_id = update.message.chat_id
    try:
        mac = context.args[0]
        ip = context.args[1]       
        port =  int(context.args[2])
        s = socket(AF_INET, SOCK_STREAM)
        result = s.connect_ex((ip, port))
        print(result)
        if(result == 0) :
            update.message.reply_text('Port: ' + str(port) + " is open")
        elif(result == 113):
            update.message.reply_text('Port: ' + str(port) + " is close")
        s.close()
    except (IndexError, ValueError):
        update.message.reply_text(message)

def main():
    """Run bot."""
    updater = Updater("746945498:AAGIBd3fjpv8lIu_ccPe45yVeyLGlid1bi4", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))
    dp.add_handler(CommandHandler("wol", wol,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))

    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()

#TODO 
#0) Создать бота+
#1) Бот спрашивает IP адресс + 
#2) Бот спрашивает мак адресс + 
#3) Бот спрашивает порт + 
#4) Бот предлгает сохранить пресет 
#5) Скрипт сохраняет все в базу
#6)  
#5) Бот будит компьютер на котором включен wol
