from collections import defaultdict
from multiprocessing import Pool

# ------------------------------------------------------------
# BASIC MAPREDUCE JOB (WORD COUNT)
# Simulates the Hadoop/Spark phases: Split -> Map -> Shuffle
# -> Reduce, using parallel worker processes.
# (No Hadoop / Spark installation required.)
# ------------------------------------------------------------

DOCUMENTS = [
    "distributed systems share resources over a network",
    "mapreduce processes big data in a distributed system",
    "map splits the work and reduce combines the results",
    "big data needs distributed processing"
]


# MAP: runs on each input split, emits (word, 1) pairs
def map_function(task):

    split_id, text = task

    pairs = []

    for word in text.lower().split():
        pairs.append((word, 1))

    print(f"[MAPPER {split_id}] Emitted {len(pairs)} pairs")

    return pairs


# REDUCE: runs on each key, sums its values
def reduce_function(item):

    word, counts = item

    return word, sum(counts)


def main():

    print("\n========== MAPREDUCE: WORD COUNT ==========")

    # ---------- INPUT SPLITS ----------
    print("\n[INPUT] Splitting input into chunks...")
    tasks = list(enumerate(DOCUMENTS))

    for split_id, text in tasks:
        print(f"[SPLIT {split_id}] {text}")

    # ---------- MAP PHASE ----------
    print("\n[MAP PHASE] Running mappers in parallel...")

    with Pool(processes=len(tasks)) as pool:
        mapped = pool.map(map_function, tasks)

    # ---------- SHUFFLE & SORT ----------
    print("\n[SHUFFLE PHASE] Grouping values by key...")

    grouped = defaultdict(list)

    for pairs in mapped:
        for word, count in pairs:
            grouped[word].append(count)

    for word in sorted(grouped)[:5]:
        print(f"[SHUFFLE] {word} -> {grouped[word]}")
    print("[SHUFFLE] ...")

    # ---------- REDUCE PHASE ----------
    print("\n[REDUCE PHASE] Running reducers in parallel...")

    with Pool() as pool:
        reduced = pool.map(reduce_function, sorted(grouped.items()))

    # ---------- OUTPUT ----------
    print("\n========== FINAL OUTPUT ==========")

    for word, total in sorted(reduced, key=lambda x: (-x[1], x[0])):
        print(f"{word:<15} {total}")

    print("\nTotal unique words:", len(reduced))
    print("Total words       :", sum(c for _, c in reduced))
    print("==================================")


if __name__ == "__main__":
    main()
