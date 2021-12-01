def main():
    with open("input.txt") as file:
        input = file.read().strip()

    group_answers = input.split('\n\n')
    group_answers = [answer.replace('\n', '') for answer in group_answers]

    maps = []
    for answers in group_answers:
        map = {}
        for answer in answers:
            map[answer] = True
        maps.append(map)

    sum = 0
    for map in maps:
        sum += len(list(map.keys()))

    print("sum of counts:", sum)


main()
