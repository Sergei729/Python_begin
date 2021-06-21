# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.

import json

with open('firms.json', 'w') as firm:
    with open('firms.txt', encoding='utf-8') as f:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}
        result = [profit, {'Average_profit = ': round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                                      len([int(i) for i in profit.values() if int(i) > 0]))}]

    json.dump(result, firm, ensure_ascii=False, indent=4)
