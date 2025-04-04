from telethon import TelegramClient, events
from telethon.tl.types import MessageActionChatAddUser, MessageActionChatJoinedByLink

# 🔹 API-ключи пользователя
API_ID = 22254977  # Без кавычек
API_HASH = "db09f5e408a1dff1898cc1613ae18415"  # В кавычках

client = TelegramClient("userbot", API_ID, API_HASH)

# 🔹 Автоудаление сообщений о входе новых участников
@client.on(events.ChatAction())
async def delete_join_messages(event):
    if event.user_joined or event.user_added:
        await event.delete()

# 🔹 Команда для удаления старых сообщений `.deljoin`
@client.on(events.NewMessage(pattern=r"\.deljoin"))
async def delete_old_join_messages(event):
    chat = await event.get_chat()
    count = 0
    async for message in client.iter_messages(chat, limit=500):  
        if isinstance(message.action, (MessageActionChatAddUser, MessageActionChatJoinedByLink)):
            await message.delete()
            count += 1
    await event.respond(f"✅ Удалено {count} сообщений о входе участников.")

# Запуск бота
print("🚀 Userbot запущен! Вход в Telegram...")
client.start()
client.run_until_disconnected()
