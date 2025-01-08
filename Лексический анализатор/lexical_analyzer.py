with open('lex_test.txt', encoding='utf-8') as file:
    data = file.read()
    data += '\n'
    status = "H"
    n = 0
    letter = data[n]
    key_words = list()
    idents = list()
    numbers = list()
    operations = list()
    seps = list()
    mistakes = list()
    while (n != len(data)):
        match status:
            case "H":
                flag_err = "OK"
                while letter in ("\n", " ", "\t"):
                    n += 1
                    try:
                        letter = data[n]
                    except:
                        print(f"Ключевые слова: {key_words}")
                        print(f"Идентификаторы: {idents}")
                        print(f"Числа: {numbers}")
                        print(f"Операторы присваивания: {operations}")
                        print(f"Разделители: {seps}")
                        print(f"Исключения: {mistakes}")
                        exit()
                if letter.isalpha() or letter == '_':
                    status = "ID"
                elif letter.isdigit() or letter in '+-.':
                    status = "NM"
                elif letter == ":":
                    status = "ASGN"
                else:
                    status = "DLM"
            case "ID":
                flag_err = "OK"
                id = letter
                n += 1
                letter = data[n]
                while letter.isalpha() or letter.isdigit() or letter == '_':
                    id += letter
                    n += 1
                    letter = data[n]
                if id in ('for', 'do'):
                    key_words.append(id)
                else:
                    idents.append(id)
                status = "H"
            case "NM":
                flag_err = "OK"
                num = letter
                n += 1
                letter = data[n]
                while letter.isdigit() or letter in '.+-eElLfF':
                    num += letter
                    n += 1
                    letter = data[n]
                c = num.count('f')+num.count('F')+num.count('l')+num.count('L')
                if c == 1:
                    if num[-1] in 'fFlL':
                        try:
                            float(num[:-1])
                        except:
                            flag_err = "NM"
                            status = "ERR"
                    else:
                        flag_err = "NM"
                        status = "ERR"
                elif c > 2:
                    flag_err = "NM"
                    status = "ERR"
                elif c == 0:
                    try:
                        float(num)
                    except:
                        flag_err = "NM"
                        status = "ERR"
                if flag_err == "OK":
                    numbers.append(num)
                    status = "H"
            case "ASGN":
                flag_err = "OK"
                op = letter
                n += 1
                letter = data[n]
                op += letter
                if op == ':=':
                    operations.append(op)
                    status = "H"
                else:
                    flag_err = "ASGN"
                    status = "ERR"
                n += 1
                letter = data[n]
            case "DLM":
                flag_err = "OK"
                if letter in ('(', ')', ';', '<', '>', '='):
                    seps.append(letter)
                    n += 1
                    letter = data[n]
                    status = "H"
                else:
                    status = "ERR"
            case "ERR":
                if flag_err == "ASGN":
                    mistakes.append(op)
                if flag_err == "NM":
                    mistakes.append(num)
                if flag_err == "DLM":
                    mistakes.append(letter)
                status = "H"
