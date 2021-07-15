from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import cv2


class BaseLayout(GridLayout):

    def get_frame(self, event):
        ret, frame = self.capture.read()
        frame = frame[::-1]
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt="rgb")
        data = frame.tostring()
        texture.blit_buffer(data, bufferfmt="ubyte", colorfmt="rgb")
        self.image.texture = texture

    def __init__(self):
        super(BaseLayout, self).__init__()
        self.rows = 2
        self.capture = cv2.VideoCapture(0)
        self.image = Image()
        self.add_widget(self.image)
        self.add_widget(Button(text="3"))
        Clock.schedule_interval(self.get_frame, 1/30)


class MyFirstKivyApp(App):

    def build(self):
        return BaseLayout()


app = MyFirstKivyApp()
app.run()
