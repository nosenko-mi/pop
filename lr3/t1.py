from random import choice


def generate_random_sequence(possible_values: list[int], length: int) -> list[int]:
    return [choice(possible_values) for _ in range(length)]


def count_it(sequence: list[int], N: int=3) -> dict[int, int]:
    freq_dist = {}
    for i in sequence:
        if i in freq_dist:
            freq_dist[i] += 1
        else:
            freq_dist[i] = 1

    sorted_freq = dict(sorted(freq_dist.items(), key=lambda item: item[1], reverse=True)[:N])
    return sorted_freq


def main():
    
    random_sequence = generate_random_sequence(list(range(9)), 15)
    print(f"Random sequence: {random_sequence}")
    n = 3
    top_freq = count_it(random_sequence, n)
    print(f"Top {n} most frequent values: {top_freq}")



main()
