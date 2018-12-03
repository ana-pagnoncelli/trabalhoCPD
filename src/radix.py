def radix_sort(array):
    def list_to_buckets(array, limite):
        buckets = [[] for _ in range(26)]
        for word in array:
            if len(word) >= limite:
                digit = ord(word[limite-1]) - ord('a')
            else:
                digit = 0
            buckets[digit].append(word)
        limite -= 1
        return buckets, limite

    def buckets_to_list(buckets):
        numbers = []
        for bucket in buckets:
            for number in bucket:
                numbers.append(number)
        return numbers

    limite = max(array, key=lambda x: len(x))
    limite = len(limite)
    # Itera, posicionando o array pra cada digito
    for i in range(limite):
        buckets, limite = list_to_buckets(array, limite)
        array = buckets_to_list(buckets)

    return array
