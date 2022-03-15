import random
import settings

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
      0,1,2,3,4,5,6,7,8,9,]


if settings.passwors_per_file == True:
    for l in letters:
        file_name = f"passwords/{l}.txt"
        with open(file_name, 'w') as file:


            for i in range(0,settings.passwors_per_file,1):
                code = l
                for j in range(0,settings.password_len,1):
                    r = random.randint(0,len(letters)-1)
                    code = f"{code}{letters[r]}"

                file.write(code + "\n")

if settings.passwors_per_file == False:
    file_name = f"passwords/passwords.txt"
    with open(file_name, 'w') as file:
        for i in range(0,(settings.passwors_per_file),1):
            code = "l"
            for j in range(0, settings.password_len, 1):
                r = random.randint(0, len(letters) - 1)
                code = f"{code}{letters[r]}"

            file.write(code + "\n")




