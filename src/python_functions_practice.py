

def return_10():
    return 10

def add(number1, number2):
    return number1+number2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(num_1, num_2):
    return num_1/num_2

def length_of_string(sentence):
    return len(sentence)

def join_string(string_1, string_2):
    return f'{string_1}{string_2}'

def add_string_as_number(num_1, num_2):
    return int(num_1) + int(num_2)

calender = {
        1 : {
            "long": "January",
            "short" : "Jan"
        },
        2 : {
            "long" : "February",
            "short" : "Feb"
        },
        3 : {
            "long" :"March",
            "short" : "Mar"
        },
        4 : {
            "long" : "April",
            "short" : "Apr"
        },
        5 : {
            "long" : "May",
            "short" : "May"
        },
        6 : {
            "long" : "June",
            "short" : "Jun"
        } ,
        7 : {
            "long" : "July",
            "short" : "Jul"
        },
        8 : {
            "long" :"August",
            "short" : "Aug"
        },
        9 : {
            "long" : "September",
            "short" : "Sep"
        },
        10 : {
            "long" :"October",
            "short" : "Oct"
        },
        11 : {
            "long" : "November",
            "short" : "Nov"
        },
        12 : {
            "long" : "December",
            "short" : "Dec"
        } 
    }


def number_to_full_month_name(number):
    return calender[number]["long"]

def number_to_short_month_name(number):
    return calender[number]["short"]

def volume_of_cube(height, width, depth):
    return height * width * depth

def reverse_string(text):
    return text[::-1]

def fahrenheit_to_celsius(farenheit):
    return (farenheit -32) * (5/9)