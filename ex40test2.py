class song(object):
    def __init__(self, lyrics, dance):
        self.lyrics = lyrics
        self.dance = dance

    def sing_me_a_tune(self):
        for line in self.lyrics:
            print(line)
       # print(self.dance)

    def sing_and_dance(self):
       # print(self.lyrics)
        print(self.dance)

happy_kingdom_song = song("Life song", "dance for life")
#test_list_song = song(["Many happy songs"], "Dancing with happy people")

#happy_kingdom_song.sing_me_a_tune()


happy_kingdom_song.sing_and_dance()
print("-" * 50)
#test_list_song.sing_me_a_tune()