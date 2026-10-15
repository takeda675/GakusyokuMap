from maps.AbstractGakushoku import AbstractGakushoku

class KamiokaOsusume(AbstractGakushoku):

    def get_menu(self):
        return "朝カレー"

    def get_summary(self):
        return "１００円だから"

    def get_author(self):
        return "上岡"