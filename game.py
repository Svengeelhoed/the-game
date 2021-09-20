print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Welcome to Dee's nuts!")
print("In this game you will be working as an employee for Dee's nuts, a street food vendor!")
print("The goal of this game is to help customers and prepare the food they order! The customers will pay you in Nuts, the local currency!")
print("Commands:")
print("<....> bun.  plain, sesame, sliced ")
print("<....> type.  salad, pizza, sandwich")
print("<....> topping.  ham, cheese, butter")
print("accept / decline")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
offer = input("There is a customer wanting to order something! Will you accept the offer? ")
if offer == "accept"or "yes":
    print("")
    print("Hey! I just arrived in this city yesterday, and I like the name of this stand! ")
    order = print("anyways, here's my order: plain buns with butter and cheese! ")
    print("type <take> to take the ingredients and <place> to use them. ")
    take = input()
    if take == "take bun":
        print("you took the bun from the storage.")
        takeplace = input()
        if takeplace == "place bun":
            print("you placed the bun on the counter")
            takeplace1 = input()
            if takeplace1 == "take butter":
                print("you took the butter out of the fridge.")
                takeplace2 = input()
                if takeplace2 == "place butter":
                    print("you placed the butter ")
                    takeplace3 = input()
                    if takeplace3 == "take cheese":
                        print("you took the cheese from the fridge")
                        takeplace4 = input()
                        if takeplace4 == "place cheese":
                            print("you placed the cheese on the butter.")
                            takeplace5 = input()
                            if takeplace5 == "take bun":
                                print("you took the bun from the storage.")
                                takeplace6 = input()
                                if takeplace6 == ("place bun"):
                                    print("you placed the bun on top of the cheese. your order is now done! type <accept> to complete the order.")
                                    ordercomp = input()
                                    if ordercomp == "accept":
                                        if take != "take bun" or takeplace != "place bun" or takeplace1 != "take butter" or takeplace2 != "place butter" or takeplace3 != "take cheese" or takeplace4 != "place cheese" or takeplace5 != "take bun" or takeplace6 != "place bun":
                                                print("You made the worst burger ever created and the customer cries and runs away. you lost.")
                                                print("*You acquired: 0 nuts*")
                                        else: print("Thanks for the burger!")
                                        print("You acquired: 5 nuts")
                                else: print("you ruined the burger. get fucked")
                            else: print("you ruined the burger. get fucked")
                        else: print("you ruined the burger. get fucked")
                    else: print("you ruined the burger. get fucked")
                else: print("you ruined the burger. get fucked")
            else: print("you ruined the burger. get fucked")
        else: print("you ruined the burger. get fucked")
    else: print("you ruined the burger. get fucked")
else: print("you declined the offer. the customer runs away crying. It was the only customer that approached your stand in 5 days.")
                            
                            
                                        
