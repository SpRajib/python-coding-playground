def are_you_playing_banjo(name):
    # Implement me!
    if name[0] in "Rr":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    
print(are_you_playing_banjo("Adam"))
print(are_you_playing_banjo("Randy"))