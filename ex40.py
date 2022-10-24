#Define a  class song with one argument object
class Song(object):
    #Define the __init__ self with another parameter, lyrics, dance
    def __init__(self, lyrics, dance):
        self.lyrics = lyrics
        self.dance = dance

    #Define sing_me_a_song for argument lyrics above
    #Inherits attributes from __init__ above namely ==> "Lyrics and dance"
    def sing_me_a_song(self):
        #Using for loop to print out each line/Item of the lyrics in self.lyrics
        for line in self.lyrics:
            print(line)
        print(self.dance)

    #Define sing_me_a_song for argument lyrics above
    #Inherits attributes from __init__ above namely ==> "Lyrics and dance"
    def sing_one_line_song(self):
        print(self.lyrics)
        print(self.dance)

#instantiate a class "song" to form ==> Object happy_bday
#by passing a list of strings as "lyrics"
happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"], "Dance the night away")

#instantiate the class "song" to form  oobject ==> bulls_on_parade
#by passing a list of strings as "lyrics"
bulls_on_parade = Song(["They rally arround tha family",
                        "With pockets of shells"], "Bulls break dancing to this on a reg")

#1. instantiate the class "song" to form  oobject ==> i_am_happy
#2. by passing a "list of strings" as "lyrics"
#3. Putting lyrics in a seperate variable
i_am_happy = Song(["Happy days are coming",
                    "I am happy"], "I will do the dougie dance")

lyrics1 = Song("Life is good, oh, always good", "hands up and jump kinda dance")

test_lyrics02 = Song(["life is a song"], "Danceee")



#passing lyrics from variable happy_bday to a class "sing_me_a_song" 
happy_bday.sing_me_a_song()
print("\n")
bulls_on_parade.sing_me_a_song()
print("\n")
i_am_happy.sing_me_a_song()
print("\n")
lyrics1.sing_one_line_song()
print("\n")
test_lyrics02.sing_one_line_song()
print("\n")
test_lyrics02.sing_me_a_song()
