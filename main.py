import csv
import json
import re

def create_psukim_vector(bible_words, psukim):
    # we want the output to contain 1000 psukim vectors
    output = {}
    count = 0
    print(bible_words)
    for pasuk in psukim:
        pasuk_output = []
        # maybe just need to put the words in a given window size around the word "על"
        for word in pasuk.split(' '):
            print(count)
            print(word)
            if word != '':
                print(pasuk)
                print(bible_words[word])
                pasuk_output.append(bible_words[word])
        if pasuk_output != []:
            output[count] = pasuk_output
        count = count + 1

    return output

def csv_to_dict(bible_words, psukim):
    bible_words_dict = {}
    psukim_list = []
    count = 0
    for bible_word in bible_words:
        if len(bible_word) > 0:
            bible_word[1] = bible_word[1].replace('־', ' ')
            splitted_word = bible_word[1].split(" ")
            if len(splitted_word) == 1:
                bible_words_dict[bible_word[1]] = int(bible_word[0]) + count
            else:
                bible_words_dict[splitted_word[0]] = int(bible_word[0]) + count
                count = count + 1
                bible_words_dict[splitted_word[1]] = int(bible_word[0]) + count
    for row in psukim:
        row = str(row).split(",")
        pasuk = row[0]
        # cleaning the psukim
        pasuk = pasuk.replace('׃', '')
        pasuk = pasuk.replace('־', ' ')
        pasuk = pasuk.replace('[', '')
        pasuk = pasuk.replace(']', '')
        pasuk = pasuk.replace("'", '')
        pasuk = pasuk.replace("׀", '')
        pasuk = pasuk.replace("׀", '')
        pasuk = pasuk.replace("\\xa0", ' ')
        pasuk = re.sub(r"\([^()]*\)", '', pasuk)


        psukim_list.append(pasuk)

    # throw the header
    psukim_list = psukim_list[1:]


    return bible_words_dict, psukim_list

def create_csv_from_dict(output : dict):
    with open('word_embeddings_for_all_1000_al_psukim.csv', 'w') as f:
        for key in output.keys():
            f.write("%s,%s\n"%(key,output[key]))

def create_json_from_dict(output : dict):
    json_output = json.dumps(output, indent=4)
    json_file = open("word_embeddings_for_all_1000_al_psukim.json", 'w')
    json_file.write(json_output)
    json_file.close()

def print_vector_to_words(bible_words):
    file_vectors= open('word_embeddings_for_all_1000_al_psukim.csv', encoding='utf8')

    sentence = [14374,	7640,	12143,	12144,	11334,	2749,	12146,	12147,	12148,	12149,	799,	12150,	12151,	12152,	14383,	799,	12154,	 12155]
    val_list = bible_words.values()
    print(val_list)
    val_list = list(val_list)
    for w in sentence:
        print(val_list[w])


file_bible_words = open('bible_words.csv', encoding="utf8")
bible_words = csv.reader(file_bible_words)

file_psukim = open('all- on.csv', encoding='utf8')
psukim = csv.reader((file_psukim))

bible_words, psukim = csv_to_dict(bible_words=bible_words, psukim=psukim)
# base_psukim_words_vector = create_psukim_vector(bible_words=bible_words, psukim=psukim)

file_bible_words.close()
file_psukim.close()

# create_csv_from_dict(base_psukim_words_vector)
# create_json_from_dict(output=base_psukim_words_vector)
print_vector_to_words(bible_words)


