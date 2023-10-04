class Match:
    def __init__(self, competitor_one, competitor_two):
        self.competitor_one = competitor_one
        self.competitor_two = competitor_two
        self.winner = None
    def __str__(self):
        return f"{self.competitor_one} vs. {self.competitor_two} with {self.winner} as the winner"
def main():
    num_competitors = int(input())
    competitors = dict()
    matches = dict()
    match_nums = []
    for i in range(0, num_competitors):
        input_str = input()
        input_str = input_str.split()
        competitors[input_str[0]] = int(input_str[1])

    for i in range(0, num_competitors - 1):
        input_str = input()
        input_str = input_str.split()
        match_nums.append(int(input_str[0]))
        matches[input_str[0]] = Match(input_str[1], input_str[2])

    for current_match in match_nums:
        if matches[str(current_match)].winner == None:
            visit_match(matches, matches[str(current_match)] , competitors)

    match_nums = sorted(match_nums)
    for current_match in match_nums:
        print(f"{current_match} {matches[str(current_match)].winner}")

def visit_match(matches, match, competitors):
    if (match.winner is None):
        if (match.competitor_one.isdigit()):
            visit_match(matches, matches[match.competitor_one], competitors)
            match.competitor_one = matches[match.competitor_one].winner
        if (match.competitor_two.isdigit()):
            visit_match(matches, matches[match.competitor_two], competitors)
            match.competitor_two = matches[match.competitor_two].winner
        if (competitors[match.competitor_one] > competitors[match.competitor_two]):
            match.winner = match.competitor_one
        else:
            match.winner = match.competitor_two

if __name__ == "__main__":
    main()
