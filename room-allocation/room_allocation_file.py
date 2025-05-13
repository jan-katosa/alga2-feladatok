# CSES - Room Allocation

MIN_CUSTOMERS = 1
MAX_CUSTOMERS = 200000

MIN_TIME = 1
MAX_TIME = 1000000000

def main(filename):
    with open(file=filename, mode="r") as FILE:
        row = FILE.readline()                                   # beolvassuk az első sort
        customer_count = row                                    # az első sorban lesz a vásárlók száma
        assert MIN_CUSTOMERS <= customer_count <= MAX_CUSTOMERS
        guests = []                                             # tömbben tároljuk le a vendégek érkezéseit

        while row:
            row = FILE.readline()                               # beolvassuk a következő sort
            if row is not "":
                row = row.strip().split()
                assert MIN_TIME <= row[0] <= row[1]
                assert row[1] <= MAX_TIME
                stay = {"arrival": row[0], "departure": row[1]}     # egy dictben tároljuk le az érkezési és távozási időket
                guests.append(stay)





        FILE.close()
            




if __name__ == "__main__":
    main()