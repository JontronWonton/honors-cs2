# Jonathan Klein
# 10/11/2018
# madLibsProject.py

# Initial print statement below gives instructions to user
story = raw_input("Welcome to Mad Libs. Which theme would you like to do?\n1. Summer Trip\n2. Pretty Princess\n3. Astronaut\n")

summerTrip = []
prettyPrincess = []
astronaut = []

# Each function below appends the user input to the end of each according list

def summerTripAdd(intake):
    summerTrip.append(raw_input(intake))


def prettyPrincessAdd(intake):
    prettyPrincess.append(raw_input(intake))


def astronautAdd(intake):
    astronaut.append(raw_input(intake))


if story == "1":
# if the user selects summer trip or according shortcut
    summerTripAdd("1. Enter a person\n")
    summerTripAdd("2. Enter a place\n")
    summerTripAdd("3. Enter an adjective\n")
    # (#2 place used)
    summerTripAdd("4. Enter a plural noun\n")
    summerTripAdd("5. Enter an adjective \n")
    summerTripAdd("6. Enter a plural noun\n")
    summerTripAdd("7. Enter a place\n")
    summerTripAdd("8. Enter a verb\n")
    summerTripAdd("9. Enter a plural noun\n")
    summerTripAdd("10. Enter a plural noun\n")
    summerTripAdd("11. Enter a noun\n")
    summerTripAdd("12. Enter a verb\n")
    summerTripAdd("13. Enter a noun\n")
    summerTripAdd("14. Enter an adjective\n")
    # Statement below prints entire story and replaces blanks with elements within the list (Using .format)
    # Print statements cannot be intended as it adds whitespace
    print ('''Last summer, my mom and dad took me and {} 
on a trip to {}. The weather there is very 
{}! Northern {} has many 
{} and they make {} {} there. 
Many people also go to {} to {} or 
see the {}. The people that live there love to 
eat {} and are very proud of their big 
{}. They also like to {} in 
the sun and swim in the {}! It was a really 
{} trip!'''.format(summerTrip[0],summerTrip[1],
    summerTrip[2], summerTrip[1], summerTrip[3],
    summerTrip[4], summerTrip[5], summerTrip[6],
    summerTrip[7], summerTrip[8], summerTrip[9],
    summerTrip[10], summerTrip[11], summerTrip[12],
    summerTrip[13]))
elif story == "2":
# if the user selects Pretty Princess or according shortcut
    prettyPrincessAdd("1. Enter an adjective\n")
    prettyPrincessAdd("2. Enter a name\n")
    prettyPrincessAdd("3. Enter a number\n")
    # (#2 name used)
    prettyPrincessAdd("4. Enter a relative\n")
    # (#2 name used)
    prettyPrincessAdd("5. Enter a place\n")
    prettyPrincessAdd("6. Enter another place\n")
    prettyPrincessAdd("7. Enter a verb ending in ing\n")
    prettyPrincessAdd("8. Enter a plural noun\n")
    prettyPrincessAdd("9. Enter an adjective\n")
    prettyPrincessAdd("10. Enter another adjective\n")
    prettyPrincessAdd("11. Enter a person\n")
    prettyPrincessAdd("12. Enter an adverb\n")
    # Statement below prints entire story and replaces blanks with elements within the list (Using .format)
    # Print statements cannot be intended as it adds whitespace
    print('''A new and {} fairy princess movie is coming 
out soon! it will be about Snow {} and the {} 
dwarfs. Snow {} is a princess whose 
beauty threatens her {}, the queen. Snow 
{} is forced to flee from {} 
and hides in nearby {}. There, she 
discovers the dwarfs {} in their 
{}. But the queen finds her and casts a 
{} on her. The dwarfs take care of her 
until the {} {} comes to rescue 
her, and they live {} ever after!'''
    .format(prettyPrincess[0], prettyPrincess[1],
    prettyPrincess[2], prettyPrincess[1], prettyPrincess[3],
    prettyPrincess[1], prettyPrincess[4], prettyPrincess[5],
    prettyPrincess[6], prettyPrincess[7], prettyPrincess[8],
    prettyPrincess[9], prettyPrincess[10], prettyPrincess[11]))
elif story == "3":
# If the user selects Astronaut or according shortcut
    astronautAdd("1. Enter a verb ending in ing\n")
    astronautAdd("2. Enter a verb\n")
    astronautAdd("3. Enter a vehicle\n")
    astronautAdd("4. Enter a verb\n")
    astronautAdd("5. Enter a plural tool\n")
    astronautAdd("6. Enter a plural noun\n")
    astronautAdd("7. Enter a color\n")
    astronautAdd("8. Enter an adjective\n")
    astronautAdd("9. Enter a color\n")
    astronautAdd("10. Enter a number\n")
    astronautAdd("11. Enter a plural body part\n")
    astronautAdd("12. Enter another plural body part\n")
    astronautAdd("13. Enter a verb\n")
    astronautAdd("14. Enter another verb\n")
    astronautAdd("15. Enter a vehicle\n")
    astronautAdd("16. Enter a place\n")
    astronautAdd("17. Enter a verb\n")
    # Statement below prints entire story and replaces blanks with elements within the list (Using .format)
    # Print statements cannot be intended as it adds whitespace
    print('''Instead of {} everyday to an 
office, I want to {} to outer 
space on a {} for my job. I'd 
{} science experiments used 
{} and {}, and get to see 
{} holes and {} stars up 
close. Maybe I'd even get to meet 
an alien life form, with {} skin 
and {} {} and {}. When it's 
time to {} to Earth, I'll {} in a 
{} and land safely in a {}, 
where friends and family will {}
me and welcome me home'''
    .format(astronaut[0], astronaut[1],
    astronaut[2], astronaut[3], astronaut[4],
    astronaut[5], astronaut[6], astronaut[7],
    astronaut[8], astronaut[9], astronaut[10],
    astronaut[11], astronaut[12], astronaut[13],
    astronaut[14], astronaut[15], astronaut[16],))
