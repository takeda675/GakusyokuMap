from maps.AbstractGakushoku import AbstractGakushoku

class OmuraOsusume(AbstractGakushoku):

    def get_menu(self):
        return "愛和食堂の日替わりランチ"

    def get_summary(self):
        return "メニューが日替わりで飽きない。"

    def get_author(self):
        return "大村"