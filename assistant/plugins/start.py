from assistant import Sammy
from telethon import events, Button

PM_START_TEXT = """
**Hi {}**
I am a bot who works for @RaiChuOfficial and can detect spammers in groups can protect groups from then

**Click the below button for getting help menu!**
"""

@Sammy.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.reply(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.inline("Help & Commands", data="help")],
        [Button.url("CreDits", "https://t.me/OfficialShield")]])
       return

    if event.is_group:
       await event.reply("`I Am Alive 24/7!`")
       return
