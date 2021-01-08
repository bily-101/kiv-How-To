from kivy.app import App  # <--- Controls the app
from kivy.lang import Builder  # <--- Builds the app
from kivy.uix.screenmanager import ScreenManager, Screen

# ^ Manages Widgets

Builder.load_file('design.kv')  # Contains kv file


class MainScreen(Screen):  # Main Screen
    pass  # We aren't doing any logic so we pass


class RootWidget(ScreenManager):  # Root widget
    pass


class MainApp(App):
    def build(self):  # Build's the file
        return RootWidget()  # Returns RootWidget


if __name__ == '__main__':
    MainApp().run()  # runs file
