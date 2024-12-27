# Early version. Supports only hardcoded language strings.

class I18N:
    def __init__(self, language_code):
        if language_code == "en":
            self.load_text_in_english()
        elif language_code == "tr":
            self.load_text_in_turkish()
        else:
            raise NotImplementedError("Unsupported language.")

    def load_text_in_english(self):
        self.title = "Week 12"
        self.fname = "First Name"
        self.lname = "Last Name"
        self.grade = "Grade"
        self.save = "Save Grade"

    def load_text_in_turkish(self):
        self.title = "Hafta 12"
        self.fname = "Ad"
        self.lname = "Soyad"
        self.grade = "Not"
        self.save = "Notu Kaydet"
