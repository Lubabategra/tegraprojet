nom=input("veuillez entrer votre nom: ") #donne à l'utilisateur la possibilité d'entrer les caractère
postnom=input("veuillez entrer votre postnom: ")
prénom=input("veuillez entrer votre prénom: ")
age=int(input("quelle est votre age: "))
if age<10: #stucture conditionelle
    print(f"bonjour {nom} {postnom} {prénom} tu es bébé")
elif age<=18 and age>10:
    print(f"bonjour {nom} {postnom} {prénom} vous êtes Mineur")    
elif age>=18 and age<50:
    print(f"bonjour {nom} {postnom} {prénom} vous êtes jeune majeur")
elif age>=50 and age<100:
    print(f"bonjour {nom} {postnom} {prénom} vous êtes Vieux majeur")
else:
    print(f"bonjour {nom} {postnom} {prénom} vous êtes un veuillard")

