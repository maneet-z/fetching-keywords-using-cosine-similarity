


import math
import os


def get_file_data(f_name):  # function to get the file data from from where we will get whole book data
    test_exist = os.path.exists(f_name)  # checks whether the file exists or not
    # print(test_exist)
    if test_exist == False:
        print('File is not present in the directory')  # if file doesnt exist it will show an error message
        return None
    else:
        file = open(f_name, 'r')  # openingthe file in the read mode
        data = file.readlines()  # reading all the lines from the file
        file.close()  # closing the file from the cache

        str_data = ''  # intializing variable
        for x in data:  # getting the data from the file to the intialized variable str_data
            str_data += x
        str_check_file = str_data.split('\n')  # Splitting data with the new line
        temp_line = str_check_file[0].split(' ')  # splitting the first line with the spaces to check the file condition if the file is correct or not
        lenght_of_data = len(temp_line)  # getting the length of the temporary line
        if lenght_of_data < 1:  # if it is less than 2 then the file is wrong
            print('Please check the file you have uploaded')
            return None
        else:
            str_data = str_data.replace('?', '.')  # Replacing  ? to .
            str_data = str_data.replace('!', '.')  # replacing ! to .
            split_data_fullsop = []  # intializing list
            split_data_fullsop = str_data.split('.')  # now spliting data with .
            return split_data_fullsop  # returning all the splited data in the list


def get_test_words(test_word_file):
    test_exist = os.path.exists(test_word_file)  # checking variable if the file exists or not
    # print(test_exist)
    if test_exist == False:  # if file doesnt exists it will show the error message
        print('File is not present in the directory')
        return None  # returning none if the file doesnt exists
    else:
        test_words = []
        file = open(test_word_file, 'r')
        data = file.readlines()
        temp2 = ''
        for temp in data:
            temp2 += temp
        str_check_file = temp2.split('\n')
        temp_line = str_check_file[0].split(' ')
        lenght_of_data = len(temp_line)
        if lenght_of_data > 1:  # if the test word file has more than 1 word in the file then it will show an error that it is the wrong file
            print('Please check the file you have uploaded')
            return None  # hence it will return None
        else:
            for data2 in data:  # getting all the data from the  tests word file i.e. all the profiles
                data2 = data2.rstrip()  # stripping all the data
                test_words.append(data2)  # appending it to the new list
            file.close()  # closing the file from the cache
            return test_words  # returning the list


def get_common_words(common_word_file):
    common_words = {}  # initializing the dictionary
    file = open(common_word_file, 'r')  # getting common words from the common word file
    data = file.readlines()
    for words in data:
        words = words.rstrip()
        common_words[words] = 0
    return common_words  # returning the list of common word


def get_word_frequency(string_data_clean, test_words, common_words):
    string_data_clean = string_data_clean.lower()  # Converting all the data to the lower case
    string_full_stops = []  #
    string_full_stops = string_data_clean.split('.')  # splitting data with the full stops
    words_in_one_line = []
    word_count = {'': {'': 0}}  # intializing word count dictionary variable
    len_of_strings = len(string_full_stops)  # getting the length of the string
    count = 0
    for x in range(
            len(test_words)):  # this loop will work till the number of lines which were splitted by the full stops
        count_profile = 0  # profile count variable
        word_count[test_words[x]] = {}
        for i in range(len_of_strings):
            words = test_words[x]
            words_in_one_line = string_full_stops[i].split(' ')  # all the words are splitted by the space
            lst_line_word = []  # list of the words in the line
            if words in words_in_one_line:
                count_profile += 1  # it will count the number of profile present in the word
                for diff_word in words_in_one_line:
                    if diff_word in common_words:  # if the word is present in the common word it will ignore it
                        flag = 0
                    else:
                        if diff_word == '':  # if it is blank space it will ignore it
                            flag = 0
                        else:
                            if diff_word == test_words[x]:  # if the word is the profile word it will ignore it
                                flag = 0
                            else:
                                if diff_word in word_count[test_words[
                                    x]] and diff_word not in lst_line_word:  # if the word has already in the dictionary for the same line then it wont add the count
                                    count = word_count[test_words[x]][diff_word]
                                    count = count + 1  # if it is  from the different line then it will add the count
                                    word_count[test_words[x]][diff_word] = count
                                else:
                                    lst_line_word.append(
                                        diff_word)  # appending to check the word from the specific line
                                    count += 1
                                    word_count[test_words[x]].update({diff_word: count})  # updating the dictionary
                                count = 0

    file = open('testingfile.txt','w',encoding='UTF8')
    tempwords = []
    for data in word_count:
        for words in word_count[data]:
            if words in tempwords:
                flag=1
            else:
                tempwords.append(words)

    for words in tempwords:
        file.write(str(words) + '\n')

    file.close()
    # for data in word_count:
    #
    #     if len(word_count[data]) > 1:
    #         file.write(data)
    #         file.write(str(word_count[data]))
    #         file.write('==================\n\n')
    # file.close()
    return word_count  # returing the dictionary


def clean_data(split_data_fullstop):  # This function will check if the single character is in the punctuation
    # then it will replace that to the blank space and the last while loop will remove all the extra blank places
    # Also it will check if it has two consecutive '-' then it will make it space
    punctuation = [',', '\'', '\"', ':', ';', '(', ')', '[', ']', '\n', '_']  # creating the punctuation list
    temporary_string = ''
    for x in range(len(split_data_fullstop) - 1):
        length = len(split_data_fullstop[x])
        for y in range(length):
            if split_data_fullstop[x][y] == '-':
                if split_data_fullstop[x][y - 1] == '-':
                    temporary_string += ' '
                else:
                    if split_data_fullstop[x][y + 1] == '-':
                        temporary_string += ' '
                    else:
                        temporary_string += split_data_fullstop[x][y]
            else:
                if split_data_fullstop[x][y] in punctuation:
                    temporary_string += ' '
                else:
                    temporary_string += split_data_fullstop[x][y]
        temporary_string += '.'
    while '  ' in temporary_string:
        temporary_string = temporary_string.replace('  ', ' ')
    file = open('temporary_file', 'w')
    file.write(temporary_string)
    file.close()
    return temporary_string


def profile_calculation(profile_count, test_words):  # This is the COSINE ALGORITHM function to find the profile count
    final_data_profile = []
    length_of_test_words = len(test_words)
    pq = 0
    count_denom_p = 0
    count_denom_q = 0
    for cnt in range(1, length_of_test_words):
        for word in profile_count[test_words[0]]:
            if word in profile_count[test_words[cnt]]:
                pq += (int(profile_count[test_words[cnt]][word]) * int(
                    profile_count[test_words[0]][word]))  # Counting the numerator with the common P and different Q
        for countwords in profile_count[test_words[0]]:
            count_denom_p += (int(profile_count[test_words[0]][countwords]) ** 2)  # Denominator for P
        for countwords in profile_count[test_words[cnt]]:
            count_denom_q += (int(profile_count[test_words[cnt]][countwords]) ** 2)  # Denominator for Q
        # count_denom_p = count_denom_p * count_denom_p

        # count_denom_q = count_denom_q* count_denom_q
        final_denom = math.sqrt((count_denom_p * count_denom_q))
        if final_denom != 0:
            final_data_profile.append(
                [test_words[cnt], round(pq / final_denom, 3)])  # Appending the count to the final list
        else:
            final_data_profile.append([test_words[cnt], 0])
        count_denom_p = 0
        count_denom_q = 0
        pq = 0
        final_denom = 0

    return sorted(final_data_profile, key=lambda l: l[1], reverse=True)  # Returning the Sorted List


def main(f_name, test_word_file, common_word_file=None):
    if f_name == '' or test_word_file == '':
        print('Please insert the File to read data from ')  # Checking if the file name is passed or not
    else:

        start_time = os.times()
        split_data_fullstop = get_file_data(f_name)
        if split_data_fullstop == None:
            print(
                'File cannot be proccessed because of the incorrect file upload')  # Checking if the Data sent is none or not
        else:
            test_words = get_test_words(test_word_file)
            if test_words == None:
                print(
                    'File cannot be proccessed because of the incorrect file upload')  # Checking if the Test file is passed or not
            else:
                string_data_clean = clean_data(split_data_fullstop)
                if common_word_file == None:
                    print('No common words file submitted')  # Checking if the Common words file was sent or not
                    profile_count = get_word_frequency(string_data_clean, test_words, '')
                else:
                    common_words = get_common_words(common_word_file)
                    profile_count = get_word_frequency(string_data_clean, test_words, common_words)
                final_data = profile_calculation(profile_count, test_words)
                for data in final_data:
                    print(data)  # Printing the data in the sorted order
                #print('Synonym for the word', test_words[0], '  is ', final_data[0][0])  # Printing the final Synonym
                finish_time = os.times()
                print("\nExecution Times - User: {0:0.2f} Sys: {1:0.2f}".format(finish_time[0] - start_time[0],
                                                                                finish_time[1] - start_time[
                                                                                    1]))  # ime for the project to run


main('TCGA-XC-AA0X.B22BD117-8DF0-47FF-BE25-9FE2DA916DB6.txt','profile.txt','common.txt')
