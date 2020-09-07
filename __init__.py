from mycroft import MycroftSkill, intent_file_handler


class DontCareBear(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('bear.care.dont.intent')
    def handle_bear_care_dont(self, message):
        self.speak_dialog('bear.care.dont')


def create_skill():
    return DontCareBear()

