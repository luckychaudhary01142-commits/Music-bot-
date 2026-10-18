from pyrogram import types
from pyrogram.enums import ButtonStyle

from Elevenyts import app, config, lang


class Inline:
    def __init__(self):
        self.ikm = types.InlineKeyboardMarkup
        self.ikb = types.InlineKeyboardButton

    def cancel_dl(self, text) -> types.InlineKeyboardMarkup:
        return self.ikm([[self.ikb(text=f"✗  {text}", callback_data="cancel_dl", style=ButtonStyle.DANGER)]])

    def controls(
        self,
        chat_id: int,
        status: str = None,
        timer: str = None,
        remove: bool = False,
    ) -> types.InlineKeyboardMarkup:
        keyboard = []

        # FIX #1: `elif` -> dono `if` taaki status aur timer dono dikh sakein
        if status:
            keyboard.append(
                [self.ikb(text=f"◈  {status}", callback_data=f"controls status {chat_id}", style=ButtonStyle.PRIMARY)]
            )
        if timer:
            keyboard.append(
                [self.ikb(text=f"  {timer}", callback_data=f"controls status {chat_id}", style=ButtonStyle.PRIMARY)]
            )

        if not remove:
            # ── Main controls row ─────────────────────────────────
            keyboard.append(
                [
                    self.ikb(text="II", callback_data=f"controls pause {chat_id}"),
                    self.ikb(text="▷", callback_data=f"controls resume {chat_id}"),
                    self.ikb(text="↻", callback_data=f"controls replay {chat_id}"),
                    self.ikb(text="‣‣I", callback_data=f"controls skip {chat_id}"),
                    self.ikb(text="▢", callback_data=f"controls stop {chat_id}"),
                ]
            )
            # ── Bottom row ────────────────────────────────────────
            keyboard.append(
                [
                    self.ikb(text="🗑  ᴄʟᴏꜱᴇ", callback_data=f"controls close {chat_id}", style=ButtonStyle.DANGER),
                ]
            )

        return self.ikm(keyboard)

    def help_markup(
        self, _lang: dict, back: bool = False
    ) -> types.InlineKeyboardMarkup:
        # FIX #6: _lang se labels lene ki koshish (fallback ke saath)
        # Agar _lang mein key na ho to default hardcoded label use hoga.
        def label(key: str, default: str) -> str:
            try:
                return _lang.get(key, default) if isinstance(_lang, dict) else default
            except Exception:
                return default

        if back:
            # FIX #9: callback "help_main" -> "help" (langs_markup ke saath consistent)
            rows = [
                [self.ikb(text=label("back", "‹  ʙᴀᴄᴋ"), callback_data="help", style=ButtonStyle.SUCCESS)]
            ]
        else:
            rows = [
                [
                    self.ikb(text=label("admins", "ᴀᴅᴍɪɴꜱ"),            callback_data="help_admins",       style=ButtonStyle.PRIMARY),
                    self.ikb(text=label("auth", "ᴀᴜᴛʜ"),                  callback_data="help_auth",         style=ButtonStyle.PRIMARY),
                    self.ikb(text=label("broadcast", "ʙʀᴏᴀᴅᴄᴀꜱᴛ"),       callback_data="help_broadcast",    style=ButtonStyle.PRIMARY),
                ],
                [
                    self.ikb(text=label("blchat", "ʙʟ-ᴄʜᴀᴛ"),            callback_data="help_blchat",       style=ButtonStyle.PRIMARY),
                    self.ikb(text=label("bluser", "ʙʟ-ᴜꜱᴇʀ"),            callback_data="help_bluser",       style=ButtonStyle.PRIMARY),
                    self.ikb(text=label("gban", "ɢ-ʙᴀɴ"),                callback_data="help_gban",         style=ButtonStyle.PRIMARY),
                ],
                [
                    self.ikb(text=label("loop", "ʟᴏᴏᴘ"),                  callback_data="help_loop",         style=ButtonStyle.PRIMARY),
                    self.ikb(text=label("play", "ᴘʟᴀʏ"),                  callback_data="help_play",         style=ButtonStyle.PRIMARY),
                    self.ikb(text=label("queue", "ǫᴜᴇᴜᴇ"),                callback_data="help_queue",        style=ButtonStyle.PRIMARY),
                ],
                [
                    self.ikb(text=label("seek", "ꜱᴇᴇᴋ"),                  callback_data="help_seek",         style=ButtonStyle.PRIMARY),
                    self.ikb(text=label("shuffle", "ꜱʜᴜꜰꜰʟᴇ"),           callback_data="help_shuffle",      style=ButtonStyle.PRIMARY),
                    self.ikb(text=label("ping", "ᴘɪɴɢ"),                  callback_data="help_ping",         style=ButtonStyle.PRIMARY),
                ],
                [
                    self.ikb(text=label("stats", "ꜱᴛᴀᴛꜱ"),               callback_data="help_stats",        style=ButtonStyle.PRIMARY),
                    self.ikb(text=label("sudo", "ꜱᴜᴅᴏ"),                  callback_data="help_sudo",         style=ButtonStyle.PRIMARY),
                    self.ikb(text=label("maintenance", "ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ"),   callback_data="help_maintenance",  style=ButtonStyle.PRIMARY),
                ],
                [
                    self.ikb(text=label("back", "ʙᴀᴄᴋ"),                 callback_data="start",             style=ButtonStyle.DANGER),
                ],
            ]
        return self.ikm(rows)

    def langs_markup(self) -> types.InlineKeyboardMarkup:
        langs = [
            ("🇬🇧 English",    "en"), ("🇮🇳 Hindi",      "hi"),
            ("🇮🇳 Telugu",     "te"), ("🇰🇷 Korean",     "ko"),
            ("🇲🇲 Myanmar",    "my"), ("🇮🇩 Indonesian", "id"),
            ("🇧🇷 Portuguese", "pt"), ("🇸🇦 Arabic",     "ar"),
            ("🇪🇸 Spanish",    "es"), ("🇫🇷 French",     "fr"),
            ("🇷🇺 Russian",    "ru"), ("🇩🇪 German",     "de"),
            ("🇹🇷 Turkish",    "tr"), ("🇧🇩 Bengali",    "bn"),
            ("🇹🇭 Thai",       "th"), ("🇻🇳 Vietnamese", "vi"),
            ("🇯🇵 Japanese",   "ja"), ("🇨🇳 Chinese",    "zh"),
            ("🇵🇰 Urdu",       "ur"), ("🇮🇷 Persian",    "fa"),
        ]
        rows = []
        for i in range(0, len(langs), 2):
            row = [self.ikb(text=langs[i][0], callback_data=f"setlang_{langs[i][1]}", style=ButtonStyle.PRIMARY)]
            if i + 1 < len(langs):
                row.append(self.ikb(text=langs[i + 1][0], callback_data=f"setlang_{langs[i + 1][1]}", style=ButtonStyle.PRIMARY))
            rows.append(row)
        rows.append([self.ikb(text="‹  ʙᴀᴄᴋ", callback_data="help", style=ButtonStyle.SUCCESS)])
        return self.ikm(rows)

    def ping_markup(self, text: str = None) -> types.InlineKeyboardMarkup:
        # FIX #7: `text` ab optional hai (dead param nahi raha — backward compatible)
        # Agar aap `text` ko button label mein use karna chahte ho to yahan kar sakte ho.
        # Filhaal ignore karte hain, par signature safe hai.
        _ = text
        return self.ikm([
            [
                self.ikb(text="  ᴄʜᴀɴɴᴇʟ", url=config.SUPPORT_CHANNEL, style=ButtonStyle.PRIMARY),
                self.ikb(text="  ꜱᴜᴘᴘᴏʀᴛ",  url=config.SUPPORT_CHAT,    style=ButtonStyle.PRIMARY),
            ],
            [
                self.ikb(
                    text="  ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                    url=f"https://t.me/{app.username}?startgroup=true",
                    style=ButtonStyle.SUCCESS,
                ),
            ],
        ])

    def play_queued(
        self, chat_id: int, item_id: str, _text: str
    ) -> types.InlineKeyboardMarkup:
        # FIX #2: `item_id` ab skip callback mein pass hota hai (dead param nahi)
        # `_text` intentionally unused hai (leading underscore convention).
        return self.ikm([
            [
                self.ikb(text="▷",    callback_data=f"controls resume {chat_id}",       style=ButtonStyle.SUCCESS),
                self.ikb(text="II",   callback_data=f"controls pause {chat_id}",        style=ButtonStyle.PRIMARY),
                self.ikb(text="‣‣I",  callback_data=f"controls skip {chat_id} {item_id}", style=ButtonStyle.PRIMARY),
                self.ikb(text="▢",    callback_data=f"controls stop {chat_id}",         style=ButtonStyle.DANGER),
            ],
            [
                self.ikb(text="ᴄʟᴏꜱᴇ", callback_data=f"controls close {chat_id}", style=ButtonStyle.DANGER),
            ],
        ])

    def queue_markup(
        self, chat_id: int, _text: str, playing: bool
    ) -> types.InlineKeyboardMarkup:
        # FIX #3: `_text` ko button label ke roop mein use kiya (dead param nahi)
        _action = "pause" if playing else "resume"
        return self.ikm(
            [[self.ikb(text=_text, callback_data=f"controls {_action} {chat_id} q", style=ButtonStyle.SUCCESS)]]
        )

    def settings_markup(
        self, lang: dict, admin_only: bool, force_admin: bool, language: str, chat_id: int
    ) -> types.InlineKeyboardMarkup:
        # FIX #4: `language` ab display mein use hota hai
        play_mode_txt  = lang["admin_only_txt"] if admin_only  else lang["everyone"]
        force_mode_txt = lang["admin_only_txt"] if force_admin else lang["everyone"]
        lang_label = language.upper() if language else "—"
        return self.ikm([
            [
                self.ikb(text="  " + lang["play_mode"],  callback_data=f"controls status {chat_id}", style=ButtonStyle.PRIMARY),
                self.ikb(text=play_mode_txt,               callback_data="playmode",                   style=ButtonStyle.SUCCESS),
            ],
            [
                self.ikb(text="  " + lang["force_mode"], callback_data=f"controls status {chat_id}", style=ButtonStyle.PRIMARY),
                self.ikb(text=force_mode_txt,              callback_data="forcemode",                  style=ButtonStyle.SUCCESS),
            ],
            # Naya row: current language show + change button
            [
                self.ikb(text=f"  ʟᴀɴɢ: {lang_label}", callback_data="controls status " + str(chat_id), style=ButtonStyle.PRIMARY),
                self.ikb(text="ᴄʜᴀɴɢᴇ",                 callback_data="langs",                          style=ButtonStyle.SUCCESS),
            ],
        ])

    def start_key(
        self, lang: dict, private: bool = False
    ) -> types.InlineKeyboardMarkup:
        # FIX #5: `private` ab use hota hai — private chat mein "add me to group" nahi dikhega
        rows = []
        if not private:
            rows.append([
                self.ikb(
                    text="  " + lang["add_me"],
                    url=f"https://t.me/{app.username}?startgroup=true",
                    style=ButtonStyle.PRIMARY,
                )
            ])
        rows.append([
            self.ikb(text="  " + lang["help"], callback_data="help"),
        ])
        rows.append([
            self.ikb(text="  " + lang["support"], url=config.SUPPORT_CHAT),
            self.ikb(text=" " + lang["channel"],  url=config.SUPPORT_CHANNEL),
        ])
        rows.append([
            self.ikb(text="owner", url="https://t.me/light_speedi", style=ButtonStyle.DANGER),
        ])
        return self.ikm(rows)

    def yt_key(self, link: str) -> types.InlineKeyboardMarkup:
        # FIX #8: `copy_text` aur `ButtonStyle` version-dependent hain.
        # Safe fallback: try/except ke saath build karo, agar unsupported ho to plain button.
        try:
            return self.ikm([
                [
                    self.ikb(text="📋  ᴄᴏᴘʏ ʟɪɴᴋ", copy_text=link, style=ButtonStyle.PRIMARY),
                    self.ikb(text="▶  ᴏᴘᴇɴ ɪɴ ʏᴛ", url=link,       style=ButtonStyle.DANGER),
                ],
            ])
        except TypeError:
            # Purana Pyrogram / fork jisme copy_text ya style support nahi
            return self.ikm([
                [
                    self.ikb(text="📋  ᴄᴏᴘʏ ʟɪɴᴋ", url=link),
                    self.ikb(text="▶  ᴏᴘᴇɴ ɪɴ ʏᴛ", url=link),
                ],
            ])
