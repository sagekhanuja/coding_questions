def longest_binary(number):
    sum_array = []
    sum = 0
    binary = str(bin(number))

    for i in range(len(binary)):
        ii = i
        while binary[ii] == '1':
            sum+=1
            ii+=1
        sum_array.append(sum)
        sum = 0
    print(binary)
    print(max(sum_array))

longest_binary(1230)