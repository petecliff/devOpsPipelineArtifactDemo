import os
from datetime import datetime
from random import randint

environments = ["Dev", "Stage", "Prod"]
qa_resources_prefix = "./QA_Resources/%s" % environments[randint(0,len(environments)-1)]

try:
    os.makedirs(qa_resources_prefix)
    print("Created QA Resources folder")
except OSError as error:
    print("QA Resources folder already exists")

now = datetime.now()

print("Build starting on " + str(now))
print("Environment is: ")

for key, value in os.environ.items():
    print("%s = %s" % (key, value))

print("Files are:")
files = []

for r,d,f in os.walk("."):
    for file in f:
        if ('.git' not in file):
            files.append(os.path.join(r, file))

for f in files:
    print(f)

existingfname = "%s/run_log.txt" % (qa_resources_prefix)
existingf = open(existingfname, 'a')

print("Resource file content is:");

for line in existingf:
    print(line)

print("== end of file ===")

existingf.write("Build run: %s\n" % str(now))
existingf.close()