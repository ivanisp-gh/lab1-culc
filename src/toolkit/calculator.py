from toolkit.errors import DivisionByZeroError , ValidationError

def calc(line: str) -> str:
    numbers: list = [str(x) for x in range(0, 10)]
    symbols: list = ['+', '-', '*', '/','%','//']
    line_list=list()
    A = str()
    for i in range(len(line)):
        if line[i].isspace():
            pass
        elif (line[i] == '-' and len(A)==0) or line[i] in numbers or line[i]=='.':
            A = A +line[i]
        elif line[i] in symbols:
            if line[i:i+2] == '//':
                line_list.append(A)
                A = str()
                line_list.append('//')
            elif A and A[-1] in numbers:
                line_list.append(A)
                A = str()
                line_list.append(line[i])
    line_list.append(A)
    if len(line_list)%2==0:
        raise ValidationError('Перепроверьте выражение')




    while any(x in line_list for x in ['*','/','//','%']):
        index_list = [line_list.index(x) for x in ['*','/','//','%'] if x in line_list]
        index = min(index_list)
        if line_list[index] == '*':
            line_list[index] = str(float(line_list[index - 1]) * float(line_list[index + 1]))
        elif line_list[index] == '/':
            if float(line_list[index + 1])==0:
                raise DivisionByZeroError('Нельзя делить на ноль')
            line_list[index] = str(float(line_list[index - 1]) / float(line_list[index + 1]))
        elif line_list[index] == '//':
            if float(line_list[index + 1])==0:
                raise DivisionByZeroError('Нельзя делить на ноль')
            line_list[index] = str(float(line_list[index - 1]) // float(line_list[index + 1]))
        elif line_list[index] == '%':
            if float(line_list[index + 1])==0:
                raise DivisionByZeroError('Нельзя делить на ноль')
            line_list[index] = str(float(line_list[index - 1]) % float(line_list[index + 1]))
        line_list = line_list[:index - 1] + [line_list[index]] + line_list[index + 2:]

    while '+' in line_list:
        index = line_list.index('+')
        line_list[index] = str(float(line_list[index - 1]) + float(line_list[index + 1]))
        line_list = line_list[:index - 1] + [line_list[index]] + line_list[index + 2:]
    while '-' in line_list:
        index = line_list.index('-')
        line_list[index] = str(float(line_list[index - 1]) - float(line_list[index + 1]))
        line_list = line_list[:index - 1] + [line_list[index]] + line_list[index + 2:]
    return line_list[0]



def parenthesis(line: str) -> str: #Поиск внутрених скобок
    l_index: int=line.index('(')
    r_index: int=line.index(')')-1
    while '('  in line[l_index:r_index+1]:
        l_index+=1
    return line[:l_index-1] + calc(line[l_index:r_index+1]) + line[r_index+2:]


def calculation(line):
    while '(' in line:
        if line.count('(')!=line.count(')'):
            raise ValidationError('Перепроверьте выражение на количество скобок')
        line = parenthesis(line)
    return calc(line) 