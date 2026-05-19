import base64
from datetime import datetime

class HistoryEntry:
    def __init__(self, url, timestamp, is_bookmark):
        self.url = url
        self.timestamp = timestamp
        self.is_bookmark = is_bookmark


class BrowserHistory:

    def __init__(self):
        self.entries = []          
        self.current_index = -1    

    def visit_page(self, url, is_bookmark=False):
        if self.current_index < len(self.entries) - 1:
            self.current_index = len(self.entries) - 1
        new_entry = HistoryEntry(url, datetime.now(), is_bookmark)
        self.entries.append(new_entry)
        self.current_index = len(self.entries) - 1

    def go_back(self):
        if self.current_index > 0:
            self.current_index -= 1
            return self.entries[self.current_index]
        return None

    def go_forward(self):
        if self.current_index < len(self.entries) - 1:
            self.current_index += 1
            return self.entries[self.current_index]
        return None

    def clear_history(self):
        self.entries = []
        self.current_index = -1

    def get_current(self):
        if 0 <= self.current_index < len(self.entries):
            return self.entries[self.current_index]
        return None

    def search_by_domain(self, domain):
        domain = domain.lower()
        result = []
        for entry in self.entries:
            if domain in entry.url.lower():
                result.append(entry)
        return result


    def load_from_base64(self, filepath):
        """Загрузить историю из Base64-файла (заменяет текущую)."""
        new_entries = []
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    decoded = base64.b64decode(line).decode()
                    parts = decoded.split('|')
                    if len(parts) != 3:
                        continue  
                    url, ts_str, bookmark_str = parts
                    timestamp = datetime.fromisoformat(ts_str)
                    is_bookmark = bool(int(bookmark_str))
                    new_entries.append(HistoryEntry(url, timestamp, is_bookmark))
        except FileNotFoundError:
            return None

        self.entries = new_entries
        self.current_index = len(self.entries) - 1


    def get_all_entries(self):
        """Вернуть все записи"""
        result = []
        for entrie in self.entries:
            a = [entrie.url, entrie.timestamp.strftime("%d/%m/%Y %H:%M:%S"), entrie.is_bookmark]
            result.append(a)
        return result

    def __len__(self):
        return len(self.entries)


if __name__ == "__main__":
    history = BrowserHistory()

    history.visit_page("https://google.com", is_bookmark=True)
    history.visit_page("https://github.com")
    history.visit_page("https://stackoverflow.com/questions/123")
    history.visit_page("https://youtube.com/watch?v=abc")

    print("Текущая:", history.get_current().url)
    print("Полный список", history.get_all_entries())


    back = history.go_back()
    print("Назад:", back.url)
    back = history.go_back()
    print("Назад:", back.url)
    fwd = history.go_forward()
    print("Вперёд:", fwd.url)


    print("\nПоиск по 'google':")
    for e in history.search_by_domain("google"):
        print(" -", e.url)

    test_file = "history.b64"
    history.load_from_base64(test_file)
    print(f"Загружено {len(history)} записей")
    print("Текущая после загрузки:", history.get_current().url)
    print("Полный список после загрузки:", history.get_all_entries())

    history.clear_history()
    print(f"\nПосле очистки: записей = {len(history)}")
    print("Назад:", history.go_back())