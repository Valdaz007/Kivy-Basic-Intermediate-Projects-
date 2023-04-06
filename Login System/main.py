from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

class Login(StackLayout):
    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
        
        # Container
        self.orientation = "lr-tb"
        self.title = "Login System"
        self.spacing = 10
        Window.clearcolor = (0,0.5,1,0.5)
        
        # Head
        self._head = StackLayout()
        self._head.orientation = "lr-tb"
        self._head.size_hint = (1, .15)
        
        self._headLbl = Label(text='Login System', font_size=32)
        self._head.add_widget(self._headLbl)
        
        # Body
        self._body = StackLayout()
        self._body.orientation = "lr-tb"
        self._body.size_hint = (1, .75)
        self._body.spacing = 10
        self._body.padding = 10
        
        self.spaceWidget1 = StackLayout()
        self.spaceWidget1.orientation = "lr-tb"
        self.spaceWidget1.size_hint = (1, .1)
        
        self._bodyLblUname = Label(text='Username', font_size=18, size_hint=(.2, .15))
        self._bodyTxtIn_Uname = TextInput(size_hint=(.8, .1))
        self._bodyLblUpwd = Label(text='Password', font_size=18, size_hint=(.2, .1))
        self._bodyTxtIn_Upwd = TextInput(size_hint=(.8, .1))
        self._bodyBtnSubmit = Button(text='Submit', font_size=18, size_hint=(1, .15))
        
        self.spaceWidget2 = StackLayout()
        self.spaceWidget2.orientation = "lr-tb"
        self.spaceWidget2.size_hint = (1, .1)
        
        self._body.add_widget(self.spaceWidget1)
        self._body.add_widget(self._bodyLblUname)
        self._body.add_widget(self._bodyTxtIn_Uname)
        self._body.add_widget(self._bodyLblUpwd)
        self._body.add_widget(self._bodyTxtIn_Upwd)
        self._body.add_widget(self._bodyBtnSubmit)
        self._body.add_widget(self.spaceWidget2)
        
        # Footer
        self._footer = StackLayout()
        self._footer.orientation = "lr-tb"
        self._footer.size_hint = (1, .1)
        
        self._footerLbl = Label(text='Valdaz007')
        self._footer.add_widget(self._footerLbl)
        
        # Add Components to Container Layout
        self.add_widget(self._head)
        self.add_widget(self._body)
        self.add_widget(self._footer)

class MainApp(App):
    def build(self):
        return Login()

if __name__ == "__main__":
    MainApp().run()
