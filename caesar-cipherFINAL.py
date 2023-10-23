

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser(cipher_text, shift_amount, cipher_direction):
    final_text=""
    shift_amount = shift_amount % 26
    if cipher_direction == "decode":
        shift_amount *= -1

    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            final_text += alphabet[new_position]
        else:
            final_text += char      
    print(f"This is your {cipher_direction}d text: {final_text}")

from art import logo
print(logo)


program_loop = True
while program_loop == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "exit": ##THIS IS A DEBUG TOOL TO LEAVE THE LOOP - I AM LAZY
        break ## Burn this mofo down
    if direction != "encode" and direction !="decode": ##Not on my watch, you get two inputs you greedy SOBS
        print("Please only enter encode or decode") #no uppercase either, I'll be real mad
        continue #I'llallowit.gif
    else:
        text = input("Type your message:\n").lower() ## input for cipher_text
        shift = int(input("Type the shift number:\n")) ## input for shift_amount 
  
    caeser(cipher_text=text, shift_amount=shift, cipher_direction=direction) #don't backstab plz

    program_continue = input("Would you like to run again? Type 'yes' or 'no':\n") #Would you like to know more?
    if program_continue == "no": # end it for shizzle
        program_loop = False #False, just like my hopes an dreams
        print("Thank you for using the program. Goodbye.") #

