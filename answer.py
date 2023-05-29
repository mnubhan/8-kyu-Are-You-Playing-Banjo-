def are_you_playing_banjo(name):
    if name[0].upper()=="R":
        return f'{name} plays banjo'
    else:
        return f'{name} does not play banjo'
      
      
def areYouPlayingBanjo(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo";
