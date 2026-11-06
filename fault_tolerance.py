import time

# ------------------------------------------------------------
# SIMPLE FAULT TOLERANCE WITH PRIMARY-BACKUP REPLICATION
# The primary serves requests and copies every update to the
# backup. A heartbeat monitor detects primary failure and the
# backup is promoted, so no data is lost.
# ------------------------------------------------------------


class Server:

    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.alive = True
        self.data = {}

    def heartbeat(self):
        return self.alive


class PrimaryBackupSystem:

    def __init__(self):
        self.primary = Server("Server_A", "PRIMARY")
        self.backup = Server("Server_B", "BACKUP")

    def write(self, key, value):

        if not self.primary.alive:
            self.failover()

        self.primary.data[key] = value
        print(f"[{self.primary.role}] {self.primary.name} stored {key} = {value}")

        if self.backup.alive:
            self.backup.data[key] = value
            print(f"[REPLICATE] Copied to {self.backup.name}")
        else:
            print("[WARNING] No backup available - running unprotected!")

    def read(self, key):

        if not self.primary.alive:
            self.failover()

        value = self.primary.data.get(key)
        print(f"[READ] {self.primary.name} -> {key} = {value}")
        return value

    def check_heartbeat(self):

        print(f"\n[HEARTBEAT] Pinging {self.primary.name}...")

        if self.primary.heartbeat():
            print("[HEARTBEAT] Primary is ALIVE")
        else:
            print("[HEARTBEAT] No response from primary!")
            self.failover()

    def failover(self):

        print("\n[FAILURE DETECTED] Primary is DOWN")
        print(f"[FAILOVER] Promoting {self.backup.name} to PRIMARY...")

        time.sleep(0.3)

        self.primary, self.backup = self.backup, self.primary
        self.primary.role = "PRIMARY"
        self.backup.role = "BACKUP (FAILED)"

        print(f"[FAILOVER] {self.primary.name} is now the PRIMARY")
        print(f"[FAILOVER] Recovered data: {self.primary.data}")

    def recover(self):

        print(f"\n[RECOVERY] {self.backup.name} restarting...")

        self.backup.alive = True
        self.backup.data = dict(self.primary.data)
        self.backup.role = "BACKUP"

        print(f"[RECOVERY] {self.backup.name} resynced from primary")
        print(f"[RECOVERY] Data: {self.backup.data}")


def main():

    print("\n========== PRIMARY-BACKUP FAULT TOLERANCE ==========")

    system = PrimaryBackupSystem()

    print("\n--- Phase 1: Normal operation ---")
    system.write("order_1", "BUY 100 AAPL")
    system.write("order_2", "SELL 50 TSLA")
    system.check_heartbeat()

    print("\n--- Phase 2: Primary crashes ---")
    system.primary.alive = False
    print(f"[SIMULATION] {system.primary.name} crashed!")
    system.check_heartbeat()

    print("\n--- Phase 3: Service continues on new primary ---")
    system.read("order_1")
    system.write("order_3", "BUY 20 MSFT")

    print("\n--- Phase 4: Failed server recovers ---")
    system.recover()

    print("\n========== FINAL STATE ==========")
    print(f"{system.primary.name} ({system.primary.role}): {system.primary.data}")
    print(f"{system.backup.name} ({system.backup.role}): {system.backup.data}")
    print("[SUCCESS] No data lost during failover.")
    print("=================================")


if __name__ == "__main__":
    main()
