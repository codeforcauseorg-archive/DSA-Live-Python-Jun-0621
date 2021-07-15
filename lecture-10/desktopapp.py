from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

def hitAction(event):
    print("I am getting hit")

class AnotherLayout(GridLayout):


    def __init__(self):
        super(AnotherLayout, self).__init__()
        self.cols = 1
        self.add_widget(Button(text="inner 1"))
        self.add_widget(Button(text="inner 2"))
        self.add_widget(Button(text="inner 3"))


class BaseLayout(GridLayout):

    def __init__(self):
        super(BaseLayout, self).__init__()
        self.rows = 2
        b1 = Button(text="1")
        self.add_widget(b1)

        b1.bind(on_press=hitAction)

        self.add_widget(Button(text="2"))
        self.add_widget(Button(text="3"))
        self.add_widget(Button(text="4"))
        self.add_widget(Button(text="5"))
        self.add_widget(AnotherLayout())


class MyFirstKivyApp(App):

    def build(self):
        return BaseLayout()


app = MyFirstKivyApp()
app.run()
