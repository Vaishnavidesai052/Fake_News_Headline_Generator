import random

subjects = [
    "NASA Scientist",
    "K-Pop Fanatic from Pune",
    "Local Cat Influencer",
    "Bored Software Engineer",
    "Rickshaw Driver with a PhD",
    "Grandma Who Raps",
    "Time Traveler from 2099",
    "Robot Built with Scrap",
    "Bollywood Stunt Double",
    "Schoolboy Hacker",
    "Lost Tourist from Mars",
    "Vlogger with Zero Followers"
]

actions = [
    "declares independence from WiFi",
    "launches flying vada pav startup",
    "dances non-stop for 42 hours",
    "hacks into a coffee machine",
    "proposes to AI assistant",
    "orders pizza using Morse code",
    "celebrates birthday with aliens",
    "writes open letter to mosquitoes",
    "starts protest against Mondays",
    "paints entire town yellow"
]

places_or_things = [
    "on Mars simulator in Ladakh",
    "at the entrance of Metro Station",
    "inside a giant samosa",
    "at Mumbai's sea-link during traffic jam",
    "inside a VR café",
    "on the rooftop of a moving train",
    "at a haunted warehouse",
    "in middle of online Zoom call",
    "during live cricket commentary",
    "underwater during scuba class"
]

while True:
    # Pick one random item from each list
    subject = random.choice(subjects)
    action  = random.choice(actions)
    place   = random.choice(places_or_things)

    # Use the *picked* words, not the lists
    headline = f"BREAKING NEWS: {subject} {action} {place}!"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input in ("no", "n"):
        print("\nThanks for using the Fake News Headline Generator. Have a nice day!")
        break
