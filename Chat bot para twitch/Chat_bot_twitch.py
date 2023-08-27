from twitchio.ext import commands
from googletrans import Translator

import time

#pip install googletrans==4.0.0-rc1
#pip install twitchio==1.2.3 


texto_del_seguidor = ""

bot = commands.Bot(
    irc_token = 'oauth:qix3u16to48seq4clrujhxi5tsabvd', #https://twitchapps.com/tmi/
    client_id = 'clh3ua91krbg8f254on5uh1fyfexhj',       #https://dev.twitch.tv/console/apps/create
    nick = 'nexusaod',  
    prefix = '!',
    initial_channels = ['nexusaod']

)



@bot.event
async def event_ready():
    print('Todo listo')


@bot.command(name='menui')
async def horario(ctx):
    await ctx.send(f'Para traducir de cualquier idioma a español es con el comando !es y para traducir de español u otro idioma a otro idioma utiliza !translate en (ingles), !translate en ja (japones), !translate es (español)')
    

@bot.command(name='es')
async def traducir(ctx):

    translator = Translator(service_urls=['translate.google.com.mx'])
       
    message = ctx.content.strip().lower()  # Obtener el contenido del mensaje en minúsculas
    global texto_del_seguidor
    texto_del_seguidor = message[3:]  # Almacenar el mensaje del seguidor (sin el comando)
    traduccion = translator.translate(texto_del_seguidor, dest='es')
    texto_traducido = traduccion.text.strip()
    await ctx.send(f"Mensaje de {ctx.author.name}: {texto_traducido}")
    time.sleep(2)

@bot.command(name='translate')
async def traducir(ctx):  
     
    translator = Translator(service_urls=['translate.google.com.mx'])

    message = ctx.content.strip().lower()
    global texto_del_seguidor
    lenguaje = ""
    texto_del_seguidor = message[13:]
    lenguaje = message[11:13]
    traduccion = translator.translate(texto_del_seguidor, dest=lenguaje)
    texto_traducido = traduccion.text.strip()
    await ctx.send(f"Mensaje de {ctx.author.name}: {texto_traducido}")
    time.sleep(2)

@bot.command(name='hola')
async def hola(ctx):
    await ctx.send(f'Bienvenido al canal!, en que puedo ayudarte?')

@bot.command(name='gracias')
async def agradecimiento(ctx):
    await ctx.send(f'De nada! cualquier cosa estoy aqui para responder dentro de mis capacidades')

@bot.command(name='horario')
async def hora(ctx):
    await ctx.send(f'Claro! el horario es de lunes a jueves de 6 a 9 de la noche')

@bot.command(name='que')
async def juegos(ctx):
    await ctx.send(f'No esta cerrado a ideas de que jugar, puedes preguntarle sin problema')


@bot.command(name='puedes')
async def suma(ctx):
    
    message = ctx.content.strip().lower()  # Obtener el contenido del mensaje en minúsculas
    global texto_del_seguidor
    sumar1 = message[14:15]  # Almacenar el mensaje del seguidor (sin el comando)
    sumar2 = message[18:19]  # Almacenar el mensaje del seguidor (sin el comando)
    respuesta = int(sumar1) + int(sumar2)



    await ctx.send(f'Claro! el resultado de la suma es: {respuesta}')


if __name__ == '__main__':
    bot.run()
