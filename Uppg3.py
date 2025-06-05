import re

file = "textfile.txt"
text = open(file)

word_list = re.findall("[a-zA-ZåäöÅÄÖ\']+", text.read())
count_word = {}  # En tom ordlista

for word in word_list:
    word = word.lower()  # Gör att alla ord är samma oberoende av storlek
    if word in count_word:
        count_word[word] += 1
    else:
        count_word[word] = 1

# Count_word.items gör en lista med tuplar
# tuple (x) som indata och returnerar det andra elementet i tupeln, antalet förekomster (x[1])
words_sorted_by_count = list(sorted(count_word.items(), key=lambda x: x[1], reverse=True))

n = int(input("Hur många av de vanligaste orden vill du se? "))
m = int(input("Hur många av de ovanligaste orden vill du se? "))


print("Totalt antal ord: ", len(word_list))
print("Antalet unika ord: ", len(count_word))

print(f"\nDe {n} vanligaste orden: ")
for i, (word, count) in enumerate(words_sorted_by_count[:n], 1):
    print(f"{i}. {word:<10} ({count})")  

print(f"\n{m} av de ovanligaste orden: ")
for j, (word, count) in enumerate (words_sorted_by_count[-m:], 1):
    print(f"{j}. {word:<10} ({count})")
