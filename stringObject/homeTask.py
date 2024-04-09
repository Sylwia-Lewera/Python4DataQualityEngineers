import re

taskText = """
homEwork:
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""
def normalize_text(text):
    # Capitalize the first word of each sentence
    text = ':\n'.join(list(map(lambda x: x.strip().capitalize(), text.split(':'))))
    text = '.\n'.join(list(map(lambda x: x.strip().capitalize(), text.split('.'))))

    # Correct 'iZ' to 'is'
    text = re.sub(r'\biZ\b', 'is', text)
    text = re.sub(r'\biz\b', 'is', text)
    text = re.sub(r'\biZ\b', 'is', text)

    # Calculate the number of whitespace characters
    whitespace_count = len(re.findall(r'\s', text))
    whitespace_count += len(re.findall(r'\n', text))

    # Add a sentence with last words of each existing sentence
    sentences = re.split(r'(?<=\.)\s*', text)
    last_words = ' '.join(sentence.split()[-1] for sentence in sentences if sentence.strip())
    text += f" {last_words}."

    return text, whitespace_count

normalized_text, whitespace_count = normalize_text(taskText)

# Print the normalized text and whitespace count
print("Normalized Text:")
print(normalized_text)
print("\nNumber of whitespace characters:", whitespace_count)