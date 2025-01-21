try:
    import pandas
    import sklearn
except ImportError as e:
    print("Environment seems to be set up incorrectly. Can't import all needed dependencies.")
    raise e
print("Environment seems correct!")