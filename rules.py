from copy import deepcopy


def replace(items: list, values: list):
    result = ' '.join(items)
    for v in values:
        result = result.replace(v, 'True')
    return [item if item == '&' or item == '|' or item == '~' else bool(item) if item == 'True' else bool() for item in result.split()]


class Rule:
    def __init__(self, op: list, result: str):
        self.op = op
        self.result = result

    def evaluate(self, values: list):
        result_list = []
        neg = False
        for target_list in replace(self.op, values):
            if target_list == '~':
                neg = True
            else:
                if neg:
                    result_list.append(not target_list)
                else:
                    result_list.append(target_list)

        result = True
        if result_list[1] == '&':
            op = bool.__and__
        else:
            op = bool.__or__
        for i in range(2, len(result_list)-2, 2):
            result = op(result, result_list[i])
            if result_list[i+1] == '&':
                op = bool.__and__
            else:
                op = bool.__or__

        result = op(result, result_list[len(result_list)-1])

        return result

    def __str__(self):
        return ' '.join(self.op)
