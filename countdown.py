#! /usr/bin/python

import time

def countdown(finish):
    """
    Runs a while loop and counts down per second till the present time reaches the parameter finish.

    Assumes argument finish is an Epoch time from the user in seconds and greater than the present.

    Returns the number of iterations completed while doing the countdown
    """

    printed_time = 0
    present_time = int(time.time())
    i = 0

    while present_time <= finish:

        if printed_time != present_time:
            print int(finish - present_time)
            printed_time = int((present_time))
            time.sleep(0.9)

        present_time = int(time.time())
        i += 1

    return i


# a countdown with less iterations, but potentially less accurate
def countdown2(finish):
    """
    Takes argument finish and counts down the time till it's reached.

    Assumes finish is an Epoch time from the user in seconds and greater than the present.

    Returns the number of iterations completed.
    """
    ticks = 0

    i = int(finish - time.time())

    while 0 <= i:
        print i
        ticks += 1
        i -= 1
        time.sleep(0.999)

    return ticks

def getTime():
    """
    Prompts the user for a time formated as MM/DD/YYYY HH:MM:SS.

    Checks if time is:
    1) Greater than the present
    2) A valid format for a date

    Returns the inputed time as a time_struct.
    """
    no_time = True

    while no_time:

        end_time = raw_input("Please enter a date MM/DD/YYYY and time HH:MM:SS(24-hour): ")

        try:
            end_time = time.strptime(end_time, "%m/%d/%Y %H:%M:%S")

            if time.time() < time.mktime(end_time):
                break
            else:
                raise ValueError
        except ValueError:
            print "Please enter a future time in the specified format.\n"
            pass

    return end_time

def main():
    print countdown2(time.mktime(getTime()))


if __name__ == '__main__':
    main()
