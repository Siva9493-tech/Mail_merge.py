#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

PLACEHOLDER="[name]"

with open("Input/Names/invited_names.txt") as names_file:
    names=names_file.readlines()
with open("Input/Letters/starting_letter.txt") as makeup_letter:
    letter_content=makeup_letter.read()
    for name in names:
        stripped_name=name.strip()
        new_letter=letter_content.replace(PLACEHOLDER,stripped_name)
        with open(f"Output/ReadyToSend/letter_to_{stripped_name}.txt",mode="w") as completed_letter:
            completed_letter.write(new_letter)