import re
import csv

with open("phonebook_raw.csv", 'r', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    new_list = []


def names_moving():
    name_pattern = r'([А-Я])'
    name_substitution = r' \1'
    for contact in contacts_list[1:]:
        full_name = contact[0] + contact[1] + contact[2]
        name_parts = re.sub(name_pattern, name_substitution, full_name).split()

        if len(name_parts) == 3:
            contact[0] = name_parts[0]
            contact[1] = name_parts[1]
            contact[2] = name_parts[2]
        elif len(name_parts) == 2:
            contact[0] = name_parts[0]
            contact[1] = name_parts[1]
            contact[2] = ''
        elif len(name_parts) == 1:
            contact[0] = name_parts[0]
            contact[1] = ''
            contact[2] = ''

    return


def phone_format():
    pattern_phone = re.compile(
        r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    phone_sub = r'+7(\2)\3-\4-\5 \8\9'
    for column in contacts_list:
        column[5] = pattern_phone.sub(phone_sub, column[5])
    return


def double_():
    for i in contacts_list:
        for j in contacts_list:
            if i[0] == j[0] and i[1] == j[1] and i is not j:
                if i[2] == '':
                    i[2] = j[2]
                if i[3] == '':
                    i[3] = j[3]
                if i[4] == '':
                    i[4] = j[4]
                if i[5] == '':
                    i[5] = j[5]
                if i[6] == '':
                    i[6] = j[6]


    for card in contacts_list:
        if card not in new_list:
            new_list.append(card)
    return new_list



if __name__ == '__main__':
    names_moving()
    phone_format()
    double_()

    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_list)
