from maps.AbstractGakushoku import AbstractGakushoku

class OmuraOsusume(AbstractGakushoku):

    def get_menu(self):
        return "愛和食堂の日替わりランチ"

    def get_summary(self):
        return "オススメのポイントやなぜオススメできるかなど、簡単に書きます"

    def get_author(self):
        return "書いた人の名前を書きます"