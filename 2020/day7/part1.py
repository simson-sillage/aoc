def main():
    with open("input.txt") as file:
        input = file.read().strip()

    colors = {}
    rules = input.split('\n')
    for rule in rules:
        outer_bag, inner_bags = rule.split('contain')
        outer_bag_color = outer_bag.replace("bags", "").strip()

        if inner_bags == "no other bags.":
            colors[outer_bag_color] = []
            continue

        inner_bags = inner_bags.split(',')
        inner_colors = []
        for inner_bag in inner_bags:
            words = inner_bag.strip().split(' ')
            inner_bag_color = words[1] + " " + words[2]
            inner_colors.append(inner_bag_color)

        colors[outer_bag_color] = inner_colors

    count = 0
    for outer_color in colors.keys():
        if can_contain(outer_color, colors, 'shiny gold'):
            count += 1

    print(f"{count} bag colors can contain shiny gold.")


def can_contain(current, rules, target):
    inner_colors = rules.get(current, [])
    if len(inner_colors) == 0:
        return False
    for inner_color in inner_colors:
        if inner_color == target:
            return True
    for inner_color in inner_colors:
        if can_contain(inner_color, rules, target):
            return True

    return False


main()
