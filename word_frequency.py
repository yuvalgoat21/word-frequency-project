def word_frequency_counter(file_name, top_n):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            
        list_of_words = text.split()
        word_dict = dict()
        
        for word in list_of_words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
                
        sorted_words = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
        
        for i in range(top_n):
            print("key: ", sorted_words[i][0], "value: ", sorted_words[i][1])
            
    except Exception as e:
        print("Error")