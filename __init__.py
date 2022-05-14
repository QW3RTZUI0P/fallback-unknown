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
        boolean = random.choice([True, False, False])
        if boolean:
            self.speak_dialog('insults')
        else:
            self.speak_dialog('swear_words')

        return True


def create_skill():
    return UnknownSkill()
