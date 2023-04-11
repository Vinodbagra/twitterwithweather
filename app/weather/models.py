class Weather:
    def __init__(self, data):
        self.description = data.get('weather')[0].get('description')
        self.temp = data.get('main').get('temp')