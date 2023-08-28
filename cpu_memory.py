class Storage:
    def __init__(self) -> None:
        self.cache = [0 for i in range(4)]
        self.cache_index = 0
        self.main_memory = [0 for i in range(260)]
        self.main_memory_index = 4

    def cache_insert(self, num):
        if self.cache_index > 3:
            self.cache_index = 0
        self.cache[self.cache_index] = num
        print(f"{num} stored in {self.cache_index}")
        self.cache_index += 1

    def main_insert(self, num):
        if self.main_memory_index > 260:
            self.main_memory_index = 4
        self.main_memory[self.main_memory_index] = num
        print(f"{num} stored in {self.main_memory_index}")
        self.main_memory_index += 1
        
    def print_main(self):
        found = False
        for i in range(4):
            if self.cache[i] != 0:
                found = True
                print(f"Index {i}: {self.cache[i]}")
        for j in range(260):
            if self.main_memory[j] != 0:
                found = True
                print(f"Index {j}: {self.main_memory[j]}")
        if not found:
            print("No values found in registers.")