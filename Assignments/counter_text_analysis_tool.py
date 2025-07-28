from collections import Counter
import re

class TextAnalyzer:
    def __init__(self, text):
        self.original_text = text
        self.text = text.lower()  # For case-insensitive analysis

    def get_character_frequency(self, include_spaces=False):
        filtered_text = self.text if include_spaces else self.text.replace(" ", "")
        return Counter(filtered_text)

    def get_word_frequency(self, min_length=1):
        words = re.findall(r'\b\w+\b', self.text)
        filtered = [word for word in words if len(word) >= min_length]
        return Counter(filtered)

    def get_sentence_length_distribution(self):
        sentences = re.split(r'[.!?]', self.original_text)
        lengths = [len(re.findall(r'\b\w+\b', s)) for s in sentences if s.strip()]
        counter = Counter(lengths)
        if not lengths:
            return {"lengths": counter, "average": 0, "longest": 0, "shortest": 0}

        return {
            "lengths": counter,
            "average": sum(lengths) / len(lengths),
            "longest": max(lengths),
            "shortest": min(lengths)
        }

    def find_common_words(self, n=10, exclude_common=True):
        common_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by',
            'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does',
            'did', 'will', 'would', 'could', 'should', 'may', 'might', 'can', 'this', 'that',
            'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her',
            'us', 'them'
        }
        words = re.findall(r'\b\w+\b', self.text)
        if exclude_common:
            words = [w for w in words if w not in common_words]
        return Counter(words).most_common(n)

    def get_reading_statistics(self):
        characters = len(self.text.replace(" ", ""))
        words = re.findall(r'\b\w+\b', self.text)
        sentences = re.split(r'[.!?]', self.text)
        word_count = len(words)
        sentence_count = len([s for s in sentences if s.strip()])
        avg_word_length = sum(len(w) for w in words) / word_count if word_count else 0
        reading_time = word_count / 200  # assume 200 words per minute

        return {
            "character_count": characters,
            "word_count": word_count,
            "sentence_count": sentence_count,
            "average_word_length": avg_word_length,
            "reading_time_minutes": round(reading_time, 2)
        }

    def compare_with_text(self, other_text):
        other_analyzer = TextAnalyzer(other_text)
        self_words = set(re.findall(r'\b\w+\b', self.text))
        other_words = set(re.findall(r'\b\w+\b', other_text.lower()))

        common = self_words & other_words
        unique_to_self = self_words - other_words
        unique_to_other = other_words - self_words

        total_words = len(self_words | other_words)
        similarity = len(common) / total_words if total_words else 0

        return {
            "common_words": list(common),
            "similarity_score": round(similarity, 2),
            "unique_to_first": list(unique_to_self),
            "unique_to_second": list(unique_to_other)
        }

# Test your implementation
sample_text = """
Python is a high-level, interpreted programming language with dynamic semantics.
Its high-level built-in data structures, combined with dynamic typing and dynamic binding,
make it very attractive for Rapid Application Development. Python is simple, easy to learn
syntax emphasizes readability and therefore reduces the cost of program maintenance.
Python supports modules and packages, which encourages program modularity and code reuse.
The Python interpreter and the extensive standard library are available in source or binary
form without charge for all major platforms, and can be freely distributed.
"""

analyzer = TextAnalyzer(sample_text)

print("Character frequency (top 5):", analyzer.get_character_frequency()[:5])
print("Word frequency (top 5):", analyzer.get_word_frequency()[:5])
print("Common words:", analyzer.find_common_words()[:5])
print("Reading statistics:", analyzer.get_reading_statistics())

# Compare with another text
other_text = "Java is a programming language. Java is object-oriented and platform independent."
comparison = analyzer.compare_with_text(other_text)
print("Comparison results:", comparison)
