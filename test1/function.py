# Name: Chử Thị Mai
# Code: B21DCCN082
from print_functions import print_models

sent_messages_list = []
def display_message():
    print("I learn python about: variable, data type, if...else, loop, function.")

def favourite_book(title):
    print(f'One of the most my favorite books is "{title}"')

def make_shirt(size: object, mess: object = "I love Python."):
    print(f"Size: {size}\nMessage: {mess}")

def description_city(city, country = 'Viet Nam'):
    print(f"{city} is in {country}")

def city_country(city, country):
    print(f"{city}, {country}")

def make_album(artist, album_title, song=None):
    album = {"Artist": artist, "Album": album_title, "Songs": song}
    return album

def show_messages(list_mess):
    for mess in list_mess:
        print(mess)

def send_message(mess):
    global sent_messages_list
    sent_messages_list.append(mess)
    print("Was sent")

def sandwiches(**kwargs):
    size = kwargs.get("size")
    ingredient = kwargs.get("ingredient")
    normal = kwargs.get("normal")
    print(f"Size: {size}\nIngredient: {ingredient}\nNormal: {normal}")
def make_car(company, type, **car):
    car["Company"] = company
    car["Type"] = type
    return car

if __name__ == "__main__":
    #1
    display_message()
    print()
    #2
    favourite_book("")
    print()
    #3
    make_shirt("M", "I love Python")
    make_shirt(mess="I love Java", size="M")
    print()
    #4
    make_shirt(size="L")
    make_shirt(size="M")
    make_shirt(size="S", mess="Python's so great")
    print()
    #5
    description_city("Ha Noi")
    description_city("Ho Chi Minh City")
    description_city("New York", "US")
    print()
    #6
    city_country("Beijing", "China")
    city_country("San Francisco", "US")
    city_country("Paris", "France")
    print()
    #7
    make_album("Black Pink", "The Album")
    make_album("Black Pink", "Born Pink")
    make_album("Taylor Swift", "Lover")
    make_album("Taylor Swift", "Lover", 18)
    print()
    #8
    isTrue = True
    while isTrue:
        print("If input Album = None it will stop!")
        album = input("Album: ")
        artist = input("Artist: ")
        if album=='None':
            isTrue = False
            break
        make_album(artist, album)
        print()
    #9
    list_mess = ["Hello", "Hi", "Are you fine?"]
    show_messages(list_mess)
    print()
    #10 + 11
    sent_message_list = []
    print("Before send_message: ",list_mess.copy())
    send_message(list_mess)
    print("After send_message: ",list_mess)
    print()
    #12
    sandwiches(size="M", ingredient=["bacon", "tomatoes", "mayonnaise", "chicken", "lettuce"])
    sandwiches(size="M", normal=True)
    sandwiches(size="L")
    print()
    #14
    car = make_car('subaru', 'outback', color='blue', tow_package=True)
    print()
    # 15
    completed_models = []
    unprinted_designs = ['People.txt', 'Animal.txt', 'Car.txt', 'Glass.txt']
    print_models(unprinted_designs, completed_models)







