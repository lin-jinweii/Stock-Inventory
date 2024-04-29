# Lin Jin Wei 193123P BF1901

from tabulate import tabulate
import matplotlib.pyplot as plt

revenue_money = []
revenue_code = []
revenue_quantity = []
countingR = []
countingsR = []

thrownaway_money = []
thrownaway_code = []
thrownaway_quantity = []
countingT = []
countingsT = []

buying_money = []
buying_code = []
buying_quantity = []
countingB = []
countingsB = []

item_money = []
item_code = []
item_quantity = []
countingI = []
countingsI = []

remove_money  = []
remove_code = []
remove_quantity = []
countingRe = []
countingsRe = []
reasons = []

profiting = [0]
profitcount = []
profitcounting = [0]

expensing = [0]
expensecount = []
expensecounting = [0]


while True:
    file = open('inventory.txt', 'r+')
    lines = file.readlines()
    print('Welcome to LJW Stock Inventory, select the following options to continue:')
    print('1. Add/Remove Items from Stock Inventory')
    print('2. Add/Remove Quantity of Items from Stock Inventory')
    print('3. Display Items from Stock Inventory')
    print('4. Sort Item Price/Item Stock Level')
    print('5. Search For Item Code using Binary Search')
    print('6. Print Out Inventory Statistical Report (Including Total & Average Stock Level)')
    print('7. Print Out Inventory Graphical Report')
    print('0. Exit Program')
    option = input('Please choose your option: ')



    def add_items():
        count = 0
        while True:
            barcodes = []
            for line in lines:
                barcode, types, description, price, stocklevel = line.split(',')
                barcodes.append(barcode)
            item_barcode = input('Enter Item Code (3 digits): ')
            if item_barcode == 'Q' or item_barcode == 'q':
                return
            elif item_barcode in barcodes:
                print('Item Code Already Existed. Please Choose Another One.')
            elif item_barcode.isdigit() and len(item_barcode) == 3:
                break
            else:
                print('Invalid Code Number. Please Try Again.')
                continue

        while True:
            item_type = input('Enter Item Type: ')
            if item_type == 'Q' or item_type == 'q':
                return
            elif len(item_type) > 0 and (x.isalpha() or x.isspace() for x in item_type):
                break
            else:
                print('Invalid Item Type. Please Try Again')
                continue

        while True:
            item_description = input('Enter Item Description: ')
            if item_description == 'Q' or item_description == 'q':
                return
            elif len(item_description) > 0 and (x.isalpha() or x.isspace() for x in item_description):
                break
            else:
                print('Please Enter the Description/Invalid Description')

        while True:
            item_costprice = input('Enter Item Cost Price: ')
            if item_costprice == 'Q' or item_costprice == 'q':
                return
            else:
                try:
                    item_costprice = float(item_costprice)
                    item_costprice = float(item_costprice)/100 * 120
                    item_costprice = round(item_costprice, 2)
                    print('The Item Selling Price will be ${0:.2f}'.format(item_costprice))
                    break
                except ValueError:
                    print('Invalid Price. Please Try Again')
                    continue

        while True:
            item_stocklevel = input('Enter Item Stock Level: ')
            if item_stocklevel == 'Q' or item_stocklevel == 'q':
                return
            elif item_stocklevel.isdigit():
                item_stocklevel = int(item_stocklevel)
                if item_stocklevel <= 0:
                    print('Stock Level must be more than 0')
                    continue
                else:
                    break
            else:
                print('Invalid Item Stock Level. Please Try Again')

        item_list = str(item_barcode+','+item_type+','+item_description+','+str(item_costprice)+','+str(item_stocklevel))
        file = open('inventory.txt', 'r+')
        file.truncate(0)
        for line in lines:
            file.write(line)
        file.write(item_list + '\n')
        print('Item code ' + str(item_barcode) + ' has been successfully stored.')
        print()
        item_code.append(item_barcode)
        item_money.append(int(item_stocklevel) * float(item_costprice))
        item_quantity.append(item_stocklevel)
        count += 1
        countingI.append(count)
        countingsI.append(len(countingI))




    def remove_items():
        barcodes = []
        for line in lines:
            barcode, types, description, price, stocklevel = line.split(',')
            barcodes.append(barcode)
        print('Press Q to return Main Menu')

        while True:
            remove_qns = input('Enter Item Code: ')
            if remove_qns == 'Q' or remove_qns == 'q':
                return
            elif remove_qns not in barcodes:
                print('No Such Item Code')
                continue
            else:
                while True:
                    areyousure = input('Are you sure you want to remove the item? (Y/N): ')
                    if areyousure == 'Q' or areyousure == 'q':
                        return
                    elif areyousure == 'Y' or areyousure == 'y':
                        count = 0
                        while True:
                            reason = input('Reason To Remove Item: ')
                            if reason == 'Q' or reason == 'q':
                                return
                            elif len(reason) > 0 and (x.isalpha() or x.isspace() for x in reason):
                                for i in range(len(lines)):
                                    if lines[i].split(',')[0] == remove_qns:
                                        code, type, description, price, stocklevel = lines[i].split(',')
                                        remove_code.append(remove_qns)
                                        remove_amount = float(price) * int(stocklevel)
                                        remove_money.append(remove_amount)
                                        remove_quantity.append(stocklevel)
                                        count += 1
                                        countingRe.append(count)
                                        countingsRe.append(len(countingRe))
                                        reasons.append(reason)
                                        lines[i] = ''

                                        file = open('inventory.txt', 'r+')
                                        file.truncate(0)

                                        for line in lines:
                                            file.write(line)
                                        print('Item code ' + str(remove_qns) + ' has been successfully removed.')
                                        print()
                                        profit1 = profiting[-1]
                                        profit = float(profit1) - (float(price) * int(stocklevel))
                                        profiting.append(profit)
                                        count += 1
                                        profitcount.append(count)
                                        profitcounting.append(len(profitcount))
                                        break
                                break
                            else:
                                print('Please Enter A Reason')
                                continue
                        break
                    elif areyousure == 'N' or areyousure == 'n':
                        print('Item code ' + str(remove_qns) + ' has failed to be removed.')
                        print()
                        break
                    else:
                        print('Please Enter Y or N')
                        continue
                break




    def addorremove_quantity():
        print('Press Q to return to main menu')
        barcodes = []
        for line in lines:
            barcode, types, description, price, stocklevel = line.split(',')
            barcodes.append(barcode)

        while True:
            remove_qns = input('Enter Item Code: ')
            if remove_qns == 'Q' or remove_qns == 'q':
                return
            elif remove_qns not in barcodes:
                print('No Such Item Code')
                continue
            else:
                while True:
                    add_or_remove = input('Do you want to Add (A) or Remove (R) Quantity?: ')
                    if add_or_remove == 'Q' or add_or_remove == 'q':
                        return
                    elif add_or_remove == 'A' or add_or_remove == 'a':
                        count = 0
                        while True:
                            quantity = input('What is the quantity needed to add?: ')
                            if quantity.isdigit():
                                for i in range(len(lines)):
                                    if lines[i].split(',')[0] == remove_qns:
                                        code, type, description, price, stocklevel = lines[i].split(',')
                                        money_earned = int(quantity) * float(price)
                                        buying_money.append(money_earned)
                                        buying_code.append(code)
                                        count = count + 1
                                        countingB.append(count)
                                        countingsB.append(len(countingB))
                                        buying_quantity.append(quantity)
                                        stocklevel = int(stocklevel) + int(quantity)
                                        lines[i] = ','.join([code, type, description, price, str(stocklevel) + '\n'])

                                        file.seek(0)
                                        for line in lines:
                                            file.write(line)
                                        print(str(quantity) + ' of ' + str(description) + ' has been successfully added')
                                        print()
                                        break
                            else:
                                print('Please Enter A Digit for Quantity')
                                continue
                            break
                        break
                    elif add_or_remove == 'R' or add_or_remove == 'r':
                        while True:
                            throw_or_sell = input('Sales(S) or Throw Away(T)?: ')
                            if throw_or_sell == 'Q' or throw_or_sell == 'q':
                                return
                            elif throw_or_sell == 'S' or throw_or_sell == 's':
                                count = 0
                                while True:
                                    quantity = input('What is the quantity needed to remove?: ')
                                    if quantity.isdigit():
                                        for i in range(len(lines)):
                                            if lines[i].split(',')[0] == remove_qns:
                                                if int(quantity) < int(lines[i].split(',')[4]):
                                                    code, type, description, price, stocklevel = lines[i].split(',')
                                                    money_earned = int(quantity) * float(price)
                                                    revenue_money.append(money_earned)
                                                    revenue_code.append(code)
                                                    count = count + 1
                                                    countingR.append(count)
                                                    countingsR.append(len(countingR))
                                                    revenue_quantity.append(quantity)
                                                    stocklevel = int(stocklevel) - int(quantity)
                                                    lines[i] = ','.join([code, type, description, price, str(stocklevel) + '\n'])

                                                    file.seek(0)
                                                    for line in lines:
                                                        file.write(line)
                                                    print(str(quantity) + ' ' + str(description) + 's have been successfully sold')
                                                    print()
                                                    profit1 = profiting[-1]
                                                    profit = float(profit1) + (float(price) * int(quantity))
                                                    profiting.append(profit)
                                                    count += 1
                                                    profitcount.append(count)
                                                    profitcounting.append(len(profitcount))
                                                    break

                                                else:
                                                    print('Quantity needed to remove is too high')
                                                    break
                                    else:
                                        print('Please enter a digit for quantity')
                                        continue
                                    break
                                break
                            elif throw_or_sell == 'T' or throw_or_sell == 't':
                                count = 0
                                while True:
                                    quantity = input('What is the quantity needed to remove?: ')
                                    if quantity.isdigit():
                                        for i in range(len(lines)):
                                            if lines[i].split(',')[0] == remove_qns:
                                                if quantity.isdigit() and int(quantity) < int(lines[i].split(',')[4]):
                                                    code, type, description, price, stocklevel = lines[i].split(',')
                                                    money_earned = int(quantity) * float(price)
                                                    thrownaway_money.append(money_earned)
                                                    thrownaway_code.append(code)
                                                    count = count + 1
                                                    countingT.append(count)
                                                    countingsT.append(len(countingT))
                                                    thrownaway_quantity.append(quantity)
                                                    stocklevel = int(stocklevel) - int(quantity)
                                                    lines[i] = ','.join([code, type, description, price, str(stocklevel) + '\n'])

                                                    file.seek(0)
                                                    for line in lines:
                                                        file.write(line)
                                                    print(str(quantity) + ' ' + str(description) + 's have been successfully thrown')
                                                    print()
                                                    profit1 = profiting[-1]
                                                    profit = float(profit1) - (float(price) * int(quantity))
                                                    profiting.append(profit)
                                                    count += 1
                                                    profitcount.append(count)
                                                    profitcounting.append(len(profitcount))
                                                    break

                                                else:
                                                    print('Quantity needed to remove is too high')
                                                    break
                                    else:
                                        print('Please enter a digit for quantity')
                                        continue
                                    break
                                break
                            else:
                                print('Please enter S for Sale and T for Throw Away')
                                continue
                        break
                    else:
                        print('Please enter A to add or R to remove quantity of items')
                        continue
                break




    def display_items():
        a_file = open('inventory.txt', 'r')
        lists = []
        for line in a_file:
            stripped_line = line.strip()
            line_list = stripped_line.split(',')
            lists.append(line_list)
        a_file.close()

        headers = ['Item Code', 'Type', 'Description', 'Price', 'Stock Level']
        print(tabulate(lists, headers=headers))




    def optimized_bubbleSort(lists):
        while True:
            aord = input('Do you want to sort in Ascending(A) or Descending(D) order?: ')
            if aord == 'A' or aord == 'a':
                n = len(lists)
                for i in range(n-1, 0, -1):
                    noSwap = True
                    for j in range(i):
                        if float(lists[j][3]) > float(lists[j+1][3]):
                            tmp = lists[j]
                            lists[j] = lists[j+1]
                            lists[j + 1] = tmp
                            noSwap = False
                    if noSwap:
                        break

                headers = ['Item Code', 'Type', 'Description', 'Price', 'Stock Level']
                print(tabulate(lists, headers=headers))
                print('')
                break

            elif aord == 'D' or aord == 'd':
                n = len(lists)
                for i in range(n-1, 0, -1):
                    noSwap = True
                    for j in range(i):
                        if float(lists[j][3]) < float(lists[j+1][3]):
                            tmp = lists[j]
                            lists[j] = lists[j+1]
                            lists[j + 1] = tmp
                            noSwap = False
                    if noSwap:
                        break

                headers = ['Item Code', 'Type', 'Description', 'Price', 'Stock Level']
                print(tabulate(lists, headers=headers))
                print('')
                break

            else:
                print('Please Enter A for Ascending or D for Descending')
                continue



    def insertionSort(lists):
        while True:
            aord = input('Do you want to sort in Ascending(A) or Descending(D) order?: ')
            if aord == 'A' or aord == 'a':
                n = len(lists)
                for i in range(1, n):
                    value = lists[i]
                    pos = i
                    while pos > 0 and int(value[4]) < int(lists[pos - 1][4]):
                        lists[pos] = lists[pos - 1]
                        pos -= 1
                    lists[pos] = value

                headers = ['Item Code', 'Type', 'Description', 'Price', 'Stock Level']
                print(tabulate(lists, headers=headers))
                print('')
                break
            elif aord == 'D' or aord == 'd':
                n = len(lists)
                for i in range(1, n):
                    value = lists[i]
                    pos = i
                    while pos > 0 and int(value[4]) > int(lists[pos - 1][4]):
                        lists[pos] = lists[pos - 1]
                        pos -= 1
                    lists[pos] = value
                headers = ['Item Code', 'Type', 'Description', 'Price', 'Stock Level']
                print(tabulate(lists, headers=headers))
                print('')
                break
            else:
                print('Please enter A for Ascending or D for Descending')
                continue



    def insertionSort1(lists):
        n = len(lists)
        for i in range(1, n):
            value = lists[i]
            pos = i
            while pos > 0 and int(value[0]) < int(lists[pos - 1][0]):
                lists[pos] = lists[pos - 1]
                pos -= 1
            lists[pos] = value

        headers = ['Item Code', 'Type', 'Description', 'Price', 'Stock Level']
        print(tabulate(lists, headers=headers))
        print('')



    def binarySearch(theValues, target):
        low = 0
        high = len(theValues) - 1
        while low <= high:
            mid = (high + low) // 2
            if int(theValues[mid][0]) == int(target):
                first_occurrence = mid
                cont = True
                while first_occurrence > 0 and cont:
                    if theValues[first_occurrence - 1] == target:
                        first_occurrence -= 1
                    else:
                        cont = False
                return first_occurrence
            elif int(target) < int(theValues[mid][0]):
                high = mid - 1
            else:
                low = mid + 1
        return -1



    def statistical_report():
        a_file = open('inventory.txt', 'r')
        listings = []
        for line in a_file:
            stripped_line = line.strip()
            line_list = stripped_line.split(',')
            listings.append(line_list)
        a_file.close()

        headers = ['Item Code', 'Type', 'Description', 'Price', 'Stock Level']
        print(tabulate(listings, headers=headers))

        print('')
        print('Please Wait while the Store is Processing......')
        print('')
        import time
        time.sleep(3)

        a_file = open('inventory.txt', 'r')
        cost = []
        for line in a_file:
            stripped_line = line.strip()
            line_list = stripped_line.split(',')
            cost.append(int(line_list[4]) * float(line_list[3]))
        total_cost = 0
        for i in cost:
            total_cost = total_cost + i
        print('The Total Potential Cost In The Inventory is ${0:.2f}'.format(float(total_cost)))
        profits = total_cost/100 * 20
        print('The Total Potential Profit In The Inventory is ${0:.2f}'.format(float(profits)))
        a_file = open('inventory.txt', 'r')
        lists = []
        for line in a_file:
            stripped_line = line.strip()
            line_list = stripped_line.split(',')
            lists.append(line_list[4])
        total = 0
        for i in lists:
            i = int(i)
            total += i
        print('The Total Stock Item Level (For All Items) is ' + str(total))
        number = len(lists)
        average = total/number
        average = int(average)
        print('The Average Stock Item Level is ' + str(average))
        print('')
        print('LOADING.........................')
        time.sleep(3)
        print('')
        new_list = [list(x) for x in zip(countingsR, revenue_code, revenue_quantity, revenue_money)]
        print('Revenue(Sales)')
        headers = ['No.', 'Item Code', 'Quantity', 'Revenue Earned($)']
        print(tabulate(new_list, headers=headers))
        print('')
        new_list1 = [list(x) for x in zip(countingsT, thrownaway_code, thrownaway_quantity, thrownaway_money)]
        print('Wasted(Thrown Away)')
        headers1 = ['No.', 'Item Code', 'Quantity', 'Amount Loss($)']
        print(tabulate(new_list1, headers=headers1))
        print('')
        new_list3 = [list(x) for x in zip(countingsB, buying_code, buying_quantity, buying_money)]
        print('Restocked(Added Quantity In Store)')
        headers3 = ['No.', 'Item Code', 'Quantity', 'Amount Spent($)']
        print(tabulate(new_list3, headers=headers3))
        print('')
        new_list4 = [list(x) for x in zip(countingsI, item_code, item_quantity, item_money)]
        print('New Items Added')
        headers4 = ['No.', 'Item Code', 'Quantity', 'Amount Spent($)']
        print(tabulate(new_list4, headers=headers4))
        print('')
        new_list5 = [list(x) for x in zip(countingsRe, remove_code, remove_quantity, remove_money, reasons)]
        print('Items Removed')
        headers5 = ['No.', 'Item Code', 'Quantity', 'Amount Removed($)', 'Reason']
        print(tabulate(new_list5, headers=headers5))
        print('')
        revenue = sum(revenue_money)
        print('The Total Revenue (Sales) Earned Today is ${0:.2f}'.format(float(revenue)))
        loss = sum(thrownaway_money)
        print('The Total Amount Loss (Wasted) Today is ${0:.2f}'.format(float(loss)))
        expenses = float(sum(buying_money)) + float(sum(item_money))
        print('The Total Expenses (Restocked + New Items Added) Today is ${0:.2f}'.format(float(expenses)))
        removed_amount = sum(remove_money)
        print('The Total Amount (Removed) Today is ${0:.2f}'.format(float(removed_amount)))
        print('')
        print('CALCULATING PROFIT/LOSS.........................')
        time.sleep(2)
        print('')
        profit = float(revenue) - float(loss) - float(removed_amount)
        expenses = float(expenses)
        if profit > 0:
            print('The Total Profit Today is ${0:.2f}'.format(float(profit)))
        else:
            profit = 0-profit
            print('The Total Loss Today is ${0:.2f}'.format(float(profit)))
        print('The Total Amount Spent Today is ${0:.2f}'.format(expenses) + ' for the Inventory')
        print('')




    def graphical_report():
        company = ['Revenue', 'Thrown', 'Expenses', 'Removed']
        performance = [sum(revenue_money), sum(thrownaway_money), sum(item_money + buying_money), sum(remove_money)]

        plt.subplot(1, 2, 1)
        plt.xlabel('Amount($)')
        plt.title('Overall Performance')
        plt.barh(company, performance)

        plt.subplot(1, 2, 2)
        plt.plot(profitcounting, profiting, label='profit')
        plt.title('Profit/Loss')
        plt.xlabel('Number of Records')
        plt.ylabel('Amount($)')
        plt.legend()

        plt.show()




    if option == '1':
        print()
        print('Press Q to return to main menu')
        while True:
            allow = input('Do you want to Add(A) or Remove(R) items?: ')
            if allow == 'Q' or allow == 'q':
                break
            elif allow == 'A' or allow == 'a':
                add_items()
                break
            elif allow == 'R' or allow == 'r':
                remove_items()
                break
            else:
                print('Please choose A to Add or R to Remove')
                continue

    elif option == '2':
        print()
        addorremove_quantity()
        print()

    elif option == '3':
        print()
        display_items()
        print()

    elif option == '4':
        print()
        print('Press Q to return Main Menu')
        while True:
            question1 = input('Do you want to sort Item Price(P) or Item Stock Level(S)?: ')
            if question1 == 'Q' or question1 == 'q':
                break
            elif question1 == 'P' or question1 == 'p':
                print('Item Price will be sorted via Bubble Sort')
                a_file = open('inventory.txt', 'r')
                lists = []
                for line in a_file:
                    stripped_line = line.strip()
                    line_list = stripped_line.split(',')
                    lists.append(line_list)
                optimized_bubbleSort(lists)
                break
            elif question1 == 'S' or question1 == 's':
                print('Item Stock Level will be sorted via Insertion Sort')
                a_file = open('inventory.txt', 'r')
                lists = []
                for line in a_file:
                    stripped_line = line.strip()
                    line_list = stripped_line.split(',')
                    lists.append(line_list)
                insertionSort(lists)
                break
            else:
                print('Please choose P for Item Price and S for Item Stock Level')
                continue

    elif option == '5':
        print()
        a_file = open('inventory.txt', 'r')
        lists = []
        for line in a_file:
            stripped_line = line.strip()
            line_list = stripped_line.split(',')
            lists.append(line_list)
        insertionSort1(lists)
        print('Press Q to return Main Menu')
        while True:
            question = input('What is the code number?: ')
            if question == 'Q' or question == 'q':
                break
            elif question.isdigit():
                whichnumber = binarySearch(lists, question)
                if whichnumber != -1:
                    listing = [lists[whichnumber]]
                    headers = ['Item Code', 'Type', 'Description', 'Price', 'Stock Level']
                    print(tabulate(listing, headers=headers))
                    print('')
                else:
                    print('Item Cannot Be Found')
                    print('')
                    continue
                break
            else:
                print('Invalid Item Code')
                continue

    elif option == '6':
        print()
        statistical_report()

    elif option == '7':
        print()
        graphical_report()

    elif option == '0':
        exit()

    else:
        print()
        print('Invalid Option. Please Try Again')

