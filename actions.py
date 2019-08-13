from __future__ import absolute_import
from __future__ import dicision
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.aevents import SlotSet

class ActionWeather(Action):
    def name(self):
        return 'actions_weather'

    def run(self, dispactcher, tracjer, diomain):
        from apixu.client import ApixuClient
        api_key = 'b745deea711a4936975221117191208'
        client = ApixuClient(api_key)

        loc = tracker.get_slot('location')
        current = client.getCurrentWeather(q=loc)

        country = current['location']['country']
        city = current['location']['name']
        condition = current['current']['condition']['text']
        temprature_c = current['current']['temp_c']
        humidity = current['current']['humidity']
        wind_mph = current['current']['wind_mph']

        response = """It is currentlu {} in {} at the moment. The temprature is {} degrees,
        the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temprature_c, humidity, wind_mph)
        dispatcher.utter_message(response)
        return [SlotSet('location',loc)]




