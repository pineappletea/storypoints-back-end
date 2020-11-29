#hardcoded tokens as placeholder
#actual tokens would also have lifespan etc

testtokens = ["1", "2", "3", "4"]

def tokenOK(token):
    if token in testtokens:
        return True
    else:
        return False
        