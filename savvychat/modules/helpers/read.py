from config import OWNER_USERNAME, SUPPORT_GRP
from savvychat import savvychat

START = """
๏ ʜᴇʏ {},
ɪ ᴀᴍ {}💞
ʏᴏᴜʀ ᴀɪ ᴄᴏᴍᴘᴀɴɪᴏɴ.
ʟᴇᴛ'ꜱ ᴄʜᴀᴛ ᴀɴᴅ ᴇxᴘʟᴏʀᴇ.
ᴛʜᴇ ᴅᴇᴘᴛʜꜱ ᴏꜰ ᴄᴏɴᴠᴇʀꜱᴀᴛɪᴏɴ ᴛᴏɢᴇᴛʜᴇʀ!
ꜰᴇᴇʟ ꜰʀᴇᴇ ᴛᴏ ᴀꜱᴋ ᴍᴇ ᴀɴʏᴛʜɪɴɢ ᴏʀ ꜱʜᴀʀᴇ 
ʏᴏᴜʀ ᴛʜᴏᴜɢʜᴛꜱ.
ɪ'ᴍ ʜᴇʀᴇ ᴛᴏ ʟɪꜱᴛᴇɴ ᴀɴᴅ ᴇɴɢᴀɢᴇ ɪɴ ᴍᴇᴀɴɪɴɢꜰᴜʟ ᴅɪꜱᴄᴜꜱꜱɪᴏɴꜱ ᴡɪᴛʜ ʏᴏᴜ.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴛʏᴘᴇ /help ɪɴ ᴍʏ ᴘᴍ. 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 """

help_1 = """ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴄᴀᴛᴇɢᴏʀʏ ғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ɢᴇᴛ ʜᴇʟᴩ.\nᴀsᴋ ʏᴏᴜʀ ᴅᴏᴜʙᴛs ᴀᴛ <a href={0}>sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ</a>\n\nᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : <code>/</code>"""

help_2 = """ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ᴍʏ ʜᴇʟᴘ ᴍᴇɴᴜ ɪɴ ʏᴏᴜʀ ᴘᴍ."""
HELP_1 ="""
<b><u>ᴘɪɴɢ :</b></u>
Available commands:
➻ /ping ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴛʜᴇ ᴘɪɴɢ ᴏғ ʙᴏᴛ.
───────────────
<b>||©️ 𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆||</b>
"""
HELP_2 ="""
<b><u>ᴄʜᴀᴛ-ʙᴏᴛ :</b></u>
Available commands:
➻ /chatbot ᴛᴏ ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ ᴛʜᴇ ᴄʜᴀᴛ-ʙᴏᴛ.
๏ ɴᴏᴛᴇ ➻ ᴛʜᴇ ᴀʙᴏᴠᴇ ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ ᴄʜᴀᴛʙᴏᴛ ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ ᴏɴʟʏ!!
───────────────
<b>||©️ 𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆||</b>
"""
HELP_3 ="""
<b><u>ɪᴅ :</b></u>
Available commands:
➻ /id ғᴏʀ ғɪɴᴅɪɴɢ ᴄʜᴀᴛ ɪᴅ ᴏʀ ᴜsᴇʀ ɪᴅ 
**───────────────**
<b>||©️ 𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆||</b>
"""
HELP_4 ="""
<b><u>ᴄʜᴀᴛ-ɢᴘᴛ :</b></u>
Available commands:
➻ /ask ➠ ǫᴜᴇʀɪᴇs ᴛʜᴇ ᴀɪ ᴍᴏᴅᴇʟ ᴛᴏ ɢᴇᴛ ᴀ ʀᴇsᴘᴏɴsᴇ ᴛᴏ ʏᴏᴜʀ ǫᴜᴇsᴛɪᴏɴ.
───────────────
<b>||©️ 𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆||</b>
"""
HELP_5 ="""
<b><u>ᴀɪ ɪᴍɢ ɢᴇɴ :</b></u>
ɢᴇɴᴇʀᴀᴛᴇ ɪᴍᴀɢᴇ ғʀᴏᴍ ᴘʀᴏᴍᴘᴛ
Available commands:
➻ /generate [ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʀᴏᴍᴘᴛ]
 ───────────────
<b>||©️ 𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆||</b>
"""
HELP_6 ="""
<b><u>ᴍᴀᴛʜs :</b></u>
Available commands:
➻ /math sᴏʟᴠᴇs ᴍᴀᴛʜᴇᴍᴀᴛɪᴄᴀʟ ᴘʀᴏʙʟᴇᴍs ᴀɴᴅ ᴇǫᴜᴀᴛɪᴏɴs.
 ───────────────
<b>||©️ 𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆||</b>
"""
HELP_7 ="""
<b><u>ɢʀᴏᴜᴘ ᴅᴀᴛᴀ :</b></u>
Available commands:
➻ /groupdata ᴛᴏ ғɪɴᴅ ᴅᴀᴛᴀ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ.
───────────────
<b>||©️ 𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆||</b>
"""
HELP_8 ="""
<b><u>ɢʀᴏᴜᴘ ɪɴғᴏ :</b></u>
Available commands:
➻ /groupinfo [ᴜsᴇʀɴᴀᴍᴇ ᴏғ ɢʀᴏᴜᴘ] ᴛᴏ ғɪɴᴅ ɪɴғᴏ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ.
───────────────
<b>||©️ 𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆||</b>
"""
HELP_9 ="""
<b><u>ɪᴍᴀɢᴇ :</b></u>
Available commands:
➻ /image <ǫᴜᴇʀʏ> sᴄʀᴀᴘs ɪᴍᴀɢᴇ ғʀᴏᴍ ᴘɪɴᴛʀᴇsᴛ.
───────────────
<b>||©️ 𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆||</b>
"""
HELP_10 ="""
<b><u>ᴊᴏᴋᴇ :</b></u>
Available commands:
➻ /joke ғᴏʀ ʀᴀɴᴅᴏᴍ ᴊᴏᴋᴇs.
───────────────
<b>||©️ 𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆||</b>
"""
HELP_11 ="""
<b><u>sᴛᴀᴛs :</b></u>
ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ʜᴏᴡ ᴍᴀɴʏ ᴜsᴇʀ ᴀʀᴇ ᴜsɪɴɢ ᴛʜᴇ ʙᴏᴛ
Available commands:
➻ /stats ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ʙᴏᴛ sᴛᴀᴛs.
───────────────
<b>||©️ 𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆||</b> 
"""
HELP_12 ="""
<b><u>ᴛᴇʟᴇɢʀᴀᴘʜ :</b></u>
Available commands:
➻ /tgm ᴏʀ /telegraph [ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇᴅɪᴀ]
───────────────
<b>||©️ 𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆||</b>
"""
HELP_13 ="""
<b><u>ɢʀᴀᴘʜ.ᴏʀɢ :</b></u>
Available commands:
➻ /graph [ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇᴅɪᴀ]
───────────────
<b>||©️ 𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆||</b>
"""
HELP_14 ="""
<b><u>ᴛʀᴀɴsʟᴀᴛᴇ :</b></u>
Available commands:
➻ /tr ➠ ᴛʀᴀɴsʟᴀᴛᴇs ᴛᴇxᴛ.
───────────────
<b>||©️ 𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆||</b>
"""
HELP_15 ="""
<b><u>ᴡʀɪᴛᴇ :</b></u>
Available commands:
➻ /write <ǫᴜᴇʀʏ> ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ғᴏʀ ᴡʀɪᴛᴇ ᴛʜᴇ ᴛᴇxᴛ ᴏɴ ᴘᴀᴘᴇʀ.
───────────────
<b>||©️ 𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆||</b>
"""
HELP_16 ="""
<b><u>sᴏɴɢ :</b></u>
Available commands:
➻ /song <ǫᴜᴇʀʏ> ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ sᴏɴɢ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ.
───────────────
<b>||©️ 𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆||</b>
"""
HELP_17 ="""
<b><u>ʙᴀʀᴅ :</b></u>
Available commands:
➻ /bard ғᴏʀ ᴜsɪɴɢ ʙᴀʀᴅ ᴀɪ.
───────────────
<b>||©️ 𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆||</b>
"""
HELP_18 ="""
<b><u>ʙʟᴀᴄᴋʙᴏx :</b></u>
Available commands:
➻ /blackbox ғᴏʀ ᴜsɪɴɢ ʙʟᴀᴄᴋʙᴏx ᴀɪ.
───────────────
<b>||©️ 𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆||</b>
"""
HELP_19 ="""
<b><u>ᴠɪᴅᴇᴏ :</b></u>
Available commands:
➻ /video <ǫᴜᴇʀʏ> ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ᴠɪᴅᴇᴏ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ.
───────────────
<b>||©️ 𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆||</b>
"""
HELP_20 ="""
<b><u>ᴄᴏsᴘʟᴀʏ :</b></u>
Available commands:
➻ /cosplay ᴏʀ /ncosplay ғᴏʀ ʀᴀɴᴅᴏᴍ ᴄᴏsᴘʟᴀʏs.
───────────────
<b>||©️ 𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆||</b>
"""
HELP_21 ="""
<b><u>ɢᴀᴍᴇs :</b></u>
Play Game With Emojis:
Available commands:
➻ /dice - Dice 🎲
➻ /dart - Dart 🎯
➻ /basket - Basket Ball 🏀
➻ /ball - Bowling Ball 🎳
➻ /football - Football ⚽
➻ /jackpot - Spin slot machine 🎰
───────────────
<b>||©️ 𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆||</b>
"""
HELP_22 ="""
<b><u>ʀᴇᴇʟ :</b></u>
Available commands:
➻ /reel ᴏʀ /ig <ʟɪɴᴋ> ғᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ʀᴇᴇʟ ғʀᴏᴍ ɪɴsᴛᴀɢʀᴀᴍ.
───────────────
<b>||©️ 𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆||</b>
"""
HELP_23 ="""
<b><u>ʙʀᴏᴀᴅᴄᴀsᴛ :</b></u>
Available commands:
➻ /broadcast ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴍsɢ ᴛᴏ ᴜsᴇʀs ᴀɴᴅ ᴄʜᴀᴛs.
───────────────
<b>||©️ 𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆||</b>
"""
HELP_24 = """
<b><u>ᴡᴀɪғᴜ :</b></u>
Available commands:
➻ /waifu ғᴏʀ ғɪɴᴅɪɴɢ ʀᴀɴᴅᴏᴍ ᴡᴀɪғᴜs.
───────────────
<b>||©️ 𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆||</b>
"""


ABOUT_READ = f"""
**➻ [{savvychat.name}](https://t.me/{savvychat.username}) ɪs ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛ-ʙᴏᴛ.**
**➻ [{savvychat.name}](https://t.me/{savvychat.username}) ʜᴀᴠᴇ ᴍᴀɴʏ ᴀɪ ᴍᴏᴅᴇʟs sᴜᴄʜ ᴀs ᴄʜᴀᴛɢᴘᴛ,ʙɪɴɢ,ʙʟᴀᴄᴋʙᴏx,ʙᴀʀᴅ ᴀɴᴅ sᴏ ᴏɴ.**
**➻ [{savvychat.name}](https://t.me/{savvychat.username}) ʜᴇʟᴘs ɪɴ sᴏʟᴠɪɴɢ ᴘʀᴏʙʟᴇᴍs ᴀɴᴅ ᴇxᴘʟᴀɪɴɪɴɢ ᴛᴏᴘɪᴄs ʀᴇʟᴀᴛᴇᴅ ᴛᴏ sᴛᴜᴅʏ.**
**➻ [{savvychat.name}](https://t.me/{savvychat.username}) ʀᴇᴘʟɪᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴛᴏ ᴀ ᴜsᴇʀ.**
**➻ ᴡʀɪᴛᴛᴇɴ ɪɴ [ᴘʏᴛʜᴏɴ](https://www.python.org) ᴡɪᴛʜ [ᴍᴏɴɢᴏ-ᴅʙ](https://www.mongodb.com) ᴀs ᴀ ᴅᴀᴛᴀʙᴀsᴇ**
**──────────────**
**➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʙᴀsɪᴄ ʜᴇʟᴩ ᴀɴᴅ ɪɴғᴏ ᴀʙᴏᴜᴛ [{savvychat.name}](https://t.me/{savvychat.username})**
"""
