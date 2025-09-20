# How to Run the Program
Prerequisites: Make sure you have Python 3 installed.

Clone the repository:


git clone <https://github.com/sethbis/Algorithm-for-breaking-passwords.git>
Navigate to the directory:


cd <the place u want to save the repositori>
Run the script:


python bruteforce.py
# Algorithm-for-breaking-passwords
# how it works?
we import 3 important functions

time = we use this find how many time the programs was need to find de password
iteertools = we use this with .produc to make posible to generate 1 by 1 all te posible combinations with the characters we give and the length we give
string = we use this to add with functions all the assci characters in upper and lower case, the numers

we add and we manually add the special characters with all the functions we call of string a a variable called chars

In the loop where itertools.product is used, the guess variable stores, one by one, every combination that itertools returns using the given characters and the current length from the outer loop. Then, 1 is added to the number of attempts, and in the attempt variable, the output from itertools is joined together, because it returns tuples, and join saves it as a string.

After that, the if statement checks if that attempt is equal to the entered password. If it's not equal and the loop has already tried all combinations for length 1, it moves on to length 2, and so on, until it finds a match.

If it finds the password, the elapsed variable saves the total time that has passed since before the loop started. Finally, it prints the number of attempts from the attempts variable, the password that was found, and the time saved in the elapsed variable, and then the program ends.

# Sample output

ingrese la contraseña para verificar que tan segura es: 1234 
Contraseña encontrada: 1234
Tiempo: 4.3023 segundos

ingrese la contraseña para verificar que tan segura es: 12345
Contraseña encontrada: 12345
Intentos: 1104957760
Tiempo: 281.4629 segundos


# Reflection
The time required to find a password grows exponentially as the password length increases and the character set becomes larger.

For the defined character set
(26 lowercase + 26 uppercase + 10 digits + 5 symbols = 67 characters),
the number of possible attempts is:

Total combinations = 67**𝐿
Total combinations=67
L
Length (L)	Possible combinations
3	            300,763
5	            1.6 × 10⁹
8	            5.7 × 10¹⁴


So short or simple passwords are found very quickly.

Long, complex passwords adding more characters, digits and symbols become practically impossible to break using brute-force, to improve security, always use long, complex passwords and consider enabling two-factor authentication if is possible.