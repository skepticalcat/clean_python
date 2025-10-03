import math

def find_largest_in_csv():
    try:
        read_handler = open("inputdata.csv", "r")

        file_contents = read_handler.read()
        file_contents = file_contents.split(",\n")

        for i in range(len(file_contents)):
            if not file_contents[i].isdigit():
                print("Oh no! There is a value in there that is not a digit, lets clean that")

        cleaned_file_contents = []
        for i in range(len(file_contents)):
            if file_contents[i].isdigit():
                cleaned_file_contents.append(int(file_contents[i]))

        largest = -math.inf
        for i in range(len(cleaned_file_contents)):
            if cleaned_file_contents[i] > largest:
                largest = cleaned_file_contents[i]
        read_handler.close()
        return largest

    except:
        read_handler.close()
        print("Oh no! Error")
        raise


print(find_largest_in_csv())