import json


class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            title= data["title"],
            author= data["author"],
        )
    def __str__(self):
        return f"{self.title} by {self.author}"

b1 = Book("1488", "Orge Georwell")
b2 = Book("Brave New World", "Aldous Huxley")

book_dict1 = b1.to_dict()
book_dict2 = b2.to_dict()

book_list = [book_dict1, book_dict2]
json_string = json.dumps(book_list, ensure_ascii=False, indent=4)
print(json_string)

load_dicts = json.loads(json_string)
print(load_dicts)
books_restored= [Book.from_dict(d) for d in load_dicts]
for b in books_restored:
    print(b)


