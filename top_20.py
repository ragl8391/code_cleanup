import matplotlib.pyplot as plt

codes = [
"E122","E501","E203","F401","W291","E302","E128","W293","E231","F403",
"F821","E402","E252","E251","F811","W292","E303","E301","E261","E305"
]

counts = [
8180,5539,626,215,158,133,77,75,72,49,
31,31,28,20,17,17,15,14,14,7
]

names = [
"Continuation line missing indentation",
"Line too long",
"Whitespace before ':'",
"Module imported but unused",
"Trailing whitespace",
"Expected 2 blank lines before definition",
"Under-indented continuation line",
"Blank line contains whitespace",
"Missing whitespace after ','",
"'from module import *' used",
"Undefined name",
"Import not at top of file",
"Missing whitespace around parameter =",
"Unexpected whitespace around parameter =",
"Redefinition of unused name",
"No newline at end of file",
"Too many blank lines",
"Expected 1 blank line",
"Spaces before inline comment",
"Expected 2 blank lines after definition"
]

labels = [f"{c} — {n}" for c, n in zip(codes, names)]

plt.figure(figsize=(12,8), dpi=300)

bars = plt.barh(labels, counts, color="#4C72B0")

plt.xlabel("Number of Warnings", fontsize=12)
plt.title("Top 20 Flake8 Warnings in the CameraTraps Repository", fontsize=14)

plt.gca().invert_yaxis()

for i, v in enumerate(counts):
    plt.text(v + 50, i, str(v), va="center")

plt.tight_layout()

plt.savefig("flake8_top20_warnings.png", dpi=300)
plt.show()
