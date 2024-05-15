# START CODING

from functions import *


@dp.message(CommandStart())
async def start(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"<b>👋 Salom {message.from_user.full_name}, bu botda siz o'zingiz uchun kerakli maxsulotlarni sotib olishingiz mumkin</b>",
        reply_markup=menu,
    )


@dp.callback_query(F.data == "result")
async def result(callback: CallbackQuery):
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer(
        text=f"<b>👋 Salom {callback.message.chat.full_name}, bu botda siz o'zingiz uchun kerakli maxsulotlarni sotib olishingiz mumkin</b>",
        reply_markup=menu,
    )


@dp.callback_query(F.data == "shop")
async def sett(callback: CallbackQuery):
    r = select_info("kategoriya")
    if r == False:
        await callback.answer(text="Kategoriyalar mavjud emas", show_alert=True)
    else:
        await bot.delete_message(callback.message.chat.id, callback.message.message_id)

        btn = InlineKeyboardBuilder()
        for i in r:
            btn.add(
                InlineKeyboardButton(text=f"{i[1]}", callback_data=f"shops**{i[1]}")
            )
        btn.add(InlineKeyboardButton(text="◀️ Orqaga", callback_data="result"))
        btn.adjust(2)
        await callback.message.answer(
            text="Kategoriyalardan birini tanlang:",
            reply_markup=btn.as_markup(),
        )


@dp.callback_query(F.data.startswith("shops**"))
async def shops(callback: CallbackQuery):
    action = callback.data.split("**")
    key = action[1]
    btn = InlineKeyboardBuilder()
    r = select_info("maxsulotlar")
    m = table_info("maxsulotlar", "kategoriya", key)
    if m == False:
        await callback.answer("Ushbu bo'lim uchun maxsulot topilmadi", show_alert=True)
    else:
        await bot.delete_message(callback.message.chat.id, callback.message.message_id)

        for i in r:
            if i[2] == f"{key}":
                btn.add(
                    InlineKeyboardButton(text=f"{i[3]}", callback_data=f"view**{i[1]}")
                )
        btn.add(InlineKeyboardButton(text="◀️ Orqaga", callback_data="shop"))
        btn.adjust(1)
        await callback.message.answer(
            text="Kerakli maxsulotni tanlang.", reply_markup=btn.as_markup()
        )


@dp.callback_query(F.data.startswith("view**"))
async def views(callback: CallbackQuery):
    action = callback.data.split("**")
    key1 = action[1]
    r = select_info("maxsulotlar")
    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=f"➕ 1", callback_data=f"w**{key1}**1**1**plus"
                ),
                InlineKeyboardButton(
                    text=f"➖ 1", callback_data=f"w**{key1}**1**1**minus"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🛒 Savatga qo'shish", callback_data=f"qosh**{key1}**1"
                )
            ],
        ]
    )
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)

    for i in r:
        if str(i[1]) == str(key1):
            print(i[1], key1)
            await callback.message.answer_photo(
                photo=f"{i[7]}",
                caption=f"""⚡️ Kategoriya: {i[2]}
                               
💥 {i[3]}
                
ℹ️ Mahsulot haqida:
<i>{i[4]}</i>

🈁 Mahsulotdan {i[5]} ta qoldi

💰 Mahsulot narxi: {i[6]} so'm

💥 1x {i[6]}""",
                reply_markup=btn,
            )


@dp.callback_query(F.data.startswith("w**"))
async def views(callback: CallbackQuery):
    action = callback.data.split("**")
    key1 = action[1]
    key2 = action[2]
    key3 = action[3]
    key4 = action[4]
    r = select_info("maxsulotlar")
    if key4 == "plus":
        t = int(key3) + 1
        btn = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=f"➕ 1", callback_data=f"w**{key1}**{key2}**{t}**plus"
                    ),
                    InlineKeyboardButton(
                        text=f"➖ 1", callback_data=f"w**{key1}**{key2}**{t}**minus"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="🛒 Savatga qo'shish",
                        callback_data=f"qosh**{key1}**{t}",
                    )
                ],
            ]
        )
        for i in r:
            if str(i[1]) == str(key1):
                if int(i[5]) < t:
                    await callback.answer("Maxsulot chegarasiga yetdi")
                else:
                    await bot.delete_message(
                        callback.message.chat.id, callback.message.message_id
                    )

                    await callback.message.answer_photo(
                        photo=f"{i[7]}",
                        caption=f"""⚡️ Kategoriya: {i[2]}
                                
💥 {i[3]}
                
ℹ️ Mahsulot haqida:
<i>{i[4]}</i>

🈁 Mahsulotdan {i[5]} ta qoldi

💰 Mahsulot narxi: {i[6]} so'm

💥 {t}x {t * i[6]} so'm""",
                        reply_markup=btn,
                    )

    elif key4 == "minus":
        if int(key3) == 1:
            await callback.answer("Bunday qila olmaysiz")
        else:
            t = int(key3) - 1
            btn = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text=f"➕ 1", callback_data=f"w**{key1}**{key2}**{t}**plus"
                        ),
                        InlineKeyboardButton(
                            text=f"➖ 1", callback_data=f"w**{key1}**{key2}**{t}**minus"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="🛒 Savatga qo'shish",
                            callback_data=f"qosh**{key1}**{t}",
                        )
                    ],
                ]
            )
            for i in r:
                if str(i[1]) == str(key1):
                    await bot.delete_message(
                        callback.message.chat.id, callback.message.message_id
                    )

                    await callback.message.answer_photo(
                        photo=f"{i[7]}",
                        caption=f"""⚡️ Kategoriya: {i[2]}
                                    
💥 {i[3]}
            
ℹ️ Mahsulot haqida:
<i>{i[4]}</i>

🈁 Mahsulotdan {i[5]} ta qoldi

💰 Mahsulot narxi: {i[6]} so'm

💥 {t}x {t * i[6]} so'm""",
                        reply_markup=btn,
                    )


@dp.callback_query(F.data.startswith("qosh**"))
async def qosh(callback: CallbackQuery):
    action = callback.data.split("**")
    key1 = action[1]
    key2 = action[2]
    r = select_info("maxsulotlar")
    for i in r:
        if str(i[1]) == f"{key1}":
            if (int(i[5]) == 0) == False:
                await bot.delete_message(
                    callback.message.chat.id, callback.message.message_id
                )

                add_savat(
                    callback.message.chat.id, i[1], i[2], i[3], i[4], key2, i[6], i[7]
                )
                update_data("maxsulotlar", "soni", "key", int(i[5]) - int(key2), i[1])
                await callback.message.answer(
                    text=f"""⚡️ {i[3]} savatga qo'shildi""", reply_markup=menu
                )

            else:
                await callback.answer(
                    "Mahsulot tugab qoldi, yangi qo'shilishini kuting", show_alert=True
                )


@dp.callback_query(F.data == "basket")
async def sett(callback: CallbackQuery):
    r = table_info("savat", "uid", callback.message.chat.id)
    print(r)
    s = ""
    y = 1
    if r == False:
        await callback.answer(text="Savatingiz bo'sh", show_alert=True)
    else:
        await bot.delete_message(callback.message.chat.id, callback.message.message_id)

        btn = InlineKeyboardBuilder()
        for i in r:
            if i[1] == callback.message.chat.id:
                btn.add(
                    InlineKeyboardButton(text=f"{y}", callback_data=f"shopx**{i[0]}")
                )
                s += f"{y}. {i[4]} - {i[6]} ta\n"
                y += 1
        btn.adjust(6)
        await callback.message.answer(
            text=f"""Savatingizdagi maxsulotlar:
            
{s}""",
            reply_markup=btn.as_markup(),
        )


@dp.callback_query(F.data.startswith("shopx**"))
async def shopx(callback: CallbackQuery):
    action = callback.data.split("**")[1]
    r = table_info("savat", "id", action)
    for i in r:
        if str(i[0]) == str(action):
            await bot.delete_message(
                callback.message.chat.id, callback.message.message_id
            )

            await callback.message.answer_photo(
                photo=str(i[8]),
                caption=f"""⚡️ Kategoriya: {i[3]}
                               
💥 Nomi: {i[4]}
                
ℹ️ Mahsulot haqida:
{i[5]}

🈁 Soni: {i[6]} ta

💰 Mahsulot narxi: {i[7]} so'm
💥 {i[6]} ta maxsulot umumiy narxi {int(i[6]) * int(i[7])} so'm""",
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(
                                text="🛍 Buyurtma berish",
                                callback_data=f"buyurtma**{action}",
                            ),
                            InlineKeyboardButton(
                                text="🗑 Savatdan olib tashlash",
                                callback_data=f"delsavat**{action}",
                            ),
                        ]
                    ]
                ),
            )


@dp.callback_query(F.data.startswith("delsavat**"))
async def delsavat(callback: CallbackQuery):
    action = callback.data.split("**")[1]
    # r = table_info("savat", "id", action)
    # m = select_info("maxsulotlar")
    # for i in r:
    #     if str(i[0]) == str(action):
    #         for j in m:
    #             if str(j[1]) == str(i[2]):
    #                 update_data("maxsulotlar", "key", "soni", str(i[2]), int(j[5]) + int(i[6]))
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer(
        text="🗑 Maxsulot savatdan muvaffaqiyatli olib tashlandi.", reply_markup=menu
    )
    delete_table("savat", "id", action)


@dp.callback_query(F.data.startswith("buyurtma**"))
async def buyurtma(callback: CallbackQuery):
    id = callback.data.split("**")[1]
    r = table_info("savat", "id", id)
    btn = InlineKeyboardBuilder()
    uzbekistan_regions = [
        "Andijon viloyati",
        "Buxoro viloyati",
        "Farg'ona viloyati",
        "Jizzax viloyati",
        "Xorazm viloyati",
        "Namangan viloyati",
        "Navoiy viloyati",
        "Qashqadaryo viloyati",
        "Qoraqalpog'iston Respublikasi",
        "Samarqand viloyati",
        "Sirdaryo viloyati",
        "Surxondaryo viloyati",
        "Toshkent viloyati",
        "Toshkent shahri",
    ]
    for i in r:
        if str(i[0]) == f"{id}":
            await bot.delete_message(
                callback.message.chat.id, callback.message.message_id
            )

            for t in uzbekistan_regions:
                btn.add(
                    InlineKeyboardButton(
                        text=f"{t}", callback_data=f"zakaz**{t}**{i[0]}"
                    )
                )
            btn.adjust(2)
            await callback.message.answer(
                text="Buyurtmani qaysi viloyatga yetkazamiz.",
                reply_markup=btn.as_markup(),
            )


@dp.callback_query(F.data.startswith("zakaz**"))
async def zakaz(callback: CallbackQuery):
    id = callback.data.split("**")[1]
    son = callback.data.split("**")[2]
    r = table_info("savat", "uid", f"{callback.message.chat.id}")
    rand = randint(111111111, 999999999)
    for i in r:
        if str(i[0]) == str(son):
            await bot.delete_message(
                callback.message.chat.id, callback.message.message_id
            )

            delete_table("savat", "id", str(son))
            add_buyurtma(
                callback.message.chat.id,
                i[2],
                i[3],
                i[4],
                i[5],
                son,
                i[7],
                i[8],
                rand,
                id,
                "Yetkazilmoqda",
            )
            await callback.message.answer(
                text=f"✅ Buyurtma muvaffaqiyatli rasmiylashtirildi, buyurtmani olish uchun maxsus kod {rand}\n\n👨‍💻 Buyurtma viloyatingizga yetib borsa sizga habar beramiz.",
                reply_markup=menu,
            )
            await bot.send_photo(
                photo=f"{i[8]}",
                chat_id=admin,
                caption=f"""✅ Yangi buyurtma keldi:
                
🤵/🤵‍♀️ Foydalanuvchi ma'lumotlari:
💥 Ismi: {callback.message.chat.full_name},
🆔 ID: {callback.message.chat.id}.

💥 Kategoriya: {i[3]}
➖ Nomi: {i[4]}

🛍 Soni: {i[6]}
💰 Narxi: {i[7]} so'm
💥 {i[6]} ta maxsulot umumiy narxi {int(i[6]) * int(i[7])} so'm

🔸 Buyurtma {id}ga yetkasilishi kerak
🕔 Buyurtma holati: Yetkazilmoqda
""",
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(
                                text="✅ Buyurtma yetkazildi",
                                callback_data=f"yetkazildi**{callback.message.chat.id}**{rand}",
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                text="🛑 Buyurtmani bekor qilish",
                                callback_data=f"bekor**{callback.message.chat.id}**{rand}",
                            )
                        ],
                    ]
                ),
            )


@dp.callback_query(F.data.startswith("bekor**"))
async def ketkazildi(callback: CallbackQuery):
    action = callback.data.split("**")
    id = action[1]
    code = action[2]
    r = table_info("buyurtma", "uid", str(id))
    for i in r:
        if str(i[9]) == str(code):
            update_data("buyurtma", "holat", "code", "Admin tomonidan bekor qilindi", str(code))
            await bot.delete_message(
                callback.message.chat.id, callback.message.message_id
            )
            await bot.send_message(
                chat_id=str(id),
                text=f"🛑  {code} raqamli buyurtmangiz adminstrator tomonidan bekor qilindi",
            )
            await bot.send_message(
                chat_id=str(admin),
                text=f"🛑 {code} raqamli buyurtma bekor qilindi"
            )
            
@dp.callback_query(F.data.startswith("yetkazildi**"))
async def ketkazildi(callback: CallbackQuery):
    action = callback.data.split("**")
    id = action[1]
    code = action[2]
    r = table_info("buyurtma", "uid", str(id))
    for i in r:
        if str(i[9]) == str(code):
            update_data("buyurtma", "holat", "code", "Yetkazilgan", str(code))
            await bot.delete_message(
                callback.message.chat.id, callback.message.message_id
            )
            await bot.send_message(
                chat_id=str(id),
                text=f"✅  {code} raqamli buyurtmangiz viloyatga yetib keldi.",
            )
            await bot.send_message(
                chat_id=str(admin),
                text=f"✅ {code} raqamli buyurtma yetkazilganligi haqidagi xabar buyurtma egasiga yuborildi"
            )
            



@dp.callback_query(F.data == "orders")
async def sett(callback: CallbackQuery):
    r = table_info("buyurtma", "uid", callback.message.chat.id)
    if r == False:
        await callback.answer(text="Sizda buyurtmalar yo'q", show_alert=True)
    else:
        await bot.delete_message(callback.message.chat.id, callback.message.message_id)

        btn = InlineKeyboardBuilder()
        for i in r:
            if i[1] == callback.message.chat.id:
                btn.add(
                    InlineKeyboardButton(
                        text=f"🆔 {i[9]}", callback_data=f"zakaz_info**{i[9]}"
                    )
                )
        btn.adjust(2)
        await callback.message.answer(
            text=f"""Sizdagi barcha buyurtmalar ro'yxati:""",
            reply_markup=btn.as_markup(),
        )


@dp.callback_query(F.data.startswith("zakaz_info**"))
async def akaz_info(callback: CallbackQuery):
    code = callback.data.split("**")[1]
    r = table_info("buyurtma", "uid", callback.message.chat.id)
    if r == False:
        await callback.message("Buyurtmalar yo'qga o'xshaydi")
    else:
        for i in r:
            if str(i[9]) == str(code):
                await bot.delete_message(
                    callback.message.chat.id, callback.message.message_id
                )

                await callback.message.answer_photo(
                    photo=f"{i[8]}",
                    caption=f"""⚡️ Kategoriya: {i[3]}
                               
💥 Nomi: {i[4]}
                
ℹ️ Mahsulot haqida:
{i[5]}

🈁 Soni: {i[6]} ta

💰 Mahsulot narxi: {i[7]} so'm
💥 {i[6]} ta maxsulot umumiy narxi {int(i[6]) * int(i[7])} so'm.

🛍 Buyurtma {i[10]}ga yetkaziladi,
🕔 Buyurtma holati: {i[11]}.""",
                    reply_markup=menu,
                )


#  ADMIN PANEL


@dp.message(Command("panel"))
async def ad_panel(message: Message):
    if str(message.from_user.id) == str(admin):
        await message.answer("<b>Admin panelga hush kelibsiz</b>", reply_markup=panel)


@dp.callback_query(F.data == "settings")
async def sett(callback: CallbackQuery):
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer(
        text="Maxsulot sozlamalari bo'limidasiz",
        reply_markup=setting,
    )


#  ADD MAHSULOT


@dp.callback_query(F.data == "ad_maxsulotlar")
async def sett(callback: CallbackQuery):
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer(
        text="Maxsulot sozlamalari bo'limidasiz", reply_markup=mlar
    )


@dp.callback_query(F.data == "add_maxsulot")
async def sett(callback: CallbackQuery, state: FSMContext):
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    r = select_info("kategoriya")
    btn = InlineKeyboardBuilder()
    for i in r:
        btn.add(InlineKeyboardButton(text=f"{i[1]}", callback_data=f"tanlas**{i[1]}"))
    btn.adjust(2)
    await callback.message.answer(
        text="Kategoriyalardan birini tanlang:",
        reply_markup=btn.as_markup(),
    )


@dp.callback_query(F.data.startswith("tanlas**"))
async def tanlas(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Yaxshi, endi maxsulot nomini yuboring")
    await state.set_state(add_maxsulot.nom)
    await state.update_data({"kateg": callback.data.split("**")[1]})


@dp.message(add_maxsulot.nom)
async def lkgj(message: Message, state: FSMContext):
    if user_("maxsulotlar", "nomi", f"{str(message.text)}") == False:
        await message.answer(text="Yaxshi, endi shu maxsulot haqida ma'lumot yuboring")
        await state.update_data({"nomi": message.text})
        await state.set_state(add_maxsulot.info)
    else:
        await message.answer(
            text="Bunday nomdagi maxsulot mavjud\n\nBoshqa nom kiriting"
        )
        await state.set_state(add_maxsulot.nom)


@dp.message(add_maxsulot.info)
async def lkgj(message: Message, state: FSMContext):
    await message.answer(text="Yaxshi, endi shu maxsulotning umumiy sonini kiriting.")
    await state.update_data({"info": message.text})
    await state.set_state(add_maxsulot.soni)


@dp.message(add_maxsulot.soni)
async def lkgj(message: Message, state: FSMContext):
    if str(message.text).isdigit() == True:
        await message.answer(text="Yaxshi, endi shu maxsulot narxini kiriting.")
        await state.update_data({"soni": message.text})
        await state.set_state(add_maxsulot.narxi)
    else:
        await message.answer(text="Faqat raqamlardan foydalaning\n\nQaytadan urining")
        await state.set_state(add_maxsulot.soni)


@dp.message(add_maxsulot.narxi)
async def lkgj(message: Message, state: FSMContext):
    if str(message.text).isdigit() == True:
        await message.answer(text="Yaxshi, endi shu maxsulot rasmini yuboring")
        await state.update_data({"narx": message.text})
        await state.set_state(add_maxsulot.rasm)
    else:
        await message.answer(text="Faqat raqamlardan foydalaning\n\nQaytadan urining")
        await state.set_state(add_maxsulot.narxi)


@dp.message(add_maxsulot.rasm)
async def lkgj(message: Message, state: FSMContext):
    if message.photo:
        id = message.photo[-1].file_id
        data = await state.get_data()
        rand = randint(111111111, 999999999)
        add_maxsulots(
            rand,
            data.get("kateg"),
            data.get("nomi"),
            data.get("info"),
            data.get("soni"),
            data.get("narx"),
            id,
        )
        await message.answer(text="Mahsulot bazaga yuklandi.")
        await state.clear()
    else:
        await message.answer(text="Faqat rasm qabul qilinadi\n\nQaytadan urining")
        await state.set_state(add_maxsulot.rasm)


# ADD CATEGORY


@dp.callback_query(F.data == "ad_categories")
async def sett(callback: CallbackQuery):
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer(
        text="Kategoriyalar sozlamalari bo'limidasiz", reply_markup=klar
    )


@dp.callback_query(F.data == "add_category")
async def sett(callback: CallbackQuery, state: FSMContext):
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer(
        text="Kategoriya nomini yuboring.",
    )
    await state.set_state(add_catego.nom)


@dp.message(add_catego.nom)
async def lkgj(message: Message, state: FSMContext):
    if user_("kategoriya", "nomi", f"{str(message.text)}") == False:
        add_categ(str(message.text))
        await message.answer(text="Kategoriya qo'shildi")
        await state.clear()
    else:
        await message.answer(text="Bunday kategoriya mavjud\n\nBoshqa nom kiriting")
        await state.set_state(add_catego.nom)


# END ADD CATEGORY


async def main() -> None:
    dp.message.middleware.register(ThrottlingMiddleware())
    dp.update.middleware.register(joinchat())
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except:
        print("Jarayon yakunlandi")
