from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture

import cv2

class CamApp(App):

    def build(self):
        self.img1=Image()
        layout = BoxLayout(orientation="vertical")
        self.da = Label(text='', size_hint=(1, 0.1))
        layout.add_widget(self.img1)
        layout.add_widget(self.da)
        self.capture = cv2.VideoCapture(0)
        self.decoder = cv2.QRCodeDetector()
        Clock.schedule_interval(self.update, 1.0/33.0)
        return layout

    def update(self, dt):
        ret, frame = self.capture.read()
        data, bbox, _ = self.decoder.detectAndDecode(frame)
        if data:
            self.da.text = data
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.img1.texture = texture1

if __name__ == '__main__':
    CamApp().run()
    cv2.destroyAllWindows()