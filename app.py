import streamlit as st
import random

"""
# Miller–Rabin Primality Tester
*Made by [Raunak Chowdhuri](https://sauhaarda.me/)*

After learning the concept in MIT's 18.200A (Applied Discrete Mathematics), I implemented this primality checker which shows its work.
"""

n = st.number_input('Number to be Tested', format='%d', value=561)
use_small_a = st.checkbox('Small/Predtermined a?', value=True)

if st.button('Calculate!'):
    s = 0
    t = n - 1

    while t % 2 == 0:
        s += 1
        t = t // 2

    f"The first step is to factor powers of $2$ out of $n-1 = {n-1}$ via repeated division: ${n-1} = 2^{s} \cdot {t}$."

    f"Next, we choose some $a$, between 1 and {n-1}."
    prime = True

    for a in range(2, 5):
        if not use_small_a:
            a = random.randint(2, n-1)
        f"Let's pick $a = {a}$"

        if n % a == 0:
            f'{n} is divisible by {a}. It is definitely not prime!'
            prime = False
            break

        prev = None
        for exp in range(s+1):
            old_prev = prev
            prev = pow(a, t, n) if prev is None else prev ** 2 % n
            f"${a}^{{2^{exp} \cdot {t}}} \equiv {a}^{{{2**exp} \cdot {t}}} \equiv {prev}$ (mod ${n}$)"
            if old_prev is not None and prev == 1 and old_prev != 1 and old_prev != n-1:
                f"Looking at the last two iterations, we find that ${old_prev}^2 \equiv {prev}$ (mod ${n}$)."
                prime = False
                break
        if not prime:
            break
        else:
            "This test determined that the number may be prime."
    if not prime:
        st.error(f'${n}$ is definitely not prime.')
    else:
        st.warning(f'{n} may be prime!')