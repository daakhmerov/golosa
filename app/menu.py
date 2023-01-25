class MenuEntry:
    def __init__(self, name, url):
        self.name = name
        self.url = url

menu = [
    MenuEntry('Главная', 'index'),
    MenuEntry('О проекте', 'about')
]