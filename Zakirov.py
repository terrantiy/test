from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer



from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

class myApp(App):
    def build(self):

        s=Scatter()
        fl=FloatLayout(size=(300,300))
        f2=FloatLayout(size=(300,300))
        s.add_widget(fl)
        s.add_widget(f2)
        fl.add_widget(Button(
            text="У МЕНЯ БУДЕТ ДЕВУШКА?",
            font_size=20,
            on_press=self.btn_press,
            background_color=[3,0,7,11],
            background_normal='',
            size_hint=(.55, .25),
            pos=(320, 250)));
        f2.add_widget(Button(
            text="ДАЖЕ ЧЕРЕЗ 10 ЛЕТ?",
            font_size=20,
            on_press=self.btn_press,
            background_color=[2,4,0,33],
            background_normal='',
            size_hint=(.55, .25),
            pos=(320, 330)));
        return s
    def btn_press(self, instance):        
        instance.text='НИКОГДА В ЖИЗНИ'
        
if __name__=="__main__":
    myApp().run()
