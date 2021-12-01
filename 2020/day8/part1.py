from collections import defaultdict


def main():
    with open("input.txt") as file:
        input = file.read().strip()

    instructions = input.split('\n')
    accumulator, ip = interpreter(instructions)
    print(f"accumulator: {accumulator}, instruction pointer: {ip}")


def interpreter(instructions):
    accumulator = 0
    ip = 0
    run_instructions = defaultdict(lambda: False)
    while True:
        if run_instructions[ip]:
            break
        run_instructions[ip] = True

        cmd, offset = instructions[ip].split(" ")
        offset = int(offset)
        match cmd:
            case 'nop':
                ip += 1
                continue
            case 'acc':
                accumulator += offset
                ip += 1
                continue
            case 'jmp':
                ip += offset
                continue
            case _:
                raise ValueError(f"invalid instruction: {cmd} {offset}")

    return accumulator, ip


main()
