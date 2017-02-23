from sys import argv

print argv
print type(argv)

script, name, age = argv

print "Ciao %s, hai %s anni" % (name, age)
