from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.audioservice import AudioService
from mycroft.util.log import getLogger

LOGGEr = getLogger(__name__)


class Meowcroft(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.audioservice = AudioService(self.bus)

    @intent_file_handler('meowcroft.intent')
    def handle_meowcroft(self, message):
        self.audioservice.play('file:///opt/mycroft/skills/meowcroft-skill.hotcakessanderson/catmeow1.mp3')
        self.audioservice.play('file:///opt/mycroft/skills/meowcroft-skill.hotcakessanderson/catmeow2.mp3')
        self.audioservice.play('file:///opt/mycroft/skills/meowcroft-skill.hotcakessanderson/catmeow3.mp3')
        self.audioservice.play('file:///opt/mycroft/skills/meowcroft-skill.hotcakessanderson/catmeow4.mp3')
        self.audioservice.play('file:///opt/mycroft/skills/meowcroft-skill.hotcakessanderson/catmeow5.mp3')
        self.audioservice.play('file:///opt/mycroft/skills/meowcroft-skill.hotcakessanderson/catmeow6.mp3')


def create_skill():
    return Meowcroft()
