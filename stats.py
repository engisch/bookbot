def get_num_words(text):
    return len(text.split())

def get_letter_count(text):
    letter_count={}
    for letter in text:
        if letter in letter_count:
            letter_count[letter]+=1
        else:
            letter_count[letter]=1
    return letter_count

def sort_on(items):
    return items["num"]

def sort_dict(dict_list):
    new_dict=[]
    for entry in dict_list:
        new_dict.append({"char": entry, "num": dict_list[entry]})
    new_dict.sort(reverse=True, key=sort_on)
    return new_dict