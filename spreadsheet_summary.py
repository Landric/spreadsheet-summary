import csv
from ast import literal_eval
import random
import numpy as np

def summarise_columns():


    headers = []
    columns = {}

    with open('data.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:

            if not headers:
                headers = row
                for header in headers:
                    columns[header] = []
            else:
                for i in range(len(headers)):
                    columns[headers[i]].append(row[i])

    summary = ""
    for header in headers:
        summary += summarise_column(header, columns[header]) + "\n\n"

    return summary




def summarise_column(header, column):

    summary = "There is a column called " + header + ". It appears to contain " + column_data(column)


    return summary


def column_data(column):


    def column_is_str(column, summary):
        pass
    def column_is_numeric(column, summary):
        pass
    def column_is_bool(column, summary):
        pass

    summary = ""
    if get_type(column[0]) == str:

        if column[0].lower in ["true", "false", "pass", "fail"]:
            summary += "boolean data, "

            #true_percent = (len([t for t in column if bool(t)]) / float(len(column))) * 100

            summary += "with {0}%% true and {1}%% false".format("%.2f" % true_percent, "%.2f" % 100-true_percent)

        else:
            summary += "textual data, "

            if few_values(column, 5):
                summary += few_values(column)
            else:
                summary += "including: "
                examples = []
                while len(examples) < 5:
                    example = column.pop(random.randint(0, len(column))).strip()
                    if example not in examples:
                        examples.append(example)
                summary += ", ".join("\"{0}\"".format(example) for example in examples)


    elif get_type(column[0]) == int or get_type(column[0]) == float:
        if get_type(column[0]) == int:
            column = np.array(column).astype(np.int)
        else:
            column = np.array(column).astype(np.float)

        summary += "numeric data, "
        
        if few_values(column):
            summary += few_values(column)
        else:
            summary += "with minimum \"{0}\", mean \"{1}\" and max \"{2}\"".format(min(column), "%.2f" % np.mean(column), max(column))
    


    elif get_type(column[0]) == bool:
        summary += "boolean data, "

        true_percent = (len([t for t in column if bool(t)]) / float(len(column))) * 100

        summary += "with {0}%% true and {1}%% false".format("%.2f" % true_percent, "%.2f" % 100-true_percent)



    # if (column == sorted(column) or column == sorted(column, reverse=True)):
    #     return "an ID."

    return summary


def few_values(column, few = 10):
    if len(set(column)) == 1:
        return "all with value \"{0}\"".format(column[0])
    elif len(set(column)) < few:
        return "with values of " + ", ".join("\"{0}\"".format(s) for s in set(column))


def get_type(input_data):
    try:
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):
        # A string, so return str
        return str


if __name__ == "__main__":
    print summarise_columns()
