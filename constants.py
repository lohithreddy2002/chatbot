DEFAULT_SQL_PATH = "sqlite:////home/lohith/chatbot/test.db"
DEFAULT_ENTRY_TABLE_DESCRP = (
    "The entries table contains information about entries and exits from a facility"
    "including the entry and exit times, the vehicle ID, and the entry and exit gates."
    " entry time and exit time are stored in the format of 'YYYY-MM-DD HH:MM:SS.FFFFFF'"
    "the user may query about entries on a specific date, then you should change the query date in to the Datetime format set the year by default to 2023 and run the query"
    "The user may query about a specific entry in the table, whose vechile can be found by mapping the vehicle id to the 'vehicles' table."
)


# (
#     "The entries table contains information about entries and exits from a facility"
#     "including the entry and exit times, the vehicle ID, and the entry and exit gates."
#     " entry time and exit time are stored in the format of 'YYYY-MM-DD HH:MM:SS'"
#     "the user may query about entries on a specific date, then you should change the query date in to the Datetime format and run the query"
#     "The user may query about a specific entry in the table, whose vechile can be found by mapping the vehicle id to the 'vehicles' table."
# )


# (
#     "The entries table contains information about entries and exits from a facility"
#     "including the entry and exit times, the vehicle ID, and the entry and exit gates."
#     " entry time and exit time are stored in the format of 'YYYY-MM-DD HH:MM:SS'"
#     "The user may query about a specific entry in the table, whose vechile can be found by mapping the vehicle id to the 'vehicles' table."
# )

DEFAULT_VEHICLES_TABLE_DESCRP = (
    "The vehicles table contains information about vehicles, including their ID, type, licence plate, and color."
    "There are 3 different types of vehicles like car, bike and truck, the type of vehicle can be found by the 'type' column in the table"
    "The user may query about specific vechile by the type or number_plate"
)

DEFAULT_VEHICLE_ENTRY_TABLE_DESCRP = (
    "the vehicle entry table contains information about vehicles which entered a parking lot."
    "There are 3 different types of vehicles like car, bike and truck, the type of vehicle can be found by the 'vehicle_type' column in the table"
    "'parked_level' colum gives information about where the vehicle is parked, level 1 is also called first floor"
)
