from lingua import Language, LanguageDetectorBuilder

languages = [Language.ENGLISH, Language.GERMAN]
detector = LanguageDetectorBuilder.from_languages(*languages).build()

confidence_min = 0.7

def isLanguageFalse(text):
    # if less than 30 words, return false
    words = len(text.split())
    print(len)
    if words < 30:
        return False
    
    # detect language
    langData = getLangData(text)
    print(langData)

    # if language is not english, return true
    if langData["confidence"] > confidence_min and not langData["isEnglish"]:
        return True
    
    return False

def getLangData(text):
    # get the most likely language
    confidence = detector.compute_language_confidence_values(text)[0]
    # check if language is english
    isEnglish = confidence.language == Language.ENGLISH
    response = {
        "isEnglish": isEnglish,
        "language": confidence.language.name,
        "confidence": confidence.value,
    }

    return response