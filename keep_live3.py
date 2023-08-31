import random

def guess_word():
    words = ["apple", "banana", "cherry", "durian", "elderberry", "fig", "grapefruit", "honeydew"]
    word = random.choice(words)
    guessed_letters = []
    tries = 6
    
    print("猜单词游戏 - 你有6次机会猜出单词的每个字母")
    print("单词的长度为", len(word), "个字母")
    
    while tries > 0:
        guessed_word = ""
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += "_"
        
        print("你猜的单词:", guessed_word)
        print("已猜过的字母:", guessed_letters)
        print("剩余猜测次数:", tries)
        
        guess = input("请输入你的猜测: ").lower()
        
        if guess in guessed_letters:
            print("你已经猜过这个字母了，请尝试其他字母。")
        elif len(guess) == 1 and guess.isalpha():
            guessed_letters.append(guess)
            if guess in word:
                print("恭喜，你猜对了一个字母！")
            else:
                print("猜错了，这个字母不在单词里。")
                tries -= 1
        else:
            print("无效的输入，请输入一个字母。")
        
        if "_" not in guessed_word:
            print("恭喜你，你猜对了整个单词！", "单词是", word)
            break
    
    if tries == 0:
        print("很遗憾，你没有猜对单词。单词是", word)

guess_word()
