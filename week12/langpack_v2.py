# Supports external language files.

import glob


class I18N:
    def __init__(self, language_code):
        if language_code in self.get_available_languages():
            self.translations = self.load_data_from_file(language_code)
        else:
            raise NotImplementedError("Unsupported language. Add missing language file.")

    @staticmethod
    def get_available_languages():
        # Language file naming format: data_<language code>.lng
        # Example: data_tr.lng, data_en.lng, ...
        language_files = glob.glob("*.lng")
        language_codes = []

        for f in language_files:
            language_code = f.replace("data_", "").replace(".lng", "")
            language_codes.append(language_code)

        return language_codes

    @staticmethod
    def load_data_from_file(language_code):
        language_file = f"data_{language_code}.lng"
        language_data = {}
        try:
            with open(language_file, encoding="utf-8") as f:
                for line in f:
                    (key, val) = line.strip().split("=")
                    language_data[key] = val
        except FileNotFoundError:
            raise ValueError("Language file not found.")

        return language_data

    @staticmethod
    def get_language_name(language_code):
        language_file = f"data_{language_code}.lng"
        try:
            with open(language_file, encoding="utf-8") as f:
                for line in f:
                    (key, val) = line.strip().split("=")
                    if key == "language":
                        return val

                # If the loop completes without finding the "language" key.
                raise ValueError("The language key was not found.")
        except FileNotFoundError:
            raise ValueError("Language file not found.")