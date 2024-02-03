
def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  char_freq = get_char_freq(text)
  print(f"--- Begin reeport of {book_path} ---")
  print(f"{num_words} words found in the document")
  for ch_stat in convert_char_freq_to_stat_list(char_freq):
    print(f"The '{ch_stat["letter"]}' character was found {ch_stat["freq"]} in the document")

def sort_on(dict):
  return dict["freq"]

def convert_char_freq_to_stat_list(char_freq):
  lst_ch_freq = []
  for ch in char_freq:
    lst_ch_freq.append({"letter": ch, "freq": char_freq[ch]})
  lst_ch_freq.sort(reverse=True, key=sort_on)
  
  return lst_ch_freq
  

def get_char_freq(text):
  char_freq = {}
  for ch in text.lower():
    if ch.isalpha():
      if ch in char_freq:
        char_freq[ch] += 1
      else:
        char_freq[ch] = 1
  return char_freq

def get_num_words(text):
  words = text.split()
  return len(words)

def get_book_text(path):
  with open(path) as f:
    return f.read()


main()