import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv'}
cities = ["chicago", "new york city", "washington"]
months = ["january", "february", "march", "april", "may", "june", "all"]
days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"]


def get_filters():
    global cities, months, days
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("Please choose a city to start (chicago, new york city, washington): ").lower()
        if city in cities:
            break
        else:
            print("please insert a valid city")
    while True:
        all_answer = input("Would you like to filter the data by month, day, or not at all? y for filter, n for all: """
                           "".lower())
        if all_answer == "n":
            month = "all"
            day = "all"
            break
        elif all_answer == "y":
            # get user input for month (all, january, february, ... , june)
            months = ["january", "february", "march", "april", "may", "june", "all"]
            while True:
                month = input("Please choose a month to proceed (all, january, february, ... , june): ").lower()
                if month in months:
                    break
                else:
                    print("please insert a valid month")

    # get user input for day of week (all, monday, tuesday, ... sunday)
            days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"]
            while True:
                day = input("Please choose a day of week to proceed (all, monday, tuesday, ... sunday): ").lower()
                if day in days:
                    break
                else:
                    print("please insert a valid day")
            break
        else:
            print("please insert a valid answer")
    print('-'*40)

    return city, month, day


def load_data(city, month, day):
    global cities, months, days, CITY_DATA
    df = pd.read_csv(CITY_DATA[city])
    df["month"] = pd.to_datetime(df["Start Time"]).dt.month
    df["day"] = pd.to_datetime(df["Start Time"]).dt.day
    if day != "all":
        day = days.index(day)+1
        df = df[df["day"] == day]
    if month != "all":
        month = months.index(month)+1
        df = df[df["month"] == month]
    df["start hour"] = pd.to_datetime(df["Start Time"]).dt.hour
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
#   print (df) """ Testing the code above """
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df.month.mode()[0]
#    print(common_month)           # testing the code
    print(f"the most common month is {common_month}")

    # display the most common day of week
    common_day = df.day.mode()[0]
    print(f"the most common day is {common_day}")
    # display the most common start hour
    common_hour = df['start hour'].mode()[0]
    print(f"the most common start hour is {common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print(f"the most common start station is {df['Start Station'].mode()[0]}")

    # display most commonly used end station
    print(f"the most common end station is {df['End Station'].mode()[0]}")
    # display most frequent combination of start station and end station trip
    df['frequent_combination'] = df['Start Station'] + " and " + df['End Station']
    most_frequent = df['frequent_combination'].mode()[0]
    #print(type(most_frequent))
    print(f"The most frequent combination is {most_frequent}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    try:
        travel_time = df["Trip Duration"]
#       print(type(travel_time)[0]) # data type testing
    # display mean travel time
        travel_time_mean = travel_time.mean()
        print(f"The mean travel time is {travel_time_mean}")
    except KeyError:
        print("Travel time data is not available in this data file.")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    try:
        user_type_count = df["User Type"].value_counts()
        print(f"user type count is: \n{user_type_count}")
    except KeyError:
        print("user type is not available in this data file.")
        pass
    # Display counts of gender
    try:
        gender = df["Gender"].value_counts()
        print(f"The Gender Count is: \n{gender}")
    except KeyError:
        print("Gender is not available in this data file.")
        pass
    # Display earliest, most recent, and most common year of birth
    try:
        most_common_birth_year = round(df["Birth Year"].mode()[0])
        most_recent_birth_year = round(df["Birth Year"].max())
        most_early_birth_year = round(df["Birth Year"].min())
        print(f"The earliest birth year is {most_early_birth_year}\nthe most """
              f"recent birth year is {most_recent_birth_year}\nthe most """
              f"common birth year is {most_common_birth_year}")
    except KeyError:
        print("Birth year data is not available in this data file.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def check_data(df):
    rows = 0
    ask = True
    while ask is True:
        check = input("Do you want to display 5 lines of data? Y/N: ").lower()
        if check == "y":
            data = df.iloc[rows:rows+5]
            rows += 5
            print(data)
        elif check == "n":
            break
        else:
            print("Please enter a valid choice.")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        check_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
