from mycroft import MycroftSkill, intent_file_handler


class TestThomas(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('thomas.test.intent')
    def handle_thomas_test(self, message):
        self.speak_dialog('thomas.test')


def create_skill():
    return TestThomas()

