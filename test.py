try:
    f = open("/Users/ruthielin/Downloads/(USE) BLM Protests 2020.csv")
except IOError:
    print("hello")
finally:
    f.close()