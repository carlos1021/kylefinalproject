from nltk.corpus import wordnet as wn

def get_synonyms(word):
    synonyms = []
    for synsets in wn.synsets(word):
        for lemma in synsets.lemmas():
            lemma_name = lemma.name().replace('_', ' ')
            synonyms.append(lemma_name)
    synonyms = list(set(synonyms))
    try:
        synonyms.remove(word)
    except:
        pass
    return synonyms

def recommend_synonym(word):
    synonyms = get_synonyms(word)
    html_output = ""
    if len(synonyms) > 0:
        synsets = wn.synsets(word)
        html_output += f"<strong>Definition(s) for {word}:</strong><br>"
        for synset in synsets:
            definition = synset.definition().capitalize()
            html_output += f"{definition}<br>"
        html_output += "<br><strong>Synonym(s) for " + word + ":</strong><ul style='margin-left: 20px;'>"
        for synonym in synonyms:
            html_output += f"<li>{synonym}</li>"
        html_output += "</ul>"
    else:
        html_output += f"No synonyms found for '{word}'."
    return html_output

if __name__ == "__main__":
    import sys
    word = sys.argv[1] 
    html_result = recommend_synonym(word)
    
    print(html_result)
