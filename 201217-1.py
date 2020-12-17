


participant = ["leo","kiki","eden"]
completion = ["eden", "kiki"]

participant.sort()
completion.sort()

for i in participant:
    if i not in completion:
        print(i)
