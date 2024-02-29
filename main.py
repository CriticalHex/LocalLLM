from os import system

tokens = int(input("Number of tokens to predict: "))
message_file = input("The filepath for the .txt file your input is in: ")

system(
    f"main.exe -m .\\models\\Mistral7Bv1\\Q5_K_S.gguf -f {message_file} -n {tokens} -c 0 -t 12 --multiline-input 1>response.txt"
)
