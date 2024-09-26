import matplotlib.pyplot as plt
import requests
import string

book_url = 'http://www.gutenberg.org/files/2701/2701-0.txt'
book_response = requests.get(book_url)
book_text = book_response.text

letter_freq = {ch: 0 for ch in string.ascii_lowercase}

for char in book_text.lower():
    if char in letter_freq:
        letter_freq[char] += 1


total_count = sum(letter_freq.values())
letter_percentage = {letter: (count / total_count) * 100 for letter, count in letter_freq.items()}
alphabet = list(letter_percentage.keys())
percentages = list(letter_percentage.values())


plt.figure(figsize=(10, 6))
plt.xlabel('Letters')
plt.ylabel('Percentage (%)')
plt.bar(alphabet, percentages, color='pink')
plt.title('Letter Frequency Distribution in Moby-Dick')
plt.show()
