# CSES - Room Allocation

MIN_CUSTOMERS = 1
MAX_CUSTOMERS = 200000

MIN_TIME = 1
MAX_TIME = 1000000000

def main():
    customer_count = int(input("Vásárlók száma: "))         # az első sorban lesz a vásárlók száma
    assert MIN_CUSTOMERS <= customer_count <= MAX_CUSTOMERS
    
    guests = []                                             # tömbben tároljuk le a vendégek érkezéseit

    for i in range(0,customer_count):
        row = input("Érkezési és távozási idő: ")
        if row is not "":
            row = row.strip().split()
            assert MIN_TIME <= row[0] <= row[1]
            assert row[1] <= MAX_TIME
            stay = {"arrival": int(row[0]), "departure": int(row[1])}     # egy dictben tároljuk le az érkezési és távozási időket
            guests.append(stay)


    # TODO: Nyilván kell tartani, hány szobánk van
    # TODO: Le kell ellenőrizni az előző összes szobát a ciklusban, mielőtt kiadunk egyet
    room_count = 0
    result = ""
    for guest in guests:
        if guests.index(guest) == 0:
            room_count += 1
            previous = guest
            result += "1 "
        
        if previous["departure"] >= guest["arrival"]:
            room_count += 1
        
        previous = guest
        





if __name__ == "__main__":
    main()