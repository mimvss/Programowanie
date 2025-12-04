# Survey questions
print("SURVEY")

# Ask questions and save answers as booleans
answer1 = input("Are you interested in computer science? (y/n): ").lower()
interested_cs = True if answer1 == 'y' else False

answer2 = input("Do you like playing computer games? (y/n): ").lower()
likes_games = True if answer2 == 'y' else False

answer3 = input("Do you have an Instagram account? (y/n): ").lower()
has_instagram = True if answer3 == 'y' else False

# Display results
print("\nSURVEY RESULTS")
print(f"Interested in computer science: {'Yes' if interested_cs else 'No'}")
print(f"Playing computer games: {'Yes' if likes_games else 'No'}")
print(f"Has an Instagram account: {'Yes' if has_instagram else 'No'}")
