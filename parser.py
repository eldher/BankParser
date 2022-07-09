# Code to format table from Scotiabanks Panama site
# Made to be sent to excel


# TO-DO
# copy to clipboard into excel format
# add description for expense type
# extract from clipboard


#filename = "C:/Users/eld02/Documents/4.coding_python/banking_parser/202206_scotia.txt"
filename = "C:/Users/eld02/Documents/4.coding_python/banking_parser/202206_cta_corriente.txt"


with open(filename,  encoding='utf8') as f:
    lines = f.readlines()


converted_list = []

for line in lines:
    converted_list.append(line.strip())

print(converted_list)

# date_and_description = ""    
# txn_type = ""
# amount = ""
# txn_list = []



def txnCC(converted_list):


    date_and_description = ""    
    txn_type = ""
    amount = ""
    txn_list = []



    for i in range(0, len(converted_list)):

        # calculated mod of item #id
        match i%4:
            # if 0 is month and day
            case 0:
                date_and_description = date_and_description + converted_list[i] + ' '
            # if 1 is year and description
            case 1:
                date_and_description = date_and_description + converted_list[i]
            # type of transaction
            case 2:
                txn_type = converted_list[i]
            # if last entry, format amount to float 
            # 
            case 3:
                # add to skip data conversion
                try:
                    amount = float(1*(converted_list[i].replace("$ ","")))
                except:
                    amount = converted_list[i]

                # split date and description from field
                date = date_and_description.split("\t")[0]
                txn = date_and_description.split("\t")[1]

                # append to final txn list
                txn_list.append([date, txn , txn_type ,  amount])
                
                # reset fields
                date_and_description = ""    
                txn_type = ""
                amount = ""

        
    for item in txn_list:
        print(item)
    
    return(txn_list)


def txnCTA(converted_list):



    date_and_description = ""    
    amount = ""
    txn_list = []



    for i in range(0, len(converted_list)):

        # calculated mod of item #id
        match i%3:
            # if 0 is month and day
            case 0:

                date_and_description = date_and_description + converted_list[i].replace(",","") + ' '

            # if 1 is year and description
            case 1:
                date_and_description = date_and_description + converted_list[i]
            # type of transaction
            case 2:
                # add to skip data conversion
                try:
                    converted_list[i] = converted_list[i].replace("$","")
                    converted_list[i] = converted_list[i].replace(" USD","")
                    converted_list[i] = converted_list[i].replace(",","")
                    amount = float(converted_list[i])
                except:
                    amount = converted_list[i]

                # split date and description from field
                date = date_and_description.split("\t")[0]
                txn = date_and_description.split("\t")[1]

                white = " "
                # append to final txn list
                txn_list.append([date, txn , white,  amount])
                
                # reset fields
                date_and_description = ""    
                amount = ""

        
    for item in txn_list:
        print(item)
    return(txn_list)


    

#txnCC(converted_list)
txnCTA(converted_list)

# myVar = "Hello World"
# print(myVar)
# print(4+4)


# list = [1,2,3,4,5,6]

# for item in list:
#     print(item)


# [print(i>4) for i in range(5)]

    # if i 
    # entry = ""
    # for j in range(4):
    #     entry = entry + 



    #converted_list.append(line.replace("\n",""))

# i=0
# for line in lines:
#     i = i + 1
#     print(i)
#     print(line.replace("\n",""))





# print(type(lines))
# print(converted_list)