from lingua import Language, LanguageDetectorBuilder

languages = [Language.ENGLISH, Language.GERMAN]
detector = LanguageDetectorBuilder.from_languages(*languages).build()

def getLangData(text):
    confidence = detector.compute_language_confidence_values(text)[0]
    isEnglish = confidence.language == Language.ENGLISH
    response = {
        "isEnglish": isEnglish,
        "language": confidence.language.name,
        "confidence": confidence.value,
    }
    print(response)
    return response