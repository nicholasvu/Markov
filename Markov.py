import pandas as pd

mdf = pd.DataFrame({'Bull market': [0.9, 0.15, 0.25],
                    'Bear market': [0.075, 0.8, 0.25],
                    'Stagnant market': [0.025, 0.05, 0.5]
                    },
                    index=["Bull market", "Bear market", "Stagnant market"])
print mdf

markets=["Bull market", "Bear market", "Stagnant market"]
for current_m in markets:
    print "if it's %s:" %current_m
    for next_m in markets:
        nextprob=mdf.loc[current_m, next_m]
        print "  - the probability of %s next is %.2f" %(next_m, nextprob)

n = 2

print "Original transitional probabilities: \n"
print mdf
print "\n"

def state(n):
	i = 1
	global mdf
	while i < n:
		mdf = mdf.dot(mdf)
		i += 1
	print "Transitional probabilities after {} transitions: \n".format(n)
	print mdf

state(n)
