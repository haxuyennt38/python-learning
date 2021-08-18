##Traitement exceptionnel quand le saisir n'est pas exact
#taper le système décimal sur le clavier (system decimal)
systemdecimal = input()

#Afficher le système de numération octal (Show the octal number system)
if systemdecimal != int :
    print('')
else :
    print('The number decimal %d in the octal number system %o' % (systemdecimal, systemdecimal))