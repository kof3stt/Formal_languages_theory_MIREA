def Lexical():
    def gc():
        nonlocal total, line_number, on_line_number, letter
        if total < len(data) - 1:
            if data[total] == '\n':
                line_number += 1
                on_line_number = 1
            else:
                on_line_number += 1
            total += 1
            letter = data[total]
            return True
        else:
            return False
    flag, FLAG_READ_FILE = False, True
    Lex_result = list()
    buffer = str()
    status = 'H'
    total, line_number, on_line_number = 0, 1, 1
    key_words = ("not", "or", "and", "dim", "integer", "real", "boolean", "while",
                 "as", "if", "else", "then", "for", "to", "do", "read", "write", "true", "false")
    separators = ('{', '}', '<>', '=', '<', '>', '<=', '[', ']', ':', '/*', '*/'
                  '>=', '+', '-', '*', '/', ',', ';', '(', ')')
    define_dict = {"not": "NOT", "or": "OR", "and": "AND", "dim": "DIM", "integer": "INTEGER", "real": "REAL", "boolean": "BOOLEAN", "while": "WHILE",
                   "as": "ASSIGN", "if": "IF", "else": "ELSE", "then": "THEN", "for": "FOR", "to": "TO", "do": "DO", "read": "READ", "write": "WRITE",
                   "true": "TRUE", "false": "FALSE", "{": "BEGIN_PROG", "}": "END_PROG", "<>": "NEQ", "=": "EQUAL", "<": "LESS", ">": "GREATER",
                   "<=": "LEQ", ">=": "GEQ", "[": "BEGIN_COMPLEX", "]": "END_COMPLEX", ":": "COLON", "+": "PLUS", "-": "MINUS", "*": "MULT",
                   "/": "DIVIDE", ",": "COMMA", ";": "SEMICOLON", "(": "LEFT_PAREN", ")": "RIGHT_PAREN"}
    # ID, KEYWORD, TYPE, LINE_BREAK, BEGIN_COMMENT,END_COMMENT, ERR,TYPE_I, TYPE_F, TYPE_B, EMPTY
    data = file.read()
    while True:
        letter = data[total]
        match status:
            case 'H':
                while letter in (' ', '\n', '\t') and FLAG_READ_FILE:
                    if letter == '\n' and flag:
                        Lex_result.append({"Тип лексемы": "LINE_BREAK", "Значение": "LINE_BREAK",
                                           "Номер строки": line_number, "Позиция в строке": on_line_number})
                    FLAG_READ_FILE = gc()
                if not FLAG_READ_FILE:
                    return Lex_result
                if letter.isalpha():
                    buffer = letter
                    FLAG_READ_FILE = gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'ID'
                elif letter in ('0', '1'):
                    buffer = letter
                    FLAG_READ_FILE = gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = "BINARY NUMBER"
                elif letter in map(str, list(range(2, 8))):
                    buffer = letter
                    FLAG_READ_FILE = gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = "OCTAL NUMBER"
                elif letter in ('8', '9'):
                    status = 'DECIMAL NUMBER'
                    buffer = letter
                    FLAG_READ_FILE = gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                elif letter == '.':
                    buffer = letter
                    FLAG_READ_FILE = gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'P1'
                elif letter == '/':
                    buffer = letter
                    FLAG_READ_FILE = gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'C1'
                elif letter == '<':
                    buffer = letter
                    FLAG_READ_FILE = gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'M1'
                elif letter == '>':
                    buffer = letter
                    FLAG_READ_FILE = gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'M2'
                elif letter == '}':
                    buffer = letter
                    Lex_result.append({"Тип лексемы": define_dict[buffer], "Значение": buffer,
                                      "Номер строки": line_number, "Позиция в строке": on_line_number})
                    FLAG_READ_FILE = gc()
                else:
                    status = 'SEPARATOR'
            case 'ID':
                while letter.isalnum():
                    buffer += letter
                    FLAG_READ_FILE = gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                if buffer in key_words:
                    Lex_result.append({"Тип лексемы": define_dict[buffer], "Значение": buffer,
                                      "Номер строки": line_number, "Позиция в строке": on_line_number-len(buffer)})
                else:
                    Lex_result.append({"Тип лексемы": "ID", "Значение": buffer,
                                      "Номер строки": line_number, "Позиция в строке": on_line_number-len(buffer)})
                status = 'H'
            case 'BINARY NUMBER':
                while letter in ('0', '1'):
                    buffer += letter
                    FLAG_READ_FILE = gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                if letter in map(str, list(range(2, 8))):
                    status = 'OCTAL NUMBER'
                elif letter in ('8', '9'):
                    status = 'DECIMAL NUMBER'
                elif letter in ('a', 'c', 'f', 'A', 'C', 'F'):
                    status = 'HEX NUMBER'
                elif letter in ('e', 'E'):
                    buffer += letter
                    FLAG_READ_FILE = gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'E11'
                elif letter in ('d', 'D'):
                    buffer += letter
                    FLAG_READ_FILE = gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'D'
                elif letter in ('o', 'O'):
                    buffer += letter
                    FLAG_READ_FILE = gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'O'
                elif letter in ('H', 'h'):
                    buffer += letter
                    FLAG_READ_FILE = gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'HX'
                elif letter == '.':
                    buffer += letter
                    FLAG_READ_FILE = gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'P1'
                elif letter in ('b', 'B'):
                    buffer += letter
                    FLAG_READ_FILE = gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'B'
                elif letter.isalpha():
                    status = 'ERROR'
                else:
                    status = 'DECIMAL NUMBER'
            case 'OCTAL NUMBER':
                while letter in map(str, list(range(0, 8))):
                    buffer += letter
                    FLAG_READ_FILE = gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                if letter in ('8', '9'):
                    status = 'DECIMAL NUMBER'
                elif letter in ('a', 'c', 'b', 'f', 'A', 'B', 'C', 'F'):
                    status = 'HEX NUMBER'
                elif letter in ('e', 'E'):
                    buffer += letter
                    FLAG_READ_FILE = gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'E11'
                elif letter in ('d', 'D'):
                    buffer += letter
                    FLAG_READ_FILE = gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'D'
                elif letter in ('H', 'h'):
                    buffer += letter
                    FLAG_READ_FILE = gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'HX'
                elif letter == '.':
                    buffer += letter
                    FLAG_READ_FILE = gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'P1'
                elif letter in ('o', 'O'):
                    buffer += letter
                    FLAG_READ_FILE = gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'O'
                elif letter.isalpha():
                    status = 'ERROR'
                else:
                    status = 'DECIMAL NUMBER'
            case 'DECIMAL NUMBER':
                while letter in map(str, list(range(0, 10))):
                    buffer += letter
                    FLAG_READ_FILE = gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                if letter in ('a', 'b', 'c', 'f', 'A', 'B', 'C', 'F'):
                    status = 'HEX NUMBER'
                elif letter in ('e', 'E'):
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'E11'
                elif letter in ('h', 'H'):
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'HX'
                elif letter == '.':
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'P1'
                elif letter in ('d', 'D'):
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'D'
                elif letter.isalpha():
                    status = 'ERROR'
                else:
                    Lex_result.append({"Тип лексемы": "десятичное число", "Значение": buffer,
                                      "Номер строки": line_number, "Позиция в строке": on_line_number-len(buffer)})
                    status = 'H'
            case 'HEX NUMBER':
                while letter.isdigit() or letter in ('a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F'):
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                if letter in ('h', 'H'):
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'HX'
                else:
                    status = 'ERROR'
            case 'B':
                if letter.isdigit() or letter in ('a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F'):
                    status = 'HEX NUMBER'
                elif letter in ('h', 'H'):
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'HX'
                elif letter.isalpha():
                    status = 'ERROR'
                else:
                    Lex_result.append({"Тип лексемы": "число в двоичной системе", "Значение": buffer,
                                      "Номер строки": line_number, "Позиция в строке": on_line_number-len(buffer)})
                    status = 'H'
            case 'O':
                if letter.isalnum():
                    status = 'ERROR'
                else:
                    Lex_result.append({"Тип лексемы": "число в восьмеричной системе", "Значение": buffer,
                                      "Номер строки": line_number, "Позиция в строке": on_line_number-len(buffer)})
                    status = 'H'
            case 'D':
                if letter in ('h', 'H'):
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'HX'
                elif letter.isdigit() or letter in ('a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F'):
                    status = 'HEX NUMBER'
                elif letter.isdigit():
                    status = 'ERROR'
                else:
                    Lex_result.append({"Тип лексемы": "десятичное число", "Значение": buffer,
                                      "Номер строки": line_number, "Позиция в строке": on_line_number-len(buffer)})
                    status = 'H'
            case 'HX':
                if letter.isalnum():
                    status = 'ERROR'
                else:
                    Lex_result.append({"Тип лексемы": "число в шестнадцатеричной системе", "Значение": buffer,
                                      "Номер строки": line_number, "Позиция в строке": on_line_number-len(buffer)})
                    status = 'H'
            case 'E11':
                if letter.isdigit():
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'E12'
                elif letter in ('+', '-'):
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'ZN'
                elif letter in ('h', 'H'):
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'HX'
                elif letter.isdigit() or letter in ('a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F'):
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'HEX NUMBER'
                else:
                    status = 'ERROR'
            case 'ZN':
                if letter.isdigit():
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'E13'
                else:
                    status = 'ERROR'
            case 'E12':
                while letter.isdigit():
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                if letter.isdigit() or letter in ('a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F'):
                    status = 'HEX NUMBER'
                elif letter in ('h', 'H'):
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'HX'
                elif letter.isalpha():
                    status = 'ERROR'
                else:
                    Lex_result.append({"Тип лексемы": "действительное число", "Значение": buffer,
                                      "Номер строки": line_number, "Позиция в строке": on_line_number-len(buffer)})
                    status = 'H'
            case 'E13':
                while letter.isdigit():
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                if letter.isalpha() or letter == '.':
                    status = 'ERROR'
                else:
                    Lex_result.append({"Тип лексемы": "действительное число", "Значение": buffer,
                                      "Номер строки": line_number, "Позиция в строке": on_line_number-len(buffer)})
                    status = 'H'
            case 'P1':
                if letter.isdigit():
                    status = 'P2'
                else:
                    status = 'ERROR'
            case 'P2':
                while letter.isdigit():
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                if letter in ('e', 'E'):
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'E21'
                elif letter.isalpha() or letter == '.':
                    status = 'ERROR'
                else:
                    Lex_result.append({"Тип лексемы": "действительное число", "Значение": buffer,
                                      "Номер строки": line_number, "Позиция в строке": on_line_number-len(buffer)})
                    status = 'H'
            case 'E21':
                if letter in ('+', '-'):
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'ZN'
                elif letter.isdigit():
                    status = 'E22'
                else:
                    status = 'ERROR'
            case 'E22':
                while letter.isdigit():
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                if (letter.isalpha() or letter == '.'):
                    status = 'ERROR'
                else:
                    Lex_result.append({"Тип лексемы": "действительное число", "Значение": buffer,
                                      "Номер строки": line_number, "Позиция в строке": on_line_number-len(buffer)})
                    status = 'H'
            case 'C1':
                if letter == '*':
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'C2'
                else:
                    Lex_result.append({"Тип лексемы": define_dict[buffer], "Значение": buffer,
                                      "Номер строки": line_number, "Позиция в строке": on_line_number-len(buffer)})
                    status = 'H'
            case 'C2':
                while total != len(data) and letter != '*':
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                buffer = ''
                buffer += letter
                gc()
                if not FLAG_READ_FILE:
                    return Lex_result
                status = 'C3'
            case 'C3':
                if letter == '/':
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    status = 'H'
                else:
                    status = 'C2'
            case 'M1':
                if letter == '>':
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    Lex_result.append({"Тип лексемы": define_dict[buffer], "Значение": buffer,
                                      "Номер строки": line_number, "Позиция в строке": on_line_number-len(buffer)})
                    status = 'H'
                elif letter == '=':
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    Lex_result.append({"Тип лексемы": define_dict[buffer], "Значение": buffer,
                                      "Номер строки": line_number, "Позиция в строке": on_line_number-len(buffer)})
                    status = 'H'
                else:
                    Lex_result.append({"Тип лексемы": define_dict[buffer], "Значение": buffer,
                                      "Номер строки": line_number, "Позиция в строке": on_line_number-len(buffer)})
                    status = 'H'
            case 'M2':
                if letter == '>':
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    Lex_result.append({"Тип лексемы": define_dict[buffer], "Значение": buffer,
                                      "Номер строки": line_number, "Позиция в строке": on_line_number-len(buffer)})
                    status = 'H'
                elif letter == '=':
                    buffer += letter
                    gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    Lex_result.append({"Тип лексемы": define_dict[buffer], "Значение": buffer,
                                      "Номер строки": line_number, "Позиция в строке": on_line_number-len(buffer)})
                    status = 'H'
                else:
                    Lex_result.append({"Тип лексемы": define_dict[buffer], "Значение": buffer,
                                      "Номер строки": line_number, "Позиция в строке": on_line_number-len(buffer)})
                    status = 'H'
            case 'SEPARATOR':
                buffer = letter
                if buffer in separators:
                    FLAG_READ_FILE = gc()
                    if not FLAG_READ_FILE:
                        return Lex_result
                    if buffer == '[':
                        flag = True
                    elif buffer == ']':
                        flag = False
                    Lex_result.append({"Тип лексемы": define_dict[buffer], "Значение": buffer,
                                      "Номер строки": line_number, "Позиция в строке": on_line_number-len(buffer)})
                    status = 'H'
                else:
                    status = 'ERROR'
            case 'ERROR':
                while FLAG_READ_FILE and letter not in (' ', '\n', '\t') and letter not in separators:
                    buffer += letter
                    gc()
                if not FLAG_READ_FILE:
                    return Lex_result
                Lex_result.append({"Тип лексемы": "ERR", "Значение": buffer,
                                   "Номер строки": line_number, "Позиция в строке": on_line_number-len(buffer)})
                status = 'H'


def Syntactic():

    def GL():
        nonlocal total, prev_lex, current_lex
        if total < len(data):
            prev_lex = current_lex
            current_lex = data[total]
            total += 1
            return True
        else:
            print(
                "========== Сборка: успешно: 1, сбой: 0, в актуальном состоянии: 0, пропущено: 0==========")
            exit(0)

    def EXPRESSION_SEQUENCE():
        GL()
        EXPRESSION()
        while current_lex['Тип лексемы'] == 'COMMA':
            GL()
            EXPRESSION()

    def ID_SEQUENCE():
        if current_lex['Тип лексемы'] == 'ID':
            GL()
            while current_lex['Тип лексемы'] == 'COMMA':
                GL()
                if current_lex['Тип лексемы'] == 'ID':
                    GL()
                else:
                    ERROR_HANDLER(5)
        else:
            ERROR_HANDLER(6)

    def ERROR_HANDLER(n: int):
        match n:
            case 1:
                print("Отсутсвует символ }")
            case 2:
                print("Отсутствует символ {")
            case 3:
                print("Требуется оператор или описание переменной")
            case 4:
                print("Ожидалась точка с запятой")
            case 5:
                print("Ошибка в последовательности идентификаторов")
            case 6:
                print("Требуется идентификатор")
            case 7:
                print("Отсутствует символ )")
            case 8:
                print("Требуется тип переменной")
            case 9:
                print("Отсутствует оператор then")
            case 10:
                print("Отсутствует оператор do")
            case 11:
                print("Отсутствует оператор do")
            case 12:
                print("Отсутствует оператор to")
            case 13:
                print("Отсутствует символ )")
            case 14:
                print("Отсутствует символ (")
            case 15:
                print("Отсутсвует символ )")
            case 16:
                print("Отсутствует символ (")
            case 17:
                print("Отсутствует символ ]")
            case 18:
                print("Ошибка в выражении")
            case 19:
                pass
            case 20:
                print("Неизвестный оператор")
            case 21:
                print("Требовался идентификатор")
        print(
            f"line {current_lex['Номер строки']}, position {current_lex['Позиция в строке']}")
        exit(n)

    def DESCRIPTION():
        if current_lex['Тип лексемы'] == "DIM":
            GL()
            ID_SEQUENCE()
            if current_lex['Тип лексемы'] not in ('INTEGER', 'REAL', 'BOOLEAN'):
                ERROR_HANDLER(8)

    def OPERATOR():
        match current_lex['Тип лексемы']:
            case "IF":
                GL()
                CONDITION_OPERATOR()
            case 'WHILE':
                GL()
                WHILE_OPERATOR()
            case "FOR":
                GL()
                FOR_OPERATOR()
            case "READ":
                GL()
                READ_OPERATOR()
            case "WRITE":
                GL()
                WRITE_OPERATOR()
            case "ID":
                GL()
                ASSIGN_OPERATOR()
            case "BEGIN_COMPLEX":
                GL()
                COMPLEX_OPERATOR()
            case _:
                ERROR_HANDLER(20)

    def EXPRESSION():
        OPERAND()
        if current_lex['Тип лексемы'] in ('EQUAL', 'LESS', 'GREATER', 'LEQ', 'GEQ', 'NEQ'):
            GL()
            EXPRESSION()

    def OPERAND():
        SUMMAND()
        if current_lex['Тип лексемы'] in ('PLUS', 'MINUS', 'OR'):
            GL()
            OPERAND()

    def SUMMAND():
        MULTIPLIER()
        if current_lex['Тип лексемы'] in ('DIVIDE', 'MULT', 'AND'):
            GL()
            SUMMAND()

    def MULTIPLIER():
        if current_lex['Тип лексемы'] in ('ID', 'действительное число', 'десятичное число', 'число в шестнадцатеричной системе',
                                          'число в восьмеричной системе', 'число в двоичной системе', 'TRUE', 'FALSE'):
            GL()
        elif current_lex['Тип лексемы'] == 'NOT':
            GL()
            MULTIPLIER()
        elif current_lex['Тип лексемы'] == 'LEFT_PAREN':
            GL()
            EXPRESSION()
            if current_lex['Тип лексемы'] == 'RIGHT_PAREN':
                GL()
            else:
                ERROR_HANDLER(7)
        else:
            ERROR_HANDLER(18)

    def CONDITION_OPERATOR():
        EXPRESSION()
        if current_lex['Тип лексемы'] == 'THEN':
            GL()
            OPERATOR()
            if current_lex['Тип лексемы'] == 'ELSE':
                GL()
                OPERATOR()
        else:
            ERROR_HANDLER(9)

    def WHILE_OPERATOR():
        EXPRESSION()
        if current_lex['Тип лексемы'] == 'DO':
            GL()
            OPERATOR()
        else:
            ERROR_HANDLER(10)

    def FOR_OPERATOR():
        if current_lex['Тип лексемы'] != 'ID':
            ERROR_HANDLER(21)
            return
        GL()
        ASSIGN_OPERATOR()
        if current_lex['Тип лексемы'] == 'TO':
            GL()
            EXPRESSION()
            if current_lex['Тип лексемы'] == 'DO':
                GL()
                OPERATOR()
            else:
                ERROR_HANDLER(11)
        else:
            ERROR_HANDLER(12)

    def ASSIGN_OPERATOR():
        if current_lex['Тип лексемы'] == 'ASSIGN':
            GL()
            EXPRESSION()

    def READ_OPERATOR():
        if current_lex['Тип лексемы'] == 'LEFT_PAREN':
            GL()
            ID_SEQUENCE()
            if current_lex['Тип лексемы'] != 'RIGHT_PAREN':
                ERROR_HANDLER(13)
            else:
                GL()
        else:
            ERROR_HANDLER(14)

    def WRITE_OPERATOR():
        if current_lex['Тип лексемы'] == 'LEFT_PAREN':
            EXPRESSION_SEQUENCE()
            if current_lex['Тип лексемы'] == 'RIGHT_PAREN':
                GL()
            else:
                ERROR_HANDLER(15)
        else:
            ERROR_HANDLER(16)

    def COMPLEX_OPERATOR():
        OPERATOR()
        while current_lex['Тип лексемы'] in ('COLON', 'LINE_BREAK'):
            GL()
            OPERATOR()
        if current_lex['Тип лексемы'] != 'END_COMPLEX':
            ERROR_HANDLER(17)
        else:
            GL()

    def ANALYZE():
        PROGRAM()

    def PROGRAM():
        GL()
        if current_lex['Тип лексемы'] == "BEGIN_PROG":
            GL()
            BODY()
            ERROR_HANDLER(1)
        else:
            ERROR_HANDLER(2)

    def BODY():
        if current_lex['Тип лексемы'] == "DIM":
            DESCRIPTION()
            GL()
        elif current_lex['Тип лексемы'] in ('ID', 'FOR', 'WHILE', 'IF', 'BEGIN_COMPLEX', 'READ', 'WRITE'):
            OPERATOR()
        else:
            ERROR_HANDLER(3)
        while current_lex['Тип лексемы'] == "SEMICOLON":
            GL()
            if current_lex['Тип лексемы'] == "DIM":
                DESCRIPTION()
                GL()
            elif current_lex['Тип лексемы'] in ('ID', 'FOR', 'WHILE', 'IF', 'BEGIN_COMPLEX', 'READ', 'WRITE'):
                OPERATOR()
            elif current_lex['Тип лексемы'] == "END_PROG":
                GL()
                break
            else:
                ERROR_HANDLER(4)

            if current_lex['Тип лексемы'] != "SEMICOLON":
                ERROR_HANDLER(4)
    total = 0
    current_lex = data[total]
    prev_lex = dict()
    ANALYZE()


with open('Lexical.txt', encoding='utf-8') as file:
    data = Lexical()
    for d in data:
        if d['Тип лексемы'] == "ERR":
            print(f"Неизвестная лексема: {d['Значение']}\nline {
                  d['Номер строки']}, position {d['Позиция в строке']}")
            exit(0)
    Syntactic()
