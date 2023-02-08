def main():

    #TODO: Step 2 - Create a complex data structure
    about_me = {
                'full_name':'Dhruvkumar Patel',
                'student_id':'10284633',
                'pizza_toppings':['LETTUCE','GREEN ONION','CILANTRO'],
                'movies':[
                    {
                    'title':'main hoo na',
                    'genre':'family'
                    },
                    {
                    'title':'bahubali',
                    'genre':'action'
                    }
                    ]
            }

    #TODO: step 3 - Add another movie to the data structure
    about_me['movies'].append({'title':'top gun','genre':'thrillar'})
    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    add_pizza_toppings(about_me,('GREEN OLIVES','CORN'))
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me)

#TODO: step 4 - fuction that print name and ID
def print_student_name_and_id(about_me):
    first_name=about_me['full_name'].split(" ")[0]
    print(f"My name is {about_me['full_name']}, but you can call me Mr. {first_name}.")
    print(f"My student ID is {about_me['student_id']}.\n")
    return

#TODO: step 5 - fuction that add pizza topings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].extend(toppings)
    
    for i,topping in enumerate (about_me['pizza_toppings']):
        about_me['pizza_toppings'][i] = topping.lower()
    about_me['pizza_toppings'].sort()
    print(" ")
    return

#TODO: step 6 - function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print(f"My favourite pizza toppings are:")
    for topping in about_me['pizza_toppings']:
        print(f"-{topping}")
    return

#TODO: step 7 - function that prints comma-seperated list of movie genres
def print_movie_genres(about_me):
    print(f"\nI like to watch",end=" ")
    genre=[g['genre'] for g in about_me['movies']]
    print(', '.join(genre), end='.')
    print('\n')
    return

#TODO: step 8 - function that prints comma-seperated list of movie titles
def print_movie_titles(movie_list):
    print(f"Some of my favourite movies are ",end='')
    movie_titles=[m['title'].title() for m in movie_list['movies']]
    print(', '.join(movie_titles),end='!\n')
    return

if __name__ == '__main__':
    main()