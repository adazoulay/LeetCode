def evaluate(RPN_expression):
    intermediate_result = []
    DELIMITER = ','
    OPERATORS = {
        '+': lambda y, x: x + y, '-': lambda y, x: x - y,
        '*': lambda y, x: x * y, '/': lambda y, x: int(x/y)
    }
    for token in RPN_expression.split(DELIMITER):
        print(intermediate_result)
        if token in OPERATORS:
            intermediate_result.append(OPERATORS[token](intermediate_result.pop(), intermediate_result.pop()))
        else:
            intermediate_result.append(int(token))
    return intermediate_result[-1]

print(evaluate("3,4,+,2,*,1,+"))