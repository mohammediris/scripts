import smvalidate

ipv4_address    = '192.4.0.1'
ipv4_mask       = '255.255.255.0'
website_address = 'www.schoolofiris.com'
email_address   = 'alerts@schoolofiris.com'
password        = 'Pythonmn'

wrong_ipv4_address    = '600.4.0.1'
wrong_ipv4_mask       = '600.255.255.0'
wrong_website_address = 'wwwchoolofirisom'
wrong_email_address   = 'alertsschoolofiris.com'
wrong_password        = 'Pyt3'

print('IP address\t\t- ',smvalidate.validate_ipv4_address(ipv4_address))
print('IP mask\t\t\t- ',smvalidate.validate_ipv4_mask(ipv4_mask))
print('web address\t\t- ',smvalidate.validate_website_address(website_address))
print('email address\t- ',smvalidate.validate_email(email_address))
print('password\t\t- ',smvalidate.validate_password(password,8,1))

print('IP address\t\t- ',smvalidate.validate_ipv4_address(wrong_ipv4_address))
print('IP mask\t\t\t- ',smvalidate.validate_ipv4_mask(wrong_ipv4_mask))
print('web address\t\t- ',smvalidate.validate_website_address(wrong_website_address))
print('email address\t- ',smvalidate.validate_email(wrong_email_address))
print('password\t\t- ',smvalidate.validate_password(wrong_password,8,1))