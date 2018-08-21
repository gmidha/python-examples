#!/usr/bin/env python3
# this program gets name and dob from a user and then returns a message when a person will turn 100 years old.

def get_details():
  name = input("Please enter your name: ")
  date = input("Please enter your date of birth in YYYY-MM-DD format: ")
  return name,date

def turn_100():
  name,dob = get_details()
  year,mon,day = dob.split("-")
  after_hun_years = int(year) + 100
  print(f"{name} will be 100 years old on {after_hun_years}-{mon}-{day}")

def main():
  turn_100()

if __name__ == '__main__':
  main()
