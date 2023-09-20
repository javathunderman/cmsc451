import heapq

class Student:
    def __init__(self, t_i, r_i, s_i, index):
        self.s_i = s_i
        self.r_i = r_i
        self.t_i = t_i
        self.next_break = s_i
        self.default_t_i = t_i
        self.index = index + 1
        self.skip = False
    def __lt__(self, other):
        return (self.t_i < other.t_i)
    def __le__(self, other):
        return (self.t_i <= other.t_i)
    def __eq__(self, other):
        return (self.t_i == other.t_i)
    def __ne__(self, other):
        return (self.t_i != other.t_i)
    def __gt__(self, other):
        return (self.t_i > other.t_i)
    def __ge__(self, other):
        return (self.t_i >= other.t_i)
    def __str__(self):
        return f"Student {self.index} with {self.t_i} time and next break in {self.next_break}. Skipping? {self.skip}"

def main():
    raw_in = input().split()
    n = int(raw_in[0])
    m = int(raw_in[1])
    students = []
    times = [0]
    for i in range(0, int(n)):
        raw_lst_str = input()
        a_i = list(map(int, raw_lst_str.split()))
        heapq.heappush(students, Student(a_i[0], a_i[1], a_i[2], i))
    # for s in students:
    #     print(s)
    # print()
    while (len(times) != m + 1):
        s = heapq.heappop(students)
        if not s.skip:
            # print(f"Solved by student {s.index} at {s.t_i} minutes")
            times.append(s.t_i)
            s.next_break -= 1
        # else:
        #     print(f"No solve at {s.t_i} minutes")

        if (s.next_break == 0):
            s.t_i += s.r_i
            s.skip = True
            s.next_break = s.s_i
        else:
            s.skip = False
            s.t_i += s.default_t_i
        heapq.heappush(students, s)
        # for s in students:
        #     print(s)
        # print()
    print(times[-1])

main()


