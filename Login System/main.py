from kivy.app import App
from kivy.uix.stacklayout import StackLayout

class Login(StackLayout):
    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
        
        # Container
        self.orientation = "lr-tb"
        self.title = "Login System"
        self.spacing = 10
        Window.clearcolor = (0,0.5,1,0.5)

class MainApp(App):
    def build(self):
        return Login()

if __name__ == "__main__":
    MainApp().run()
