from collections import Counter

with open('q2.txt', 'r', encoding='utf-8') as file:
    words = file.read().split()

word_counts = Counter(words)

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write("Word, Freq\n")
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[0].lower())  # 단어를 대소문자 구분 없이 정렬
    for word, count in sorted_word_counts:
        file.write(f"{word},{count}\n")

total_words = sum(word_counts.values())
print(f"q2.txt 파일의 총 단어 수 = {total_words}개")
