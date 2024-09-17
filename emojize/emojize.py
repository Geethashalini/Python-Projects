import emoji

text = input("Input: ")
find_emoji_name = text.find(":")

emoji_name = text[find_emoji_name:]
other_text = text[:find_emoji_name]

create_emoji = emoji.emojize(emoji_name, language = "alias")
print("Output: ", other_text + create_emoji)
