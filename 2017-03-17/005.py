univer = raw_input()
#result = univer + " is the best! Go, " + univer + "!"
#result = "%s is the best! Go, %s" % (univer, univer)
#result = "{0} is the best! Go, {0}!".format(univer)

res = "%(u)s is the best! Go, %(u)s!" % {'u' : univer}

print res