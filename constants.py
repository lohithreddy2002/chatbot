DEFAULT_SQL_PATH = "sqlite:////home/lohith/chatbot/test.db"
DEFAULT_BUSINESS_TABLE_DESCRP = (
    "This table gives information on the IDs, addresses, and other location "
    "information for several restaurants in San Francisco. This table will "
    "need to be referenced when users ask about specific businesses."
)
DEFAULT_VIOLATIONS_TABLE_DESCRP = (
    "This table gives information on which business IDs have recorded health violations, "
    "including the date, risk, and description of each violation. The user may query "
    "about specific businesses, whose names can be found by mapping the business_id "
    "to the 'businesses' table."
)
DEFAULT_INSPECTIONS_TABLE_DESCRP = (
    "This table gives information on when each business ID was inspected, including "
    "the score, date, and type of inspection. The user may query about specific "
    "businesses, whose names can be found by mapping the business_id to the 'businesses' table."
)
DEFAULT_LC_TOOL_DESCRP = "Useful for when you want to answer queries about violations and inspections of businesses."