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
from datetime import date

today = date.today()

DEFAULT_VEHICLES_TABLE_DESCRP = (
    "The vehicles table contains information about vehicles, including their ID, type, licence plate, and color."
    "There are 3 different types of vehicles like car, bike and truck, the type of vehicle can be found by the 'type' column in the table"
    "The user may query about specific vechile by the type or number_plate"
)

DEFAULT_VEHICLE_ENTRY_TABLE_DESCRP = (
    # "Use the following pieces of context to answer the questions abouth the table. If you don't know the answer, just say that you don't know, don't try to make up an answer. "
    "queries should not write into the database or change the database schema. Like DELETE, INSERT and CREATE should not be run."
    "the vehicle entry table contains information about vehicles which entered a parking lot."
    "the user may ask queries related to specific Date for which the the 'entry_time' should be converted into Date format. "
    "the user may query about entries on a specific date and the year is not specfied, then you should change the query date in to the Datetime format set the year by default to 2023 and run the query. "
    "There are 3 different types of vehicles car,bike and truck, the type of vehicle can be found by the 'vehicle_type' column in the table. "
    "the user may query about a particular type of vehicle for which 'vehicle_type' column should be queried"
    "'parked_level' column gives information about where the vehicle is parked, level 1 is also called first floor. "
    "the entries with the same number_plate should be counted as a single entry. "
    "Ignore the 'id' column when giving the reults. "
    "when running queries related to dates use sqlite synatx only. "
    "vehicle type and vehicle color is always in lower case. "
    "time spent by a vehicle should be displayed in minutes. "
    "vehicles should be described by the number plate"
    "the queries which only want current date can use this date {} , for other queries this should not be used.".format(today)

   
)


DEFAULT_VEHICLE_ENTRY_TABLE_TEST_DESCRP = (
    "queries should not write into the database or change the database schema. Like DELETE, INSERT and CREATE should not be run."
    "the vehicle entry table contains information about vehicles which entered a parking lot."
    "the user may ask queries related to specific Date for which the the 'entry_time' should be converted into Date format. "
    "the user may query about entries on a specific date, then you should change the query date in to the Datetime format set the year by default to 2023 and run the query. "
    "There are 3 different types of vehicles like car, bike and truck, the type of vehicle can be found by the 'vehicle_type' column in the table if the vechicle_type value is"
    " 1 then it is car and if the value is 2 then it is a bike if the value is 3 then it is a Truck"
    "'parked_level' column gives information about where the vehicle is parked, level 1 is also called first floor. "
    "the entries with the same number_plate should be counted as a single entry. "
    "Ignore the 'id' column when giving the reults. "
    "when running queries related to dates use only sqlite synatx. "
    "the queries related which want current date can use this date use current date as {} .".format(today)
    
   
)
