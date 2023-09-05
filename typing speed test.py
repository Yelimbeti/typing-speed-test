import time

def typing_speed_test(text):
    print("Type the following text:")
    print(text)
    input("Press Enter to start...")
    
    start_time = time.time()
    user_input = input("Start typing here: ")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    words = text.split()
    word_count = len(words)
    user_words = user_input.split()
    correct_words = 0

    for i in range(min(word_count, len(user_words))):
        if user_words[i] == words[i]:
            correct_words += 1

    accuracy = (correct_words / word_count) * 100
    words_per_minute = (correct_words / elapsed_time) * 60

    print(f"\nYour typing speed: {words_per_minute:.2f} words per minute")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    sample_text = "The quick brown fox jumps over the lazy dog"
    typing_speed_test(sample_text)
