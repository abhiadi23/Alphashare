from pyrogram import Client
from database import Database
import asyncio

db = Database()

async def schedule_message_deletion(client: Client, file_uuid: str, chat_id: int, message_ids: list, delete_time: int):
    await asyncio.sleep(delete_time * 60)
    try:
        await client.delete_messages(chat_id, message_ids)
        await client.send_message(
            chat_id=chat_id,
            text=(
                "🚫 **Your video/file was successfully deleted ✅**"
             )
        )
        for msg_id in message_ids:
            await db.remove_file_message(file_uuid, chat_id, msg_id)
    except Exception as e:
        print(f"Error in auto-delete: {str(e)}")
