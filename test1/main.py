from function import *
from user_profile import build_profile
from print_functions import print_models

#16
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
        print("If input Album = 0 it will stop!")
        album = input("Album: ")
        if album == "0":
            isTrue = False
            continue
        artist = input("Artist: ")
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
    #13
    user_profile = build_profile('Mai', 'Chu', location='Viet Nam', field='IT')
    print(user_profile)
    print()
    #14
    car = make_car('subaru', 'outback', color='blue', tow_package=True)
    print()
    #15
    completed_models = []
    unprinted_designs = ['People.txt', 'Animal.txt', 'Car.txt', 'Glass.txt']
    print_models(unprinted_designs, completed_models)

