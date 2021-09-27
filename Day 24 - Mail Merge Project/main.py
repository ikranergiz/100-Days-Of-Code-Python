# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("../../../Desktop/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    people = file.read()
    people = people.split("\n")
    print(people)

    with open(
            "../../../Desktop/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
        letter_contents = letter.read()

        for name in people:
            print(name)
            completed_letter = letter_contents.replace("[name]", name)

            with open(
                    f"../../../Desktop/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/{name}.txt",
                    "w") as a:
                a.write(completed_letter)
                #not replace dediğimizde ilk eleman name yerine yazılıyor fakat replace sonucu dönen stringi yine reletter
