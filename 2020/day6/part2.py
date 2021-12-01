from collections import defaultdict


class Vote:
    def __init__(self):
        self.voter_count = 0
        self.map = defaultdict(lambda: 0)


def main():
    with open("input.txt") as file:
        input = file.read().strip()

    group_answers_raw = input.split('\n\n')
    group_answers = []
    for answers_raw in group_answers_raw:
        answers = answers_raw.split('\n')
        group_answers.append(answers)

    votes = []
    for answers in group_answers:
        vote = Vote()
        vote.voter_count = len(answers)
        for answer in ''.join(answers):
            vote.map[answer] += 1
        votes.append(vote)

    sum = 0
    for vote in votes:
        for _, value in vote.map.items():
            if value == vote.voter_count:
                sum += 1

    print("sum of counts:", sum)


main()
