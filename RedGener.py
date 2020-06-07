# Written by Darcy from RedAntsSec team ...
# Our email : RedAntsSec@gmail.com
# Follow us in Telegram/Github : @RedAntsSec

def user_input():
    banner = """\033[91m
 ____          _  ____                      
|  _ \ ___  __| |/ ___| ___ _ __   ___ _ __ 
| |_) / _ \/ _` | |  _ / _ \ '_ \ / _ \ '__|
|  _ <  __/ (_| | |_| |  __/ | | |  __/ |   
|_| \_\___|\__,_|\____|\___|_| |_|\___|_| 

Password list generator v1.1 ** Written by Darcy from @RedAntsSec (Github/Telegram)\n
"""
    print(banner)
    global words
    words = input("\033[92mEnter words (split them with (,) . Like: Darcy , john , redants): ")
    words = words.replace(" " , "")
    words = words.split(",")
    global char_yn
    global num_yn
    char_yn = input("Use characters ?(like !@#$% and ...) (Y/n): ")
    if char_yn == "y" or char_yn == "Y":
        char_yn = 1
    else:
        char_yn = 0
    num_yn = input("Use numbers in your passwords (Like 123)?(Y/n): ")
    if num_yn == "y" or num_yn == "Y":
        num_yn = 1
    else :
        num_yn = 0
def automatic1(words , char_yn , num_yn , characters):
    index=0
    global ans_index
    ans_index=[]
    words_len=len(words)
    while 1:
        if index != words_len:
            for i in words:
                if char_yn == 1 and num_yn == 1:
                    for b in characters:
                        ans_index.append(words[index] + b)
                        ans_index.append(words[index] + i + b)
                        ans_index.append(words[index] + b + i)
                        ans_index.append(b + words[index])
                        ans_index.append(b + i + words[index])
                        ans_index.append(i + b + words[index])
                        ans_index.append(b + words[index] + b)
                        ans_index.append(b + i + words[index] + b + i)
                        ans_index.append(i + b + words[index] + b + i)
                        ans_index.append(b + i + words[index] + i + b)
                        ans_index.append(b + i + words[index] + b + i)
                        # words[index] is for setting up all words together...
                    for n in range(101):
                        n = str(n)
                        ans_index.append(words[index] + n)
                        ans_index.append(n + words[index])
                        ans_index.append(n + words[index] + n)
                        ans_index.append(words[index] + n + i)
                        ans_index.append(words[index] + i + n)
                        ans_index.append(n + i + words[index])
                        ans_index.append(i + n + words[index])
                        ans_index.append(n + i + words[index] + n + i)
                        ans_index.append(i + n + words[index] + n + i)
                        ans_index.append(i + n + words[index] + i + n)
                        ans_index.append(n + i + words[index] + i + n)

                        for b in characters:
                            ans_index.append(words[index] + n + b)
                            ans_index.append(words[index] + i + n + b)
                            ans_index.append(words[index] + i + b + n)
                            ans_index.append(words[index] + b + i + n)
                            ans_index.append(words[index] + b + n + i)
                            ans_index.append(words[index] + n + i + b)
                            ans_index.append(words[index] + n + b + i)
                            ans_index.append(words[index] + b + n)
                            ans_index.append(n + b + words[index])
                            ans_index.append(i + n + b + words[index])
                            ans_index.append(i + b + n + words[index])
                            ans_index.append(n + i + b + words[index])
                            ans_index.append(n + b + i + words[index])
                            ans_index.append(b + n + i + words[index])
                            ans_index.append(b + i + n + words[index])
                            ans_index.append(b + n + words[index])
                if char_yn == 1 and num_yn == 0 :
                    for b in characters:
                        ans_index.append(words[index] + b)
                        ans_index.append(words[index] + i + b)
                        ans_index.append(words[index] + b + i)
                        ans_index.append(b + words[index])
                        ans_index.append(b + i + words[index])
                        ans_index.append(i + b + words[index])
                        ans_index.append(b + words[index] + b)
                        ans_index.append(b + i + words[index] + b + i)
                        ans_index.append(i + b + words[index] + b + i)
                        ans_index.append(b + i + words[index] + i + b)
                        ans_index.append(b + i + words[index] + b + i)
                if char_yn == 0 and num_yn == 1 :
                        for n in range(100):
                            n = str(n)
                            ans_index.append(words[index] + n)
                            ans_index.append(n + words[index])
                            ans_index.append(n + words[index] + n)
                            ans_index.append(words[index] + n + i)
                            ans_index.append(words[index] + i + n)
                            ans_index.append(n + i + words[index])
                            ans_index.append(i + n + words[index])
                            ans_index.append(n + i + words[index] + n + i)
                            ans_index.append(i + n + words[index] + n + i)
                            ans_index.append(i + n + words[index] + i + n)
                            ans_index.append(n + i + words[index] + i + n)
                    
                ans_index.append(words[index] + i)
                ans_index.append(i + words[index])
                ans_index.append(i + words[index] + i)
                ans_index.append(words[index] + i + i)
                ans_index.append(i + i + words[index])
                ans_index.append(i + i + words[index] + i + i)
            # ------------------------------------------------
            index = index + 1
        else:
             ans_correct = []
             for i in ans_index :
                 i = i + "\n"
                 ans_correct.append(i)
                 ans_index = ans_correct
             print("Passwords generated successfully.")
             break
def show_generated(passwords):
    print("Choose one of these for showing passwords: ")
    print ("1. Save passwords in a file.")
    print ("2. Show passwords here in terminal and save them in a file. ")
    print ("3. Just show the passwords here in terminal.")
    choose = int(input("1-3: "))
    if choose > 3 or choose < 1 :
        print("Wrong password !")
        show_generated(passwords)
    else :
        if choose == 1:
            file_addr = input("Enter the address of your file to save passwords in it: ")
            f = open(file_addr , "w")
            for i in ans_index:
                f.write(i)
            print("Good luck.")
            exit()
        if choose == 2:
            file_addr = input("Enter the address of your file to save passwords in it: ")
            f = open(file_addr , "w")
            for i in ans_index:
                print(i)
                f.write(i)
            print("Good luck.")
            exit()
        else:
            for i in ans_index:
                print(i)
            print("Good luck.")
            exit()
def main():
    user_input()
    characters = ['!' , '@' , '#' , '$' , '%' , '^' , '&' , '*' , '(' , ')']
    automatic1(words , char_yn , num_yn , characters)
    show_generated(ans_index)
main()
