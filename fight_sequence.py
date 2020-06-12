def main():
    response1 = input('Did you have a fight? Say yes/no: ')
    response2 = input('Who started the fight?Say I or husband: ')
    if response1 == 'yes':
        fight_situation_mom(response1, response2)





def fight_situation_mom(response1, response2):
    days = 3
    gossiped = 0
    isolated = 0
    for i in range(days):
        cried = 1
        gossiped += cried
        isolated += cried
        #days += days
        #print(days)
    print('The fight was started by my '+ response2)

    print('I cried '+ str(cried) + ' time today')
    print('I gossiped ' + str(gossiped)+ ' times')
    print("I have avoided my husband for close to " + str(isolated) + ' days now')


if __name__ == '__main__':
    main()