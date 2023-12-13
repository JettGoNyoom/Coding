# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting list in Dict  
travel_logA = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Munich"]
}
# can also nest lists in list

# Nest dict in dict
travel_logB = {
    "France" : {"cities visited": ["Paris", "Lille", "Dijon"], "total visits": 12},
    "Germany": {"cities visited": ["Berlin", "Hamburg", "Munich"], "total visits": 5}
}

#Nesting Dictionaries in Lists

travel_logC = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]