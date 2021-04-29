# -*- coding: utf-8 -*-
"""
poems.py

Selected poetry in various languages given as lists of lines, where each
line is a list of strings.
"""


# Composed as an example of a no-spaces "language" that only uses ASCII
# characters in case some students have rendering issues with Chinese or
# Japanese.
variables = {
    "VariableNames": [
        [ "snake", "_", "case", "_", "slithers", "_", "quietly", "," ],
        [ "SCREAMING", "_", "SNAKE", "_", "CASE", "_", "IS", "_", "LOUD", "," ],
        [ "camel", "Case", "Has", "Humps", "," ],
        [ "kebab", "-", "case", "-", "skewers", "-", "words", "." ],
        [ "justpleasedontnameyourvariableslikethis", "!" ],
    ]
}

# Original Haiku (in Katakana/Hiragana) by Matsuo Bashō
shortLegs = {
    "Japanese": [
        [ "さみだれ", "に" ],
        [ "つる", "の", "あし" ],
        [ "みじかく", "なれり" ]
    ],
    # The same poem transliterated into Latin characters
    "JapaneseTransliterated": [
        [ "samidare", "ni" ],
        [ "tsuru", "no", "ashi" ],
        [ "mijikaku", "nareri" ]
    ],
    # Translation into English in "Basho's Haiku: Selected Poems of
    # Matsuo Basho":
    # https://ebookcentral.proquest.com/lib/well/reader.action?docID=3408445
    "English": [
        [ "in", "summer", "rains" ],
        [ "the", "crane's", "legs" ],
        [ "become", "short" ]
    ]
}


# "Up in the Morning Early" by Robert Burns
# https://www.scottishpoetrylibrary.org.uk/poem/morning-early/
upEarly = {
    # Actually this poem is somewhere between English and Scots
    "English": [
        [ "Cauld", "blaws", "the", "wind", "frae", "east", "to", "west", "," ],
        [ "The", "drift", "is", "driving", "sairly", ";" ],
        [ "Sae", "loud", "and", "shrill’s", "I", "hear", "the", "blast", "," ],
        [ "I’m", "sure", "it’s", "winter", "fairly", "." ],
        [],
        [ "Up", "in", "the", "morning’s", "no", "for", "me", "," ],
        [ "Up", "in", "the", "morning", "early", ";" ],
        [ "When", "a’", "the", "hills", "are", "cover’d", "wi’", "snaw", "," ],
        [ "I’m", "sure", "its", "winter", "fairly", "." ],
        [],
        [ "The", "birds", "sit", "chittering", "in", "the", "thorn", "," ],
        [ "A’", "day", "they", "fare", "but", "sparely", ";" ],
        [ "And", "lang’s", "the", "night", "frae", "e’en", "to", "morn", "," ],
        [ "I’m", "sure", "it’s", "winter", "fairly", "." ],
        [],
        [ "Up", "in", "the", "morning’s", "no", "for", "me", "," ],
        [ "Up", "in", "the", "morning", "early", ";" ],
        [ "When", "a’", "the", "hills", "are", "cover’d", "wi’", "snaw", "," ],
        [ "I’m", "sure", "its", "winter", "fairly", "." ],
    ]
}

# "Über allen Gipfeln Ist Ruh" by Johann Wolfgang Von Goethe
# https://de.wikipedia.org/wiki/Wandrers_Nachtlied
eveningRest = {
    "German": [
        [ "Über", "allen", "Gipfeln" ],
        [ "Ist", "Ruh'", "," ],
        [ "In", "allen", "Wipfeln" ],
        [ "Spürest", "Du" ],
        [ "Kaum", "einen", "Hauch", ";" ],
        [ "Die", "Vögelein", "schweigen", "im", "Walde", "." ],
        [ "Warte", "nur", "!", "Balde" ],
        [ "Ruhest", "du", "auch", "." ],
    ],
    # English translation as "Song of the Traveller at Evening" found here:
    # https://www.poetryfoundation.org/poetrymagazine/browse?contentId=31642
    "English": [
        [ "Over", "all", "the", "hills", "now", "," ],
        [ "Repose", "." ],
        [ "In", "all", "the", "trees", "now", ],
        [ "Shows" ],
        [ "Barely", "a", "breath", ".", "Birds", "are", "through" ],
        [ "That", "sang", "in", "their", "wood", "to", "the", "west", "." ],
        [ "Only", "wait", ",", "traveller", ".", "Rest" ],
        [ "Soon", "for", "you", "too", "." ],
    ]
}


# "咏鹅" (Yǒng É) by 骆宾王 (Luòbīnwáng) (at age 7)
# Source: Ying Su
theGoose = {
    "Chinese": [
        [ "鹅", "鹅", "鹅" ],
        [ "曲", "项", "向", "天", "歌" ],
        [ "白", "毛", "浮", "绿", "水" ],
        [ "红", "掌", "拨", "清", "波" ],
    ],
    "ChineseTransliterated": [
        [ "É", "é", "é" ],
        [ "Qǔ", "xiàng", "xiàng", "tiān", "gē" ],
        [ "Bái", "máo", "fú", "lǜ", "shuǐ" ],
        [ "Hóng", "zhǎng", "bō", "qīng", "bō" ],
    ],
    # English translation as "To Ganders" found here:
    # http://tcfl.tingroom.com/2016/01/12030.html
    "English": [
        [ "Goose", ",", "goose", ",", "goose" ],
        [ "Sing", "to", "the", "sky", "with", "necks", "incurving", "." ],
        [ "White", "feathers", "afloat", "on", "verdant", "waters", "," ],
        [ "Orange", "palmate", "feet", "push", "the", "clear", "water", "." ]
    ]
}


# "Las Condiciones del Pájaro Solitario" by San Juan de la Cruz
# https://stevensametz.com/composer/works/info/luz-y-amor-light-and-love/
solitaryBird = {
    "Spanish": [
        [ "Las", "condiciones", "del", "pájaro", "solitario", "son", "cinco", "." ],
        [ "La", "primera,", "que", "se", "va", "a", "lo", "más", "alto", ";" ],
        [ "la", "segunda", ",", "que", "no", "sufre", "compañía", ",", "aunque", "sea", "de", "su", "naturaleza", ";" ],
        [ "la", "tercera", ",", "que", "pone", "el", "pico", "al", "aire", ";" ],
        [ "la", "cuarta", ",", "que", "no", "tiene", "determinado", "color", ";" ],
        [ "la", "quinta", ",", "que", "canta", "suavemente", "." ],
    ],
    # Translation to English as "The Conditions of a Solitary Bird" (same source)
    "English": [
        [ "The", "conditions", "of", "a", "solitary", "bird", "are", "five", ":" ],
        [ "first", ",", "that", "it", "seeks", "the", "highest", "place", ";" ],
        [ "second", ",", "that", "it", "does", "not", "want", "company", ",",
         "not", "even", "of", "its", "own", "kind",
         ";" ],
        [ "third", ",", "that", "it", "aims", "its", "beak", "to", "the", "wind", ";" ],
        [ "fourth", ",", "that", "it", "has", "no", "definite", "color", ";" ],
        [ "fifth", ",", "that", "it", "sings", "very", "sweetly", "." ],
    ]
}

# "Caged Bird" by Maya Angelou
# https://www.poetryfoundation.org/poems/48989/caged-bird
cagedBird = {
    "English": [
        [ "A", "free", "bird", "leaps" ],
        [ "on", "the", "back", "of", "the", "wind" ],
        [ "and", "floats", "downstream" ],
        [ "till", "the", "current", "ends" ],
        [ "and", "dips", "his", "wing" ],
        [ "in", "the", "orange", "sun", "rays" ],
        [ "and", "dares", "to", "claim", "the", "sky", "." ],
        [],
        [ "But", "a", "bird", "that", "stalks" ],
        [ "down", "his", "narrow", "cage" ],
        [ "can", "seldom", "see", "through" ],
        [ "his", "bars", "of", "rage" ],
        [ "his", "wings", "are", "clipped", "and" ],
        [ "his", "feet", "are", "tied" ],
        [ "so", "he", "opens", "his", "throat", "to", "sing", "." ],
        [],
        [ "The", "caged", "bird", "sings" ],
        [ "with", "a", "fearful", "trill" ],
        [ "of", "things", "unknown" ],
        [ "but", "longed", "for", "still" ],
        [ "and", "his", "tune", "is", "heard" ],
        [ "on", "the", "distant", "hill" ],
        [ "for", "the", "caged", "bird" ],
        [ "sings", "of", "freedom", "." ],
        [],
        [ "The", "free", "bird", "thinks", "of", "another", "breeze" ],
        [ "and", "the", "trade", "winds", "soft", "through", "the", "sighing", "trees" ],
        [ "and", "the", "fat", "worms", "waiting", "on", "a", "dawn", "bright", "lawn" ],
        [ "and", "he", "names", "the", "sky", "his", "own" ],
        [],
        [ "But", "a", "caged", "bird", "stands", "on", "the", "grave", "of", "dreams" ],
        [ "his", "shadow", "shouts", "on", "a", "nightmare", "scream" ],
        [ "his", "wings", "are", "clipped", "and", "his", "feet", "are", "tied" ],
        [ "so", "he", "opens", "his", "throat", "to", "sing", "." ],
        [],
        [ "The", "caged", "bird", "sings" ],
        [ "with", "a", "fearful", "trill" ],
        [ "of", "things", "unknown" ],
        [ "but", "longed", "for", "still" ],
        [ "and", "his", "tune", "is", "heard" ],
        [ "on", "the", "distant", "hill" ],
        [ "for", "the", "caged", "bird" ],
        [ "sings", "of", "freedom", "." ],
    ]
}


# A single list holding all of the poems
ALL_POEMS = [
    variables,
    shortLegs,
    upEarly,
    eveningRest,
    theGoose,
    solitaryBird,
    cagedBird,
]
