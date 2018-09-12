import tempfile
from word_count import WordCounter

with tempfile.NamedTemporaryFile() as writable_fd:
    writable_fd.write(b"123")
    writable_fd.flush()

    print("===> creating WordCounter")
    wc = WordCounter(writable_fd.name).search("2")
    print("===> created WordCounter")

print("===> deleting wc")
del wc
print("===> deleted wc")
