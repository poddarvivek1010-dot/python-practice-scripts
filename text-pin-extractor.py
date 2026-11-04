# Text PIN Extractor using loops & sequences


def find_secret_codes(text_list):
    all_codes = []

    # creating loop through the big text block in our list
    for text_block in text_list:
        secret_pin = ""
        lines = text_block.split("\n") # for spliting the text block into separate lines

        # creating loop through each line using its index position
        for line_num, single_line in enumerate(lines):
            words = single_line.split()

            # Making sure that the  line has enough words to match our index position
            if len(words) > line_num:
                target_word = words[line_num]
                secret_pin += str(len(target_word)) # for Counting the letters
            else:
                secret_pin += "0"

        all_codes.append(secret_pin)

    return all_codes


# messages which going to extract
message_1 = "I am learning loops and sequences now\nI learn about coding every single day\nJust a beginner now."
message_2 = "Coding is interesting but complex as well\nLoops help me to process text easily\nFunctions are very powerful in python."

my_test_list = [message_1, message_2]

results = find_secret_codes(my_test_list)
print(f"Running Code Extractor....\nThe overall result is: {results}")

print(f"Secret PIN for first text: {results[0]}")
print(f"Secret PIN for second text: {results[1]}")

