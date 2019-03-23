from mycroft import MycroftSkill, intent_file_handler


class Meowcroft(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('meowcroft.intent')
    def handle_meowcroft(self, message):
        self.speak_dialog('meowcroft')


def create_skill():
    return Meowcroft()

