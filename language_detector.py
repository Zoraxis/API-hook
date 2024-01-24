from lingua import Language, LanguageDetectorBuilder
from settings import getEnv

languages = [Language.ENGLISH, Language.GERMAN]
detector = LanguageDetectorBuilder.from_all_languages().with_preloaded_language_models().build()
# detector = LanguageDetectorBuilder.from_languages(*languages).with_preloaded_language_models().build()

# get settings
min_confidence = float(getEnv("LANG_MIN_CONFIDENCE"))
min_percent = float(getEnv("LANG_MIN_PERCENT"))
min_length = int(getEnv("LANG_MIN_LENGTH"))
allowed_languages = getEnv("LANG_ALLOWED_LIST").split()
deep_filter = getEnv("LANG_DEEP")

def isLanguageFalse(text):
    # if less than 30 words, return false
    words = len(text.split())
    if words < min_length:
        return False
    
    # detect language
    langData = getLangData(text)
    print(langData)

    #check confidence level
    if langData["confidence"] < min_confidence:
        return False
    
    # check if language is allowed
    if not langData["isNotAllowedLanguage"]:
        return False
    
    if deep_filter:
        if not isPercentReached(text):
            return False
    
    # if language all checks passed - return true
    return True

def isPercentReached(text):
    disallowedPercent = 0

    # iterate over all detected languages
    for result in detector.detect_multiple_languages_of(text):
        # calculate the percentage of the text that is in the language
        cutLength = result.end_index - result.start_index
        cutPercent = cutLength / len(text)
        
        # if language is not allowed - add to disallowed percent
        if result.language.name not in allowed_languages:
            disallowedPercent += cutPercent
            
    # true returned if disallowed percent is higher than min_percent
    return disallowedPercent >= min_percent

def getLangData(text):
    # get the most likely language
    confidence = detector.compute_language_confidence_values(text)[0]
    # check if language is not allowed
    isNotAllowedLanguage = True
    for lang in allowed_languages:
        if confidence.language.name == lang:
            isNotAllowedLanguage = False
    #form response
    response = {
        "isNotAllowedLanguage": isNotAllowedLanguage,
        "language": confidence.language.name,
        "confidence": confidence.value,
    }

    return response