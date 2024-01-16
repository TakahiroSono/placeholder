import sys

NAME_KEY = "%NAME%"
AGE_KEY = "%AGE%"
HOBBY_KEY = "%HOBBY%"

def prohibitionWord(text):
    return text.replace("犬", "※").replace("イヌ", "※※").replace("dog", "※※※").replace("DOG", "※※※")

def replaceText(baseKey, baseText, targetKey1, targetText1, targetKey2, targetText2):
    if (targetKey1 in baseText and targetKey2 in baseText):
        return baseText.replace(
            targetKey1, targetText1.replace(targetKey2, targetText2.replace(targetKey1, "")).replace(baseKey, "")
        ).replace(targetKey2, targetText2.replace(targetKey1, targetText1.replace(targetKey2, "")).replace(baseKey, ""))
    if (targetKey1 in baseText):
        return baseText.replace(targetKey1, targetText1.replace(targetKey2, targetText2.replace(targetKey1, "")).replace(baseKey, ""))

    if (targetKey2 in baseText):
        return baseText.replace(targetKey2, targetText2.replace(targetKey1, targetText1.replace(targetKey2, "")).replace(baseKey, ""))
    return baseText

errMessage = ""
name = prohibitionWord(sys.argv[1].removeprefix("NAME="))
if (len(name) == 0 or len(name) > 20):
    errMessage = "NAME は１文字以上２０文字以下で入力してください。"

age = prohibitionWord(sys.argv[2].removeprefix("AGE="))
if (not age.isdecimal() or age < "18" or age > "65"):
    errMessage += "\n" if errMessage != "" else ""
    errMessage += "AGE は18〜65の範囲の整数で入力してください。"

hobby = prohibitionWord(sys.argv[3].removeprefix("HOBBY=") if len(sys.argv) == 4 else "無趣味")

if (errMessage != ""):
    print(errMessage)
    exit()

nameMessage = f"私は{replaceText(NAME_KEY, name, AGE_KEY, age, HOBBY_KEY, hobby)}です。"
ageMessage = f"今年で{age}になります。"
hobbyMessage = f"趣味は{replaceText(HOBBY_KEY, hobby, NAME_KEY, name, AGE_KEY, age)}です。"
template = f"こんにちは。{nameMessage}\n{ageMessage}{hobbyMessage}"

print(template)
