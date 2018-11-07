from opencage.geocoder import OpenCageGeocode
from darksky import forecast
from discord.ext import commands
import discord
from discord import embeds, Color

deg = u'\u00b0'

with open('opencage_key.txt','r') as f: #add opencage token to opencage_key.txt
    cage_key = f.readline()
with open('darksky_key.txt','r') as f: #add opencage token to darksky_key.txt
    dark_key = f.readline()



class Weather:
    def __init__(self, client):
        self.client = client
        self.geocoder = OpenCageGeocode(key=cage_key)

    @commands.command(pass_context=True)
    async def weather(self, ctx, *, city):
        # Gives the current weather of the specified location
        if not city:
            raise commands.MissingRequiredArgument("Please add city.")

        g = self.geocoder.geocode(city)
        #print(g)
        if not g:
            raise commands.BadArgument("City not found")
        lat = g[0]['geometry']['lat']
        lng = g[0]['geometry']['lng']
        #radar_map = 'https://darksky.net/map-embed/@temperature,' + str(lat) + ',' + str(lng) + ',4.js?embed=true&timeControl=false&fieldControl=false&defaultField=temperature&defaultUnits=_f' dark sky does not have radar snapshots only embeds
        with forecast(dark_key, lat, lng) as myforecast:
            embed=discord.Embed(title=g[0]['formatted'], url='https://darksky.net/forecast/' + str(lat) +'/' + str(lng), description=myforecast.currently.summary + ' : ' + myforecast.daily.summary, color=0xfa14e9)#0x02adf7
            embed.set_thumbnail(url='https://darksky.net/images/darkskylogo.png')
            embed.add_field(name='Current Temperature:', value='{}F ({:.1f}C)'.format(myforecast.currently.temperature, (myforecast.currently.temperature - 32) * (5 / 9)), inline=True)
            embed.add_field(name='Feels Like:', value='{}F ({:.1f}C)'.format(myforecast.currently.apparentTemperature, (myforecast.currently.apparentTemperature - 32) * (5 / 9)), inline=True)
            embed.add_field(name='Chance of Precipitation:', value='{}%'.format(myforecast.currently.precipProbability * 100, inline=False))
            try:#try catch for precipType
                embed.add_field(name='Type of Precipitation:', value=myforecast.currently.precipType, inline=True)
            except:
                embed.add_field(name='Type of Precipitation:', value='N/A', inline=True)
            embed.add_field(name='Humidity:', value='{}%'.format(myforecast.currently.humidity * 100, inline=False))
            embed.add_field(name='Wind Speed:', value='{}mph'.format(myforecast.currently.windSpeed , inline=True))
            try:#try catch for alerts
                embed.add_field(name='Alerts:', value= myforecast.alerts[0].title , inline=False)
            except:
                embed.add_field(name='Alerts:', value= 'No alerts currently' , inline=False)
            #embed.set_image(url=radar_map)
            embed.set_footer(text='Powered by DarkSky: https://darksky.net/poweredby/')
        return await self.client.say(embed=embed)

    '''async def __error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await self.client.say(error)
        if isinstance(error, commands.BadArgument):
            await ctx.send(error)
        else:
            traceback.print_tb(error.original.__traceback__)
            print(error)'''

def setup(client):
    client.add_cog(Weather(client))
