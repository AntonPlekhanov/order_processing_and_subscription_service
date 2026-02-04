import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String



async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Отправьте номер телефона для регистрации")


async def handle_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phone = update.message.text.strip()
    telegram_id = str(update.effective_user.id)

    try:
        engine = create_engine(
            f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
        )

        metadata = MetaData()

        customuser_table = Table('subscriptions_customuser', metadata,
            Column('id', Integer, primary_key=True),
            Column('phone', String),
            Column('telegram_id', String),
        )

        stmt = update(customuser_table)
        stmt = stmt.where(customuser_table.c.phone == phone)
        stmt = stmt.values(telegram_id=telegram_id)
        stmt = stmt.returning(customuser_table.c.id)

        with engine.begin() as conn:
            result = conn.execute(stmt)

            if result.fetchone():
                await update.message.reply_text("Регистрация прошла успешно")
            else:
                await update.message.reply_text("Пользователь с таким номером не найден")

    except Exception:
        await update.message.reply_text("Ошибка при регистрации")


def main():
    TOKEN = os.getenv('TOKEN')

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_phone))

    app.run_polling()


if __name__ == '__main__':
    main()