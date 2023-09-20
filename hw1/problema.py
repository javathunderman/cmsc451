n = int(input())
a = []
for i in range(0, int(n)):
    raw_lst_str = input()
    a_i = list(map(int, raw_lst_str.split()))
    m_i = a_i.pop(0)
    a.append((m_i, a_i))

sumval = 0
for m_a_pair in a:
    m_i = m_a_pair[0]
    a_i = m_a_pair[1]
    for j in range(0, n):
        m_j = a[j][0]
        a_j = a[j][1]
        for k in range(0, min(m_i, m_j)):
            sumval += int((a_i[k] ^ a_j[k]) / (a_i[k] & a_j[k]))
print(sumval)