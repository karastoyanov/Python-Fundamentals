import re

number_barcodes = int(input())
list_of_matches = []

while number_barcodes > 0:
    bardcode = input()
    pattenr = r'^@+#{1,}[A-Za-z0-9]{5,}[A-Z]@+#{1,}'
    matches = re.findall(pattenr, bardcode)
    if matches:
        list_of_matches.append(matches[0])
        for i in range(len(list_of_matches)):
            current_bardcore = list_of_matches[i]
            current_pattern = r"\d"
            current_match = re.findall(current_pattern, current_bardcore)
            if not current_match:
                print("Product group: 00")
                break
            else:
                print(f"Product group: {''.join(current_match)}")
                break
    else:
        print("Invalid barcode")
    list_of_matches = []
    number_barcodes -= 1


