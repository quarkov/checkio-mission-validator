"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [LogLine("123 k passive")],
            "answer": [None, None, None, "wrong name value"]
        },
        {
            "input": [LogLine("123 search active")],
            "answer": [123, "search", "active", "passed data is valid"]
        },
        {
            "input": [LogLine("1001 search active")],
            "answer": [None, None, None, "wrong id value"]
        },
        {
            "input": [LogLine(["1001 search active"])],
            "answer": [None, None, None, "wrong input type"]
        },
        {
            "input": [LogLine("900 search passive")],
            "answer": [None, None, None, "wrong status value"]
        },
        {
            "input": [LogLine("900 search passive something")],
            "answer": [None, None, None, "wrong input value"]
        },
        {
            "input": [LogLine("0111 transfer active")],
            "answer": [111, "transfer", "active", "passed data is valid"]
        },
        {
            "input": [LogLine(set("0111 transfer active"))],
            "answer": [None, None, None, "wrong input type"]
        },
    ],
    "Extra": [
        {
            "input": [LogLine("")],
            "answer": [None, None, None, "wrong input value"]
        },
        {
            "input": [LogLine([])],
            "answer": [None, None, None, "wrong input type"]
        },
    ]
}
