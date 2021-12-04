nr_inputs = int(input())
positive_nmb = []
positive_sums = 0
negative_nmb = []
negative_sum = 0

for i in range(nr_inputs):
    number = int(input())
    if number >= 0:
        positive_nmb.append(number)
        positive_sums += 1
    else:
        negative_nmb.append(number)


print(positive_nmb)
print(negative_nmb)
print(f"Count of positives: {positive_sums}\nSum of negatives: {sum(negative_nmb)}")

