A_idx = 0


def is_bracket_valid(expr: str) -> bool:
    parity = 0
    for char in expr:
        if char == '(':
            parity += 1
        elif char == ')':
            parity -= 1
        else:
            pass
        if parity < 0:
            return False
    return parity == 0


def cleaner(expr: str) -> str:
    incomming = expr.split(' ')
    return "".join(incomming)


def get_number(expr: str):
    global A_idx
    is_int = True
    num_idx = A_idx

    while A_idx < len(expr) and expr[A_idx].isdigit():
        A_idx += 1
    if A_idx < len(expr) and expr[A_idx] == ".":
        is_int = False
        A_idx += 1
    while A_idx < len(expr) and expr[A_idx].isdigit():
        A_idx += 1

    return int(expr[num_idx:A_idx]) if is_int else float(expr[num_idx:A_idx])


def get_term_3(expr: str):
    global A_idx

    if A_idx > len(expr) - 1:
        return

    if expr[A_idx] == "(":
        A_idx += 1
        exp = get_expr(expr)
        if expr[A_idx] == ")":
            A_idx += 1
            return exp
        else:
            print("Не парные скобки")
            return

    return get_number(expr)


def get_term_2(expr: str):
    global A_idx

    if expr[A_idx] == "-":
        A_idx += 1
        return -get_term_3(expr)
    return get_term_3(expr)


def get_term_1(expr: str):
    global A_idx

    term_2 = get_term_2(expr)
    if A_idx > len(expr) - 1:
        return term_2

    if expr[A_idx] == "*":
        A_idx += 1
        return term_2 * get_term_1(expr)
    elif expr[A_idx] == "/":
        A_idx += 1
        return term_2 / get_term_1(expr)

    return term_2


def get_expr(expr: str):
    global A_idx

    term_1 = get_term_1(expr)
    if A_idx > len(expr) - 1:
        return term_1

    if expr[A_idx] == "+":
        A_idx += 1
        return term_1 + get_expr(expr)
    elif expr[A_idx] == "-":
        A_idx += 1
        return term_1 - get_expr(expr)

    return term_1


def evaluate(expr: str):
    '''
    Основная функция для парсинга арифметического выражения
    '''
    if expr is None or len(expr) == 0:
        print("Пустое выражение")
        return
    else:
        if is_bracket_valid(expr):
            return get_expr(expr)
        else:
            print("Несоответствие закрытых и открытых скобок")
            return


while True:
    expr = input("Введите выражение для вычисления (для выхода - 'x')? ")
    if expr == 'x':
        break
    expr = cleaner(expr)
    print(f"= {evaluate(expr)}")
    A_idx = 0