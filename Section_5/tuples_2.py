# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company" "Bad Company", 1974         # append = shtoj; tupple doesn't have an append method
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Imelda May", 2011, ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"),
#                                              (4, "Kentish Town Waltz"))
#
# print(imelda)
# print()
#
# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)
# for song in tracks:
#     track, title = song
#     print(f"\tTrack number {track}, Title {title}, produced in {year} by {artist}.")

imelda = "More Mayhem", "Imelda May", 2011, ([(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"),
                                             (4, "Kentish Town Waltz")])        # we added [] and turned it into a list
# by changing it into a list we can use '.append' to add more contents in this album and not get an error
print(imelda)

imelda[3].append((5, "All For You"))

title, artist, year, tracks = imelda
tracks.append((6, "Eternity"))
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print(f"\tTrack number {track}, Title {title}, produced in {year} by {artist}.")
