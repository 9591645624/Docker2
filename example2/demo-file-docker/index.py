def http_status(status):
    switcher = {
        200: "OK",
        404: "Not Found",
        500: "Internal Server Error"
    }
    return switcher.get(status, "Unknown Status")

print(http_status(200))   # Output: OK
print(http_status(404))   # Output: Not Found
print(http_status(123))   # Output: Unknown Status