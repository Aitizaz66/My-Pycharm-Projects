def generate_challan(vehicle_no, violation, discount=0):
    t_fine = 0
    if violation == "no helmet":
        t_fine += 500
    elif violation == "overspeed":
        t_fine += 1000
    elif violation == "signal violation":
        t_fine += 1500
    elif violation == "no seat belt":
        t_fine += 700
    elif violation == "wrong parking":
        t_fine += 800
    else:
        print("Enter valid challan")
    t_fine -= discount
    print("Total Fine : ", t_fine)
    return t_fine


def record_challan(challan_list, vehicle_no, fine, area):
    challan = {
        'Vehicle': vehicle_no,
        'Fine ': fine,
        'Area': area
    }
    challan_list.append(challan)
    for i in challan_list:
        print(i, " : ", challan_list[i])


def repeat_offender(challan_list, vehicle_no, fine):
    for i in challan_list:
        if i['vehicle_no'] == vehicle_no:
            fine += 500
            break
    return fine


def calculate_total_revenue(challans):
    t = 0
    for i in challans:
        t += sum(i['Fine'])
    return t


def officer_record(**details):
    for i in details:
        print(i, " : ", details[i])
    # print(details)


def area_report(challans, area):
    for i in challans:
        if i['Area'] == area:
            print(challans[i])
