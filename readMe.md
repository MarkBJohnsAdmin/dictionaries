# Dictionaries

Till this point, we've been storing our x axis data and y axis data in their own lists, but this can present a problem. Let's look at the populations of a few countries:

```py
populations = [30.55, 2.77, 39.21] # in millions

countries = ["afghanistan", "albania", "algeria"]
```

If we wanted to get the population of Albania, we need to figure out what the index of "albania" is in the `countries` list, and then find the corresponding index in the `populations` list:

```py
alb_idx = countries.index("albania")

alb_pop = populations[alb_idx]

print(alb_pop) # 2.77
```

This worked, but it's a terrible approach. For starters, it's slow and inconvenient, but it's also making an assumption that the populations and countries lists are perfectly aligned, and will continue to be for the lifetime of the project.

This is where `dictionaries` come in. Instead of keeping two lists and hoping they stay formatted together, we can connect the two values directly. Think about how a real dictionary works when you're trying to figure out what a word means. You already know the word you're looking up, it's just the definition you need to find out. Python dictionaires work the same, with the "word" you're trying to figure out being represented by a `key`, and the "definition" of that word being the key's `value`.

Dictionaires are enclosed in braces, with the keys (usually) being strings and the values being several possible (but not all) data types. We can rework the two lists into a single dictionary to make looking up the values much faster and more intuitive.

```py
population_chart = {
    "afghanistan": 30.55,
    "albania": 2.77,
    "algeria": 39.21
}
```

Now, not only is the search is only a single step process:

```py
alb_pop = population_chart['albania']
```

## Why Dictionaries

But the search has much better performance as well. When you search for the list index of a value, Python has to go through all of the items in the list until it finally reaches the value you searched for, meaning that if your value is the last value in the list, you have to go through every item in that list before the search ends. However, if you already know the index, it's only a single step regardless of how big the list is, because it knows where in the list to go right away. Dictionaries work in largely the same way, but rather than an index, it searches by the key. This makes it so no matter how many countries you add to population_chart, it's always extremely fast to check that country's population.

The keys in dictionaries need to be `immutable objects`, which just means that they should be data types that can't have their value changed once it's created. Strings, booleans, integers, and floats are immutable, while lists are not.

```py
string1 = "hello world" # this string cannot be changed

string1 = "Hello, world!" # the value of the string1 variable has been redeclared, but this is a new string - the value of the first string didn't change

nums = [1, 2, 3, 4, 5] # this array can be changed

nums = [6, 7, 8, 9, 10] # the values inside the array are different, but nums is stil the same array
```

Keys need to be immutable so once they're set up, you can always get the same data consistently from the same search term:

```py
i_am_hungry = {
    True: "eat something",
    False: "don't eat something"
}
```

## Adding / Removing Keys

To add a key to your dictionary, you declare it the same way you would declare any other variable, you just have to tie it to the dictionary as you do:

```py
population_chart['bosnia'] = 3.28

# population_chart == {
#     "afghanistan": 30.55,
#     "albania": 2.77,
#     "algeria": 39.21,
#     "bosnia": 3.28
# }
```

Just like you can redeclare existing variables without causing any issues, you can redeclare key values. Python will automatically change a key value or create a new key / value pair depending on if the key is already in the object or not, and you don't need to do anything to set that up.

Deleting keys is simple as well, as you can use the built-in `del` function:

```py
del(population_chart['bosnia'])

# population_chart == {
#     "afghanistan": 30.55,
#     "albania": 2.77,
#     "algeria": 39.21
# }
```

Just be sure to declare the key you want to delete so you don't delete the entire dictionary.
