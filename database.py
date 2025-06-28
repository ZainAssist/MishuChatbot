import motor.motor_asyncio
from config import MONGO_URI

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client.ananya_bot
users = db.users

async def save_user_name(user_id, name):
    await users.update_one({"_id": user_id}, {"$set": {"name": name}}, upsert=True)

async def save_birthday(user_id, birthday):
    await users.update_one({"_id": user_id}, {"$set": {"birthday": birthday}}, upsert=True)

async def get_user_name(user_id):
    user = await users.find_one({"_id": user_id})
    return user.get("name") if user else None

async def get_user_count():
    return await users.count_documents({})

async def get_all_users():
    all_users = await users.find({}).to_list(length=10000)
    return [user["_id"] for user in all_users]
