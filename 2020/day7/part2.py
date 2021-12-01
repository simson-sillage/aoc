class Bags:
    def __init__(self, color, count):
        self.color = color
        self.count = count


def main():
    with open("input.txt") as file:
        input = file.read().strip()

    bags = {}
    rules = input.split('\n')
    for rule in rules:
        outer_bag_rule, inner_bags_rules = rule.split('contain')
        inner_bags_rules = inner_bags_rules.strip()
        outer_bag_color = outer_bag_rule.replace("bags", "").strip()

        if inner_bags_rules == "no other bags.":
            bags[outer_bag_color] = []
            continue

        inner_bags_rules = inner_bags_rules.split(',')
        inner_bags = []
        for inner_bag in inner_bags_rules:
            words = inner_bag.strip().split(' ')
            bag_count = int(words[0])
            inner_bag_color = words[1] + " " + words[2]
            bag = Bags(inner_bag_color, bag_count)
            inner_bags.append(bag)

        bags[outer_bag_color] = inner_bags

    count = count_bags('shiny gold', bags)

    print(f"a single shiny gold bag must contain {count} other bags.")


def count_bags(color, bags):
    inner_bags = bags.get(color, [])

    if len(inner_bags) == 0:
        return 0

    count = 0
    for bag in inner_bags:
        count += bag.count + bag.count * count_bags(bag.color, bags)

    return count


main()
