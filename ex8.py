# define formatter as %r %r %r %r
formatter = "%r %r %r %r"

# print formatter with values 1, 2, 3, 4
print formatter % (1, 2, 3, 4)

# print formatter with values 'one', 'two', 'three', 'four'
print formatter % ("one", "two", "three", "four")

# print formatter with values True, False, False, True
print formatter % (True, False, False, True)

# print formatter with values '%r %r %r %r', '%r %r %r %r', '%r %r %r %r', '%r %r %r %r'
print formatter % (formatter, formatter, formatter, formatter)

# print formatter with values of the below strings. The third line will be printed with double quotes
# because it contains a contraction with an apostrophe.
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
	)