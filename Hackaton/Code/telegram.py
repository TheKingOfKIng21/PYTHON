import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(_name_)
def start(update, context):
    update.message.reply_text('¡Xopa io!')
def ayuda(update, context):
    update.message.reply_text('En que te ayudo??!')
def copia(update, context): update.message.reply_text(update.message.text)
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def sumar(update,context):
    try:
        numero1 = int(context.args[0])
        numero2 = int(context.args[1])

        suma = numero1 + numero2

        update.message.reply_text("La suma es "+str(suma))

    except (ValueError):
        update.message.reply_text("por favor utilice dos numeros")
def main():
    updater = Updater("5902155969:AAE-lVrn-_qudBVzIJ4nKwVS96w2YSrwhec", use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", ayuda))

    dp.add_handler(CommandHandler("sumar", sumar))

    dp.add_handler(MessageHandler(filters.text, copia))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

    if _name_ == '_main_':
        main()

        def run_discord():
            buttonPage.destroy()
            control_window = Tk()
            control_window.config(height=250, width=250, bg="white")
            control_window.title("Controlando el sistema")

            photo_powerOn = PhotoImage(file="poweron.png")
            photo_shutDown = PhotoImage(file="shutdown.png")

            control_label = Label(control_window, height=1, width=34,
                                  text="Para detener el bot, presione el botón.",
                                  font=("verdana", 8, "bold"))
            control_label.config(bg="green")
            control_label.place(x=15, y=50)

            shutDown_button = Button(control_window, height=70, width=60,
                                     image=photo_shutDown, bg="white", bd=0)
            shutDown_button.place(x=150, y=100)
            powerOn_button = Button(control_window, height=80, width=60,
                                    image=photo_powerOn, bg="white", bd=0)
            powerOn_button.place(x=50, y=100)

            control_window.mainloop()