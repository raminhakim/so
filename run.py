import os

if __name__ == "__main__":
   try:
       os.system("git pull")
       __import__("D3M09").moch_yayan()
   except Exception as e:
       exit(str(e))
