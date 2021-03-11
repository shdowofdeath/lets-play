import string, random ,time , datetime
print('Welcome to stes playing')
print('Elay')
def start_playing() :
    generated_target = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:'
    target = input("Enter your target word text: ")
    start_time  = datetime.datetime.now()
    attempt = ''.join(random.choice(generated_target) for i in range(len(target)))
    completed = False
    generation = 0
    list_try = []

    while completed == False:
        list_try.append(attempt)
        next_try = ''
        completed = True
        for i in range(len(target)):
            if attempt[i] != target[i]:
                completed = False
                next_try += random.choice(generated_target)
            else:
                next_try += target[i]
        generation += 1
        attempt = next_try
    end_time = datetime.datetime.now()
    durration = end_time - start_time
    for item in list_try:
        print(item)
    print("target word matched! That took \n" + str(generation) + " generation(s) , \ntime to generate the Target :" ,durration)
    more = input("click y to run it again ")
    if more == "y":
        start_playing()
start_playing()
