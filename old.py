#-*-coding: UTF-8 -*-
import logging, config, sqlite3, aiohttp, json, socket, codecs, logging, asyncio, requests
from requests.structures import CaseInsensitiveDict
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, message, ChatActions, Update
from bs4 import BeautifulSoup
from aiogram import Bot, types 
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.utils.exceptions import Throttled
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import Dispatcher, FSMContext
from keyboards import replyKeyboards as navreply
from keyboards import inlineKeyboards as navinline
from aiohttp import ClientSession
from asyncio import new_event_loop, set_event_loop
import keep_alive
from datetime import datetime
import time
from pprint import pprint

start_time = datetime.now()

# -=-=-=-=-=-= Переменные бота -=-=-=-=-=-=
bot = Bot(token=config.TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot,storage=storage)

async def anti_flood3(*args, **kwargs):
    m = args[0]
    return



@dp.message_handler(lambda message: "/logger" in message.text)
async def logger(message: types.Message):
  nicknames = str(message.from_user.first_name)
  if nicknames in 'ㅤ': 
    await message.reply("❌ Извините! но я буду вас игнорить так как у вас пустой ник")
    return
  wyw = await message.answer("создаю логер...")
  time.sleep(2)
  await bot.edit_message_text(chat_id=message.chat.id, message_id=wyw.message_id,  text='failed to created', parse_mode='Markdown')

@dp.message_handler()
async def buttons(message: types.Message):
 nicknames = str(message.from_user.first_name)
 if nicknames in 'ㅤ': 
    await message.reply("❌ Извините! но я буду вас игнорить так как у вас пустой ник")
    return
 if '/cc' in message.text:
       ywwy1 = message.get_args()
       ywwy2 = ywwy1.replace(' ', '').replace('-', '').replace(',', '')
       bin = requests.get(f"https://lookup.binlist.net/{ywwy2}")
       bindata = bin.json()
       scheme = bindata['scheme']
       try:
         number = bindata['number']['length']
       except:
        number = ''
       try:
        lyna =  bindata['number']['luhn']
       except:
        lyna = '-'
       try:
        type =  bindata['type']
       except:
         type = '-'
       try:
         scheme =  bindata['scheme']
       except:
         scheme = '-'
       try:
         brand =  bindata['brand']
       except:
         brand = '-'
       try:
         prepaid = bindata['prepaid']
       except:
        prepaid = '-'
       try:
        country = bindata['country']['emoji']
       except:
        country = '-'
       try:
        name =  bindata['country']['name']
       except:
        name = '-'
       try:
        alpha2 = bindata['country']['alpha2']
       except:
        alpha2 = '-'
       try:
        currency = bindata['country']['currency']
       except:
        currency = '-'
       try:
        bank = bindata['bank']['name']
       except:
        bank = '-'
       try:
        url = bindata['bank']['url']
       except:
        url = '-'
       try:
        phone = bindata['bank']['phone']
       except:
         phone = '-'
       try:
        city = bindata['bank']['city']
       except:
        city = '-'
        await message.answer(f'💳 {ywwy2}\n├  Длина: `{number}`\n├  Алгоритм луна: `{lyna}`\n├  Тип: `{type}`\n├  Компания: `{scheme}`\n├  Бренд: `{brand}`\n└  Предоплата: `{prepaid}`\n\n`{country} {name} ({alpha2})`\n└  Валюта: `{currency}`\n\n🗾 {bank}\n├  Сайт: `{url}`\n├  Город: `{city}`\n└  Телефон: `{phone}`', parse_mode='Markdown')
        return
 if '#' in message.text:
        indataaa = message.text
        indata4 = indataaa.replace('#', '')
        user_id = str(message.from_user.id)
        fstep_msg111 = await message.reply('*🔎 На поиск требуется время, жди...*', parse_mode="Markdown")
        fstep_msg1141 = '🆔 ID: `'+indata4+'`'
        regdatebot =  InlineKeyboardButton('👀 regdatebot', url='https://t.me/regdatebot')
        gta = InlineKeyboardButton('🪐 Gta', url='https://t.me/gta_search_bot')
        TgAnalyst = InlineKeyboardButton('🤠 TgAnalyst', url='https://t.me/TgAnalyst_bot')
        variationsregdatebot = InlineKeyboardMarkup().add(regdatebot).add(gta).add(TgAnalyst)
        with open('checking.db', 'a') as file:
                    input = str(indata4)
                    user_id = str(message.from_user.id)
                    file.write(f'{input}\n')
        try:
         global check_tg
         check_tg = 0
         with open('checking.db') as file:
             for line in file:
              if indata4 in line:
                check_tg += 1
              else:
                pass
        except:
          intelest = ''
 #обява
        intelest = f'*👁 Интересовались*: `{str(check_tg)} раз`'
        await bot.edit_message_text(chat_id=message.chat.id, message_id=fstep_msg111.message_id,  text=''+fstep_msg1141+'\n\n'+intelest+'', parse_mode='Markdown', reply_markup=variationsregdatebot)
        try:
              martrix = requests.get(f"http://api.murix.ru/eye?uid={indata4}")
              data = martrix.json()
              try:
               uid = data['res']['uid']
              except:
                    pass
              try:
               try:
                name = data['res']['name']
               except:
                name = 'нет данных'
              except:
                    name = '-'
              try:
                phone = data['res']['phone']
              except:
                    phone = '-'
              try:
                nik = 'нет данных'
                nik = data['res']['nik']
              except:
                    nik = '-'
              try:
                fname = data['res']['fname']
              except:
                    fname = '-'
              ekhelkek = InlineKeyboardButton(f"🔎 {phone}", callback_data='log35ger25')
              regdatebot =  InlineKeyboardButton('👁 regdatebot', url='https://t.me/regdatebot')
              gta = InlineKeyboardButton('🪐 Gta', url='https://t.me/gta_search_bot')
              TgAnalyst = InlineKeyboardButton('🤠 TgAnalyst', url='https://t.me/TgAnalyst_bot')
              variationsregdatebot = InlineKeyboardMarkup().add(regdatebot).add(gta).add(TgAnalyst)
              if uid: wtwwtw = f'💬 В "Telegram":\n├📱 {phone}\n├👤 {name}\n└📧 @{nik}'
              await bot.edit_message_text(chat_id=message.chat.id, message_id=fstep_msg111.message_id,  text=''+fstep_msg1141+'\n\n'+wtwwtw+'\n\n'+intelest+'', parse_mode='Markdown', reply_markup=variationsregdatebot)
        except:
           try:
              ekhelkek = InlineKeyboardButton(f"🔎 {phone}", callback_data='log35ger25')
              regdatebot =  InlineKeyboardButton('👁 regdatebot', url='https://t.me/regdatebot')
              gta = InlineKeyboardButton('🪐 Gta', url='https://t.me/gta_search_bot')
              variationsregdatebot = InlineKeyboardMarkup().add(regdatebot).add(gta)
              await bot.edit_message_text(chat_id=message.chat.id, message_id=fstep_msg111.message_id,  text=''+fstep_msg1141+'\n\n'+wtwwtw+'\n\n'+intelest+'', parse_mode='Markdown', reply_markup=variationsregdatebot)
           except:
                 pass
           api = "https://vt45n5m4m9vtbn8t54n934.gimnwxyevw34.repl.co"

           async with ClientSession() as session:
              async with session.get(f"{api}/get_murix_uid_info?value={indata4}", headers={"key": "point1o1secretkey:00nd8n4nmd83fp0cnd"}) as response:
                pprint(await response.json(), indent=4)
                if response['DataFound'] == 'False':
                  pass
                else:
                  await message.answer(f'💬 Информация по базе данных Telegram 2020:\n├📱 {response["phone"]}\n├👤 {response["name"]}\n├🆔 {response["uid"]}\n└📧 @{response["nickname"]}')
           try:
              await message.reply('✅ Поиск завершён!', parse_mode='Markdown')
              try:
                 with open('EYEOFGOD.db', encoding='utf-8', errors='ignore') as file:
                     for line in file:
                         if indata4 in line: 
                          id = line
                          glasboga1 = f'{id}'
                          wgwehwh = glasboga1.split(';')[1]
                          await message.answer(f"📱 *Связанные телефоны* (1) :\n▪️ `{wgwehwh}`", parse_mode='Markdown')
                          return
              except:
               pass
           except:
                 pass
        return
 if 'x' in message.text: 
        try:
             rhash = requests.get(f'https://blockchain.info/rawaddr/{message.text}')
             data = rhash.json()
             n_tx = data['n_tx']
             total_sent = data['total_sent']
             total_received = data['total_received']
             final_balance = data['final_balance']
             gwewy = await message.reply("*🔎 На поиск требуется время, жди...*", parse_mode="Markdown")
             time.sleep(2)
             gta = InlineKeyboardButton('Blockchain', url=f'https://www.blockchain.com/ru/btc/address/{message.text}')
             regdatebot = InlineKeyboardButton('WhosWho', url=f'https://bitcoinwhoswho.com/address/{message.text}')
             ekhelkek = InlineKeyboardButton('intelx', url=f'https://intelx.io/?s={message.text}')
             ekhelkek1 = InlineKeyboardButton("🤑 Скачать транзакции и файл", callback_data='translakt')
             variationsregdatebot = InlineKeyboardMarkup().add(regdatebot).add(gta).add(ekhelkek)
             await gwewy.delete()
             await message.reply(f"💎 *Bitcoin адрес*:\n└ `{message.text}`\n\n🔄 *Всего транзакций*: `{n_tx}`\n📈 *Всего получено*: `{total_received} BTC`\n📉 *Всего отправлено*: `{total_sent} BTC`\n💵 *Итоговый баланс*: `{final_balance} BTC`", parse_mode="Markdown", reply_markup=variationsregdatebot)
        except:
              pass
 if '@' in message.text:
    fstep_msg = await message.reply('*🔎 На поиск требуется время, жди...*', parse_mode="Markdown")
    api = "https://vt45n5m4m9vtbn8t54n934.gimnwxyevw34.repl.co"

    async with aiohttp.ClientSession() as session:
      async with session.get(f"{api}/get_2gis_info?value={message.text}", headers={"key": "point1o1secretkey:00nd8n4nmd83fp0cnd"}) as response:
        response = await response.json()
        if response['DataFound'] == 'False':
          pass
        else:
          await message.answer('📗 *Информация по сервису 2ГИС*:\n└ 🏷 Статус существования: `есть`', parse_mode="Markdown")
    
    async with aiohttp.ClientSession() as session:
      async with session.get(f"{api}/get_gravatar_info?value={message.text}", headers={"key": "point1o1secretkey:00nd8n4nmd83fp0cnd"}) as response:
        response = await response.json()
        if response['DataFound'] == 'False':
          pass
        else:
          profile = response["profile"]
          await message.answer(f'🖼 <b>Информация по сервису Gravatar</b>:\n├ 🏷 Статус существования: <code>есть</code>\n└ 🔗 <a href="{profile}">Ссылка на профиль</a>', parse_mode=types.ParseMode.HTML)
    async with aiohttp.ClientSession() as session:
      async with session.get(f"{api}/get_icq_info?value={message.text}", headers={"key": "point1o1secretkey:00nd8n4nmd83fp0cnd"}) as response:
        response = await response.json()
        if response['DataFound'] == 'False':
          pass
        else:
          profile = response["profile"]
          avatar = response["avatar_url"]
          await message.answer(f'🦠 <b>Информация по сервису ICQ</b>:\n├ 🏷 Статус существования: <code>есть</code>\n├ 🖼 <a href="{avatar}">Ссылка на аватарку</a>\n└ 🔗 <a href="{profile}">Ссылка на профиль</a>', parse_mode=types.ParseMode.HTML)
    async with aiohttp.ClientSession() as session:
      async with session.get(f"{api}/get_snusbase_info?value={message.text}", headers={"key": "point1o1secretkey:00nd8n4nmd83fp0cnd"}) as response:
        response = await response.json()
        if response['DataFound'] == 'False':
          pass
        else:
          list_a = response["output"]["results"]
          numlist = len(list_a)
          passwords = ''
          for num in range(0,numlist):
            passwords_get = response["output"]["results"][num]['password']
            if num != 0:
              passwords += f', {passwords_get}'
            else:
              passwords += f'{passwords_get}'
          try:
            await message.answer(f'🗃 <b>Утечки паролей и логинов</b>:\n├ 📪 Почта: <code>{message.text}</code>\n└ 🔑 Пароли: {passwords}', parse_mode=types.ParseMode.HTML)
          except:
            await message.answer(f'🗃 <b>Утечки паролей и логинов</b>:\n├ 📪 Почта: <code>{message.text}</code>\n└ 🔑 Пароли: <code>приложены ниже в файле</code>', parse_mode=types.ParseMode.HTML)
            with open('passwords.txt', 'w') as file:
              file.write(passwords)
            await message.reply_document(open('passwords.txt', 'rb'))
    async with aiohttp.ClientSession() as session:
      async with session.get(f"{api}/get_facebook_info?value={message.text}", headers={"key": "point1o1secretkey:00nd8n4nmd83fp0cnd"}) as response:
        response = await response.json()
        if response['DataFound'] == 'False':
          pass
        else:
          await message.answer(f'📘 <b>Информация по сервису Facebook</b>:\n└ 🏷 Статус существования: <code>есть</code>', parse_mode=types.ParseMode.HTML)
    async with aiohttp.ClientSession() as session:
      async with session.get(f"{api}/get_ok_info?value={message.text}", headers={"key": "point1o1secretkey:00nd8n4nmd83fp0cnd"}) as response:
        response = await response.json()
        if response['DataFound'] == 'False':
          pass
        else:
          name = response['maskedName']
          info = response['profile_info']
          reg = response['profile_registered']
          await message.answer(f'📙 <b>Информация по сервису Facebook</b>:\n├ 👤 Фамилия и имя(из восстановления): <code>{name}</code>\n├ 📁 Информация: <code>{info}</code>\n└ ⏰ Дата регистрации: <code>{reg}</code>', parse_mode=types.ParseMode.HTML)
    async with aiohttp.ClientSession() as session:
      async with session.get(f"{api}/get_sber_info?value={message.text}", headers={"key": "point1o1secretkey:00nd8n4nmd83fp0cnd"}) as response:
        response = await response.json()
        if response['DataFound'] == 'False':
          pass
        else:
          masked_phone = response['maskedPhone']
          reg = response['creationData']
          await message.answer(f'💳 <b>Информация по сервису Facebook</b>:\n├ 📞 Часть номера телефона: <code>{masked_phone}</code>\n└ ⏰ Дата регистрации: <code>{reg}</code>', parse_mode=types.ParseMode.HTML)


 if '' in message.text:
     indata = message.text
     phonse = indata.replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
     lenz = len(phonse)
     if lenz <= 8: return
 try:
      phonse = int(phonse)
      ogogg = 0
 except:
      ogogg = 1
 if 'import' in indata:
      pass
 if ogogg == 0:
      phonse = indata.replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
      async with aiohttp.ClientSession() as session:
       async with session.get(
                        f"https://smsc.ru/sys/info.php?get_operator=1&login=drghjyuloytdrsa&psw=TJnv5uRAnePz3Kr&phone={phonse}"
                ) as response:
        response = await response.text()
        if response in "ERROR = 3 (operator not found)": return
        if response in "ERROR = 1 (parameters error)": return
        with open('alarm.db', encoding='utf-8', errors='ignore') as file:
              for line in file:
                  if phonse in line:
                    id = line.split(';')[0]
                    id1 = line.split(';')[1]
                    await bot.send_message(id, text=f"⚠️ Вас пытались пробить по номеру телефона! ({id1})", parse_mode='Markdown')
        with open('alarm.db', encoding='utf-8', errors='ignore') as file:
                     for line in file:
                       if phonse in line: return
        await message.reply("ура, это номер телефона, ну я тебя по-качто проигнорю")

@dp.callback_query_handler()
async def callback_worker(call):
    if call.data == "support":
      await bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = '🧰 *Техническая поддержка*: @cerbersupport', parse_mode="Markdown", reply_markup=nav.variations)
    if call.data == "stat":
      await bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = '*📈 Статистика*\n\n*🙂 Ваша статистика*:\nКоличество запросов: `0`\n\n*🤖 Статистика бота:*\nЛюдей: `0`\nКоличество запросов за все время: `0`\nСколько работает бот с: `'+str(start_time)+'`', parse_mode="Markdown", reply_markup=nav.variations)

if __name__ == '__main__':
  keep_alive.keep_alive()
  executor.start_polling(dp, skip_updates=True)