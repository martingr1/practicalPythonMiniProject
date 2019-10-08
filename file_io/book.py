import re
import collections

text = open('/workspace/practicalPythonMiniProject/file_io/files/relative_data.txt').read().lower()
words = re.findall('\w+', text)
print(collections.Counter(words).most_common(10))