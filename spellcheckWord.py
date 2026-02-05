# Project: Advanced Spell Checker (B.Tech Portfolio)
# Logic: Hybrid approach using pyspellchecker + Custom Rule Mapping

from spellchecker import SpellChecker

class EnhancedSpellChecker:
    def __init__(self):
        # Initialize the spellchecker library
        self.spell = SpellChecker()
        
        # Custom dictionary for slang, abbreviations, or tech terms
        self.custom_map = {
            "pythn": "Python",
            "btech": "B.Tech",
            "clg": "College",
            "js": "JavaScript",
            "ai": "AI",
            "ml": "ML"
        }

    def correct_text(self, text):
        """
        Processes input text:
        1. Applies custom corrections first.
        2. Uses library corrections for general spelling mistakes.
        """
        words = text.split()
        corrected_words = []

        for word in words:
            # Remove punctuation for checking
            clean_word = word.lower().strip(",.!?")

            # Apply custom mapping first
            if clean_word in self.custom_map:
                corrected = self.custom_map[clean_word]
                print(f"[Custom Correction] '{word}' -> '{corrected}'")
                corrected_words.append(corrected)
            
            # Use spellchecker library for general corrections
            else:
                corrected = self.spell.correction(clean_word)
                if corrected and corrected != clean_word:
                    print(f"[SpellChecker] '{word}' -> '{corrected}'")
                    corrected_words.append(corrected)
                else:
                    corrected_words.append(word)

        return " ".join(corrected_words)

    def run(self):
        print("=== Welcome to Enhanced Spell Checker v1.0 ===")
        print("Type 'quit' to exit the application.\n")
        
        while True:
            user_input = input("Enter text: ")
            if user_input.lower() == 'quit':
                print("Thank you for using the Spell Checker! Keep coding!")
                break
            
            final_text = self.correct_text(user_input)
            print(f"\nCorrected Output: {final_text}\n")


if __name__ == "__main__":
    app = EnhancedSpellChecker()
    app.run()
