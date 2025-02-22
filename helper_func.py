#(©)Codexbotz

import base64
import re
import asyncio
from pyrogram import filters
from config import FORCE_SUB_CHANNEL_I, FORCE_SUB_CHANNEL_II, FORCE_SUB_CHANNEL_III, FORCE_SUB_CHANNEL_IV, FORCE_SUB_CHANNEL_V, FORCE_SUB_CHANNEL_VI, ADMINS
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors import FloodWait

async def subscribed_I(filter, client, update):
    if not FORCE_SUB_CHANNEL_I:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL_I, user_id = user_id)
    except UserNotParticipant:
        return False

    return member.status in ["creator", "administrator", "member"]:
 
async def subscribed_II(filter, client, update):
    if not FORCE_SUB_CHANNEL_II:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL_II, user_id = user_id)
    except UserNotParticipant:
        return False

    return member.status in ["creator", "administrator", "member"]:
    
 async def subscribed_III(filter, client, update):
    if not FORCE_SUB_CHANNEL_III:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL_III, user_id = user_id)
    except UserNotParticipant:
        return False

    return member.status in ["creator", "administrator", "member"]:
    
async def subscribed_IV(filter, client, update):
    if not FORCE_SUB_CHANNEL_IV:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL_IV, user_id = user_id)
    except UserNotParticipant:
        return False

    return member.status in ["creator", "administrator", "member"]:

async def subscribed_V(filter, client, update):
    if not FORCE_SUB_CHANNEL_V:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL_V, user_id = user_id)
    except UserNotParticipant:
        return False

    return member.status in ["creator", "administrator", "member"]:
    
  async def subscribed_VI(filter, client, update):
    if not FORCE_SUB_CHANNEL_VI:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL_VI, user_id = user_id)
    except UserNotParticipant:
        return False

    return member.status in ["creator", "administrator", "member"]:
    
    async def is_subscribed(filter, client, update):
    if not FORCE_SUB_CHANNEL_I:
        return True
    if not FORCE_SUB_CHANNEL_II:
        return True
    if not FORCE_SUB_CHANNEL_III:
        return True
    if not FORCE_SUB_CHANNEL_IV:
        return True
    if not FORCE_SUB_CHANNEL_V:
        return True
    if not FORCE_SUB_CHANNEL_VI:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(
            chat_id=FORCE_SUB_CHANNEL_II, user_id=user_id
        )
    except UserNotParticipant:
        return False
    try:
        member = await client.get_chat_member(
            chat_id=FORCE_SUB_CHANNEL_III, user_id=user_id
        )
    except UserNotParticipant:
        return False
    try:
        member = await client.get_chat_member(
            chat_id=FORCE_SUB_CHANNEL_IV, user_id=user_id
        )
    except UserNotParticipant:
        return False
    try:
        member = await client.get_chat_member(
            chat_id=FORCE_SUB_CHANNEL_V, user_id=user_id
        )
    except UserNotParticipant:
        return False
    try:
        member = await client.get_chat_member(
            chat_id=FORCE_SUB_CHANNEL_VI, user_id=user_id
        )
    except UserNotParticipant:
        return False
    try:
        member = await client.get_chat_member(
            chat_id=FORCE_SUB_CHANNEL_I, user_id=user_id
        )
    except UserNotParticipant:
        return False
    return member.status in ["creator", "administrator", "member"]
    
async def encode(string):
    string_bytes = string.encode("ascii")
    base64_bytes = base64.urlsafe_b64encode(string_bytes)
    base64_string = (base64_bytes.decode("ascii")).strip("=")
    return base64_string

async def decode(base64_string):
    base64_string = base64_string.strip("=") # links generated before this commit will be having = sign, hence striping them to handle padding errors.
    base64_bytes = (base64_string + "=" * (-len(base64_string) % 4)).encode("ascii")
    string_bytes = base64.urlsafe_b64decode(base64_bytes) 
    string = string_bytes.decode("ascii")
    return string

async def get_messages(client, message_ids):
    messages = []
    total_messages = 0
    while total_messages != len(message_ids):
        temb_ids = message_ids[total_messages:total_messages+200]
        try:
            msgs = await client.get_messages(
                chat_id=client.db_channel.id,
                message_ids=temb_ids
            )
        except FloodWait as e:
            await asyncio.sleep(e.x)
            msgs = await client.get_messages(
                chat_id=client.db_channel.id,
                message_ids=temb_ids
            )
        except:
            pass
        total_messages += len(temb_ids)
        messages.extend(msgs)
    return messages

async def get_message_id(client, message):
    if message.forward_from_chat:
        if message.forward_from_chat.id == client.db_channel.id:
            return message.forward_from_message_id
        else:
            return 0
    elif message.forward_sender_name:
        return 0
    elif message.text:
        pattern = "https://t.me/(?:c/)?(.*)/(\d+)"
        matches = re.match(pattern,message.text)
        if not matches:
            return 0
        channel_id = matches.group(1)
        msg_id = int(matches.group(2))
        if channel_id.isdigit():
            if f"-100{channel_id}" == str(client.db_channel.id):
                return msg_id
        else:
            if channel_id == client.db_channel.username:
                return msg_id
    else:
        return 0

subsALL = filters.create(is_subscribed)
subsCH_VI = filters.create(subscribed_VI)
subsCH_V = filters.create(subscribed_V)
subsCH_IV = filters.create(subscribed_IV)
subsCH_III = filters.create(subscribed_III)
subsCH_I = filters.create(subscribed_I)
subsCH_II = filters.create(subscribed_II)
