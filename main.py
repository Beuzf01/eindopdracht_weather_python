from login import *
from weather import *
from suntimes import *


def main():
    while True:
        # asking the user how they want to continue
        account_choice = input("Welcome! Do you:\n"
                           "1. Want to log in?\n"
                           "2. Want to sign up?\n"
                            "3. Want to continue as guest?\n"
                           "Your choice: ")

        # processing the input and asking the user to perform the according actions
        if account_choice == "1" or "log in" in account_choice:
            login_success = login()
            if login_success:
                break
            else:
                continue

        elif account_choice == "2" or "sign up" in account_choice:
            signup()
            break
        elif account_choice == "3" or "guest" in account_choice:
            guest_signin()
            break
        else:
            print("Sorry, we didnt understand that")
            continue

    while True:
        print("_"*40)
        weather_menu = input("How can we help you today?\n"
                             "1. Display weather forecast in a selected place for up to 5 days\n"
                             "2. Display sunrise and sunset times of the current day in a selected place\n"
                             "Choice: ")
        if weather_menu == "1":
            # getting input from user and processing the city into coördinates using geo-API
            city, cnt = userinput()
            loc_status, location_data = locationfetch(city)
            try:
                lat, lon = location_processing(loc_status, location_data)
                if lat and lon:
                    # using found coördinates to fetch the weather in that place and give the user output
                    try:
                        weather_status, location_weather = weather_fetch(lat, lon)
                        weather_data = weather_processing(weather_status, location_weather, cnt, city)
                    except Exception as e:
                        print("Sorry, we have trouble finding the weather-forecast")
                        continue
            except Exception as e:
                print("Sorry, we couldn't find the place you are looking for")
                continue

        elif weather_menu == "2":
            print("_" * 40)
            city = input("Which city would you like to know the sunrise and sunset of? ")
            try:
                loc_status, location_data = locationfetch(city)
                lat, lon = location_processing(loc_status, location_data)
                if lat and lon:
                    sun_data = suntimes_fetch(lat, lon)
                else:
                    sun_data = None
                if sun_data:
                    try:
                        print("_" * 40)
                        sundata_processing(sun_data)
                    except Exception as e:
                        print("Sorry, we have trouble finding the sun-times")
                        continue
                print("_" * 40)
            except Exception as e:
                print("Sorry, we couldn't find the place you are looking for")
                continue

        else:
            print("We didnt quite understand, try again")
            continue
        # asking the user whether they want to use the application again
        while True:
            again = input("Would you like to do something else? (y/n) ").strip()
            if again.upper() == "Y" or again.upper() == "YES":
                print("_" * 40)
                break
            if again.upper() == "N" or again.upper() == "NO":
                print("_" * 40)
                print("Have a nice day!")
                print("_" * 40)
                exit()
            else:
                print("_" * 40)
                print("Invalid input")
                print("_" * 40)
                continue


if __name__ == '__main__':
    main()