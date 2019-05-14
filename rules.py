from copy import deepcopy


def replace(items: list, values: dict):
    result = ' '.join(items)
    for k, v in values.items():
        result = result.replace(k, str(v))
    return [item if item == '&' or item == '|' or item == '~' else float(item) for item in result.split()]


class Rule:
    def __init__(self, rule: list, op_or, op_and, op_not):
        self.rule = rule
        self.op_or = op_or
        self.op_and = op_and
        self.op_not = op_not

    def evaluate(self, values: dict):
        result_list = []        
        neg = False
        for target_list in replace(self.rule, values):
            if target_list == '~':
                neg = True
            elif target_list == '&' or target_list == '|':
                result_list.append(target_list)
            else:
                if neg:
                    result_list.append(self.op_not(target_list))
                    neg = False
                else:
                    result_list.append(target_list)

        result = result_list[0]
        if result_list[1] == '&':
            op = self.op_and
        else:
            op = self.op_or
        for i in range(2, len(result_list)-2, 2):
            result = op(result, result_list[i])
            if result_list[i+1] == '&':
                op = self.op_and
            else:
                op = self.op_or

        result = op(result, result_list[len(result_list)-1])

        return result

    def __str__(self):
        return ' '.join(self.rule)
