import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from telegram import InputFile

API_KEY = '7840981516:AAEqJNWYSMGXQT1sSgOaZHYCOgCyRkKBVG4'  # Replace with your bot's token
ADMIN_ID = 'admin id si'  # Replace with your admin ID

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


# Start command handler
async def start(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat.id
    text = "Salom botimizga xush kelibsiz."


    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id, text, reply_markup=reply_markup)

    # Send a photo with a clear caption
    await context.bot.send_photo(chat_id=chat_id, photo="https://t.me/uzb_php_bot/135",
                                 caption="**Send your file to edit**")


# Document handler
async def handle_document(update: Update, context: CallbackContext) -> None:
    message = update.message
    chat_id = message.chat.id
    document = message.document
    file_id = document.file_id
    file = await context.bot.get_file(file_id)

    # Get file path and download
    file_path = file.file_path
    file_url = f'https://api.telegram.org/file/bot{API_KEY}/{file_path}'

    # Download the file with appropriate filename based on file type
    file_extension = document.file_name.split('.')[-1]
    file_name = f"temp_file.{file_extension}"
    await file.download(file_name)

    try:
        # Perform editing operations on the file (replace this with your actual editing logic)
        # ...

        # Send the edited file back to the user
        with open(file_name, 'rb') as edited_file:
            await context.bot.send_document(chat_id=chat_id, document=edited_file, caption="Here's your edited file")
    except Exception as e:
        logger.error(f"Error processing file: {e}")
        await context.bot.send_message(chat_id, "An error occurred while processing your file. Please try again later.")
    finally:
        # Delete the temporary file
        os.remove(file_name)


# Main function to handle bot commands and messages
def main() -> None:
    # Create the Application and pass it your bot's API key
    application = Application.builder().token(API_KEY).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))

    # Start the Bot
    application.run_polling()


if __name__ == '__main__':
    main()