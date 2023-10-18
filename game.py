import random 
repeat = True

while repeat:
   number = random.randint(1, 100)
   guess = 0
   tries = 0

   while guess != number:
       if guess<number:
          print("lielāku")
       else:
           print("mazāku")

       guess = int(input("Uzmini skaitli: "))
       tries += 1
   else:
       if tries < 4:
           print(f"labi, uzminēji pēc {tries} reizēm")
       elif tries < 7:
           print(f"normāli, uzminēji pēc {tries} reizēm")
       else:
           print(f"mēģini vēlreiz, uzminēji tikai pēc {tries} reizēm...")
       

   response = input("gribi turpināt ? y/n: ")
   if response == "y":
        repeat = True
   elif response == "n":
       repeat = False
       print("atā")
   else:
       repeat = False
       print("atā")
    
