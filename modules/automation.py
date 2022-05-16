import re


def get_phones(read_path, write_path):
    with open(read_path) as file:
        text = file.readlines()
    phone_contacts = []
    phone_regex =  r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}(?:\s*(?:#|x\.?|ext\.?| extension)?\s*(?:\d+)?)'
    phone_comp = re.compile(phone_regex)

    for t in text:
        phones = phone_comp.findall(t)
        for phone in phones:
            symbols = re.sub(r'(?:\s|[\(\)._-])', "",phone)
            normalize = re.sub(r"(\d{3})(\d{3})(.*)", r"\1-\2-\3",symbols)
            extend = re.sub(r'x', " x",normalize)
            phone_string = str(extend)
            if extend not in phone_contacts:
                phone_contacts.append(phone_string)
    
    phone_contacts.sort()
    file.close()

    with open(write_path,'w') as phone_file:
        for contact in phone_contacts:
            phone_file.write(contact)
            phone_file.write('\n')
    
    phone_file.close()


def get_emails(read_path, write_path):
    with open(read_path) as file:
        text = file.readlines()
    email_contacts = []
    email_regex = r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)'
    email_comp = re.compile(email_regex)

    for t in text:
        emails = email_comp.findall(t)
        for email in emails:
            email_string = str(email)
            if email not in email_contacts:
                email_contacts.append(email_string)
    
    email_contacts.sort()
    file.close()

    with open(write_path, 'w') as email_file:
        for email in email_contacts:
            email_file.write(email)
            email_file.write('\n')
    
    email_file.close()


file_to_read = './assets/potential-contacts.txt'
phone_file_to_write = './assets/phone_numbers.txt'
email_file_to_write = './assets/email_addresses.txt'

get_phones(file_to_read, phone_file_to_write)
get_emails(file_to_read, email_file_to_write)