Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> username = input (' What is your username  ')
password = input (' what is your password  ')

password_len = len(password)
hiddin_password = '*' * password_len

print(f'{username} , your password {hiddin_password} is  more than {password_len} ')