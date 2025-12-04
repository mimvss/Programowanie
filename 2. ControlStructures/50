# Correct PIN
correct_pin = "0805"

# Give user 3 attempts
for attempt in range(1, 4):
    entered_pin = input("Enter the PIN code: ")
    if entered_pin == correct_pin:
        print("PIN correct. Access granted.")
        break  # przerywa pętlę, jeśli PIN jest poprawny
    else:
        print("Incorrect...")
else:
    # ten else jest wywoływany jeśli pętla zakończy się bez break
    print("Sorry, your payment card has been blocked.")
