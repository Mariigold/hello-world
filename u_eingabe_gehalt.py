
print"Bitte geben Sie ihren Bruttolohn ein"
bruttobetrag = float(input())

if bruttobetrag > 2500:
	steuerbetrag = bruttobetrag * 0.22

elif bruttobetrag > 4000:
	steuerbetrag = bruttobetrag * 0.26

else:
	steuerbetrag = bruttobetrag * 0.18

print("Es ergibt sich ein Steuerbetrag von", steuerbetrag, "CHF")


