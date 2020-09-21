#%%
import random
#%%
def newFunction ():
    x = random.random() * 100
    return x

def formattedPrint(username, output):
    print(f'{username}: {output}')