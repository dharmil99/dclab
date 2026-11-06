import threading
import time

# ------------------------------------------------------------
# DATA CONSISTENCY AND REPLICATION MODELS
#   1. Strong consistency   (synchronous replication)
#   2. Eventual consistency (asynchronous replication)
# ------------------------------------------------------------


class Replica:

    def __init__(self, name):
        self.name = name
        self.data = {}
        self.version = 0

    def apply(self, key, value, version):
        self.data[key] = value
        self.version = version

    def read(self, key):
        return self.data.get(key, None)


class ReplicatedStore:

    def __init__(self, replica_names):
        self.primary = Replica(replica_names[0])
        self.replicas = [Replica(n) for n in replica_names[1:]]
        self.version = 0

    def all_nodes(self):
        return [self.primary] + self.replicas

    # ---------- STRONG CONSISTENCY ----------
    def write_strong(self, key, value):

        self.version += 1

        print(f"\n[WRITE] {key} = {value} (version {self.version})")
        self.primary.apply(key, value, self.version)
        print(f"[PRIMARY] {self.primary.name} updated")

        # Write completes only after ALL replicas acknowledge
        for r in self.replicas:
            time.sleep(0.1)
            r.apply(key, value, self.version)
            print(f"[SYNC] {r.name} updated -> ACK received")

        print("[COMMIT] All replicas updated. Write acknowledged to client.")

    # ---------- EVENTUAL CONSISTENCY ----------
    def write_eventual(self, key, value, delay=1.0):

        self.version += 1
        version = self.version

        print(f"\n[WRITE] {key} = {value} (version {version})")
        self.primary.apply(key, value, version)
        print(f"[PRIMARY] {self.primary.name} updated")
        print("[COMMIT] Write acknowledged to client immediately.")

        def propagate(replica):
            time.sleep(delay)
            replica.apply(key, value, version)
            print(f"[ASYNC] {replica.name} updated in background")

        threads = []
        for i, r in enumerate(self.replicas):
            t = threading.Thread(target=propagate, args=(r,))
            t.start()
            threads.append(t)
            delay += 0.5

        return threads

    def show_state(self, key, title):
        print(f"\n--- {title} ---")
        for n in self.all_nodes():
            print(f"{n.name}: {key} = {n.read(key)} (v{n.version})")

        values = {n.read(key) for n in self.all_nodes()}
        if len(values) == 1:
            print("[STATUS] CONSISTENT")
        else:
            print("[STATUS] INCONSISTENT (stale replicas present)")


def main():

    print("\n========== DATA CONSISTENCY & REPLICATION ==========")

    # ---------- Strong ----------
    print("\n######## MODEL 1: STRONG CONSISTENCY ########")
    store = ReplicatedStore(["Primary", "Replica_1", "Replica_2"])
    store.write_strong("balance", 1000)
    store.show_state("balance", "Read after strong write")

    # ---------- Eventual ----------
    print("\n######## MODEL 2: EVENTUAL CONSISTENCY ########")
    store2 = ReplicatedStore(["Primary", "Replica_1", "Replica_2"])
    store2.write_eventual("balance", 2000)

    store2.show_state("balance", "Read IMMEDIATELY after async write")

    print("\n[WAIT] Waiting for replication to finish...")
    for t in threading.enumerate():
        if t is not threading.main_thread():
            t.join()

    store2.show_state("balance", "Read AFTER propagation")

    print("\n========== SUMMARY ==========")
    print("Strong   : higher latency, replicas always identical.")
    print("Eventual : low latency, replicas may be stale briefly,")
    print("           but converge when propagation finishes.")
    print("=============================")


if __name__ == "__main__":
    main()
