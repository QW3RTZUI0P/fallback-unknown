from mycroft.skills.core import FallbackSkill
import random


class UnknownSkill(FallbackSkill):
    def __init__(self):
        super(UnknownSkill, self).__init__()

    def initialize(self):
        self.register_fallback(self.handle_fallback, 100)

    def read_voc_lines(self, name):
        with open(self.find_resource(name + '.voc', 'vocab')) as f:
            return filter(bool, map(str.strip, f.read().split('\n')))

    def handle_fallback(self, message):
        # through changing the frequency these numbers you can adjust the propability for the fallback sentences
        number = random.choice([0, 0, 1, 1, 1, 2, 3, 3])
        if number == 0:
            self.speak_dialog('insults')
        elif number == 1:
            self.speak_dialog('swear.words')
        elif number == 2:
            self.speak_dialog('tongue.twisters')
        elif number == 3:
            self.speak_dialog('sayings')

        return True


def create_skill():
    return UnknownSkill()
