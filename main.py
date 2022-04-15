import Lexer_prog

while True:
    text=input('Текст: ')
    result = Lexer_prog.run(text)
    print(result)