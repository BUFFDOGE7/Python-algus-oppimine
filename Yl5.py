def show_truth_table():

    print("A AND (B OR C)")
    print("A  B  C  B OR C  Result")
    for A in [False, True]:
        for B in [False, True]:
            for C in [False, True]:
                b_or_c = B or C
                result = A and b_or_c
                print(int(A), int(B), int(C), int(b_or_c), int(result))

    print("\n(A XOR B) OR NOT(C AND A)")
    print("A  B  C  A XOR B  C AND A  NOT(C AND A)  Result")
    for A in [False, True]:
        for B in [False, True]:
            for C in [False, True]:
                a_xor_b = A != B
                c_and_a = C and A
                not_c_and_a = not c_and_a
                result = a_xor_b or not_c_and_a
                print(int(A), int(B), int(C), int(a_xor_b), int(c_and_a), int(not_c_and_a), int(result))

show_truth_table()