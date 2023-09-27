from pyrogram import Client,filters

StrPy = Client("ChatGpt", api_id=15145595,api_hash="c3f60ecf742e136436acc9082ac8d9a4",bot_token="token") 

@StrPy.on_message(filters.command("start"))
async def _(StrPy,message):
 await StrPy.send_message(message.chat.id,"""
 مرحبًا! انا شات Gpt\nتمت برمجتي بواسطة @xx_YaBh\nهل تحتاج الى مساعدة ؟"""
 )
 
@StrPy.on_message(filters.reply&filters.private)
async def chatgptt(StrPy, message):
  
    from OpsAi import Ai
    gonb = Ai(query=message.text)
    await message.reply_text(gonb.chat()) 
    

@StrPy.on_message(filters.text)
async def textt(StrPy, message):
    	from OpsAi import Ai
    	gonb = Ai(query=message.text)
    	await message.reply_text(gonb.chat())
  
print("is run")
StrPy.run()
