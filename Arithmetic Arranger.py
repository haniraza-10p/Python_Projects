def arithmetic_arranger(problems, answer_required=False):
    first = True
    line1 = line2 = line3 = line4 = ""
    side_space = "    "

    if len(problems) > 5:
        return "Error: Too many problems."

    for p in problems:
        p = p.split()

        if len(p[0]) > 4 or len(p[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        if p[1] != '+' and p[1] != '-':
            return "Error: Operator must be '+' or '-'."

        try:
            int(p[0])
            int(p[2])
        except ValueError:
            return "Error: Numbers must only contain digits."

        param1 = p[0]
        param2 = p[2]

        opera = p[1]
        if answer_required:
            if p[1] == '+':
                answer = int(param1) + int(param2)
            else:
                answer = int(param1) - int(param2)

        space = max(len(param1), len(param2))

        if first:
            line1 += param1.rjust(space + 2)
            line2 += opera + ' ' + param2.rjust(space)
            line3 += '-' * (space + 2)
            if answer_required:
                line4 += str(answer).rjust(space + 2)
            first = False
        else:
            line1 += param1.rjust(space + 6)
            line2 += opera.rjust(5) + ' ' + param2.rjust(space)
            line3 += side_space + '-' * (space + 2)
            if answer_required:
                line4 += str(answer).rjust(space + 6)

    if answer_required:
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    else:
        return line1 + '\n' + line2 + '\n' + line3


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
