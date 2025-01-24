def manual_hash(data):
    """Қарапайым қолмен жасалған хэш алгоритмі"""
    hash_value = 0
    for char in data:
        hash_value += ord(char)  # Әріптің ASCII мәнін қосу
        hash_value *= 31  # Мультипликация арқылы қиындығын арттыру
    return hex(hash_value)  # Нәтижені 16-лық форматқа ауыстыру
import time

class Block:
    def __init__(self, data, previous_hash="0"):
        self.timestamp = time.time()  # Уақыт таңбасы
        self.data = data  # Блоктағы мәлімет
        self.previous_hash = previous_hash  # Алдыңғы блоктың хэші
        self.hash = self.calculate_hash()  # Өз хэші

    def calculate_hash(self):
        """Блоктың хэшін есептеу"""
        block_string = f"{self.timestamp}{self.data}{self.previous_hash}"
        return manual_hash(block_string)
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """Генезис блогын жасау"""
        return Block("Genesis Block")

    def add_block(self, data):
        """Жаңа блок қосу"""
        previous_block = self.chain[-1]
        new_block = Block(data, previous_block.hash)
        self.chain.append(new_block)

    def is_valid(self):
        """Блокчейннің жарамдылығын тексеру"""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Алдыңғы хэш сәйкес пе?
            if current_block.previous_hash != previous_block.hash:
                return False

            # Блоктың өз хэші дұрыс па?
            if current_block.hash != current_block.calculate_hash():
                return False

        return True
import tkinter as tk

class BlockchainExplorer:
    def __init__(self, blockchain):
        self.blockchain = blockchain
        self.window = tk.Tk()
        self.window.title("Blockchain Explorer")

        # Блоктарды көрсету үшін мәтін аймағы
        self.text_area = tk.Text(self.window, width=80, height=20)
        self.text_area.pack()

        # Блокчейнді тексеру батырмасы
        self.validate_button = tk.Button(self.window, text="Validate Blockchain", command=self.validate_chain)
        self.validate_button.pack()

        # Блоктарды көрсету
        self.display_chain()

    def display_chain(self):
        """Блоктардың тізімін көрсету"""
        self.text_area.delete(1.0, tk.END)
        for block in self.blockchain.chain:
            self.text_area.insert(tk.END, f"Address: {block.hash}\n")
            self.text_area.insert(tk.END, f"Timestamp: {block.timestamp}\n")
            self.text_area.insert(tk.END, f"Data: {block.data}\n")
            self.text_area.insert(tk.END, f"Previous Hash: {block.previous_hash}\n")
            self.text_area.insert(tk.END, "-" * 50 + "\n")

    def validate_chain(self):
        """Блокчейннің жарамдылығын тексеру"""
        is_valid = self.blockchain.is_valid()
        if is_valid:
            self.text_area.insert(tk.END, "Blockchain is valid.\n")
        else:
            self.text_area.insert(tk.END, "Blockchain is INVALID!\n")

    def run(self):
        self.window.mainloop()
# Хэш алгоритмі
def manual_hash(data):
    hash_value = 0
    for char in data:
        hash_value += ord(char)
        hash_value *= 31
    return hex(hash_value)

# Блок
import time
class Block:
    def __init__(self, data, previous_hash="0"):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.timestamp}{self.data}{self.previous_hash}"
        return manual_hash(block_string)

# Блокчейн
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("Genesis Block")

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(data, previous_block.hash)
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.previous_hash != previous_block.hash:
                return False
            if current_block.hash != current_block.calculate_hash():
                return False
        return True

# GUI
import tkinter as tk
class BlockchainExplorer:
    def __init__(self, blockchain):
        self.blockchain = blockchain
        self.window = tk.Tk()
        self.window.title("Blockchain Explorer")
        self.text_area = tk.Text(self.window, width=80, height=20)
        self.text_area.pack()
        self.validate_button = tk.Button(self.window, text="Validate Blockchain", command=self.validate_chain)
        self.validate_button.pack()
        self.display_chain()

    def display_chain(self):
        self.text_area.delete(1.0, tk.END)
        for block in self.blockchain.chain:
            self.text_area.insert(tk.END, f"Address: {block.hash}\n")
            self.text_area.insert(tk.END, f"Timestamp: {block.timestamp}\n")
            self.text_area.insert(tk.END, f"Data: {block.data}\n")
            self.text_area.insert(tk.END, f"Previous Hash: {block.previous_hash}\n")
            self.text_area.insert(tk.END, "-" * 50 + "\n")

    def validate_chain(self):
        is_valid = self.blockchain.is_valid()
        if is_valid:
            self.text_area.insert(tk.END, "Blockchain is valid.\n")
        else:
            self.text_area.insert(tk.END, "Blockchain is INVALID!\n")

    def run(self):
        self.window.mainloop()

# Блокчейнді іске қосу
if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.add_block("Block 1 Data")
    blockchain.add_block("Block 2 Data")
    explorer = BlockchainExplorer(blockchain)
    explorer.run()
