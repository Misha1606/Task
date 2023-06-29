from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
class MainWidget(BoxLayout):
    summa_label= ObjectProperty()
    number_input_1=ObjectProperty()
    number_input_2=ObjectProperty()
    def sum_numbers(self):
        self.summa_label.text=str(int(self.number_input_1.text)+int(self.number_input_2.text))
class MainApp(App):
    def build(self):
        return MainWidget()
if __name__ == '__main__':
    app = MainApp()
    app.run()