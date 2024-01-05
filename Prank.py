import os
a = os.getcwd()
f = sorted(list(os.walk(a))[1:],reverse=True)
for fld in f:
   try:
    os.rmdir(fld[0])
   expect OSError as error:
    print("\U0001F637:J4F")
