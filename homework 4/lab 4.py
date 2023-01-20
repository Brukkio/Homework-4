#Bruk Thomas Tewelde
#PSID: 1834503
num_calls = 0
def partition(user_ids, l, h):
        i = (l-1)
        pivot = user_ids[h]
        for j in range(l, h):
                if user_ids[j] < pivot:
                        i = i+1
                        # swap
                        user_ids[i], user_ids[j] = user_ids[j], user_ids[i]
        user_ids[i+1], user_ids[h] = user_ids[h], user_ids[i+1]
        return (i+1)

def quickSort(user_ids, l, h):
        global num_calls
        num_calls = num_calls + 1
        if l < h:
                pi = partition(user_ids, l, h)
                quickSort(user_ids, l, pi-1)
                quickSort(user_ids, pi+1, h)


if __name__ == "__main__":
        user_ids = []
        user_id = input()
        while (user_id != "-1"):
                user_ids.append(user_id)
                user_id = input()
        quickSort(user_ids, 0, len(user_ids) - 1)
        print(num_calls)
        for user_id in user_ids:
                print(user_id),