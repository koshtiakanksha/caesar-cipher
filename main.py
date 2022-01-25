import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(text, shift, direction,):
    result = ""
    if direction == "encode":
        for i in text:
            result += alphabet[(alphabet.index(i) + shift)%len(alphabet)]
        print(f"The encoded text is {result}")
    else:
        for i in text:
            result += alphabet[(alphabet.index(i) - shift)%26]
        print(f"The decoded text is {result}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    result = input(f"Type yes if you want to go again. Else type no\n").lower()
    if result == "no":
        should_continue = False
        print("Goodbye!")







