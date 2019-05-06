def secretCode(s):
    u = s
    u_count = 0
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    l_count = 0
    lower = upper.lower()
    num = '012345679'
    n_count = 0
    ans = ''
    for v, i in enumerate(s):
        if i in upper:
            u_count += 1
            if n_count != 0 or l_count != 0:
                l_count, n_count = 0, 0
        elif i in num:
            n_count += 1
            if n_count != 1 and u_count != 2:
                n_count, u_count = 0, 0
        elif i in lower:
            l_count += 1
            if l_count == 2 and u_count == 2 and n_count == 1:
                ans += s[v-2]
                n_count, l_count, u_count = 0, 0, 0
            elif l_count > 2:
                n_count, l_count, u_count = 0, 0, 0
    return ans


assert(secretCode('TT4za7GH5xpNHD1tyu8XQ9vg') == '459')
assert(secretCode('AAAAAAA4aaaaaBB5bb') == '5')
assert(secretCode('XX4xx6kk') == '4')
assert(secretCode('MMM555MMM') == '')
print("Pass")
