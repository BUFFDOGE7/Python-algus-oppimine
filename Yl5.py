import itertools

def generate_truth_table():
    variables = ['A', 'B', 'C']
    
    print("Truth Table for: A AND (B OR C)")
    print("=" * 50)
    print(f"{'A':<6}{'B':<6}{'C':<6}{'B OR C':<10}{'A AND (B OR C)':<15}")
    print("-" * 50)
    
    for values in itertools.product([False, True], repeat=3):
        A, B, C = values
        b_or_c = B or C
        result1 = A and b_or_c
        print(f"{int(A):<6}{int(B):<6}{int(C):<6}{int(b_or_c):<10}{int(result1):<15}")
    
    print("\n" + "=" * 50)
    print("Truth Table for: (A ~ B) OR NOT(C AND A)")
    print("=" * 50)
    print(f"{'A':<6}{'B':<6}{'C':<6}{'A ~ B':<10}{'C AND A':<10}{'NOT(C AND A)':<15}{'Result':<10}")
    print("-" * 50)
    
    for values in itertools.product([False, True], repeat=3):
        A, B, C = values
        a_xor_b = A != B
        c_and_a = C and A
        not_c_and_a = not c_and_a
        result2 = a_xor_b or not_c_and_a
        print(f"{int(A):<6}{int(B):<6}{int(C):<6}{int(a_xor_b):<10}{int(c_and_a):<10}{int(not_c_and_a):<15}{int(result2):<10}")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    generate_truth_table()