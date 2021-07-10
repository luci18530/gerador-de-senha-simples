# Gerador de senha simples com 8 caracteres, sendo 2 letras maiusculas, 2 minusculas e 4 digitos

from random import randint

letramaiuscula1 = chr(randint(65, 90))
letramaiuscula2 = chr(randint(65, 90))
letraminuscula1 = chr(randint(97, 122))
letraminuscula2 = chr(randint(97, 122))
digito1 = chr(randint(48, 57))
digito2 = chr(randint(48, 57))
digito3 = chr(randint(48, 57))
digito4 = chr(randint(48, 57))

senha = letramaiuscula1+letramaiuscula2+letraminuscula1+letraminuscula2+digito1+digito2+digito3+digito4
print(senha)
