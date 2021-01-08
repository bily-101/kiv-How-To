from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('design.kv')


class MainScreen(Screen):
    def next_page(self):
        self.manager.current = "final_page" # goes to second file

    def get_name(self, name):
        f = open("name.txt", "w") # Makes a new file
        f.write(name.text) # Writes the name into that file


class RootWidget(ScreenManager):
    pass


class FinalScreen(Screen):

    def show_name(self):
        f = open("name.txt") # opens the file

        self.ids.namee.text = f.read() # reads the file


class MainApp(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
