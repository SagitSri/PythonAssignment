import datetime
from csv import reader, writer, DictReader, DictWriter


new_column_data_dict = {}

def from_dob_to_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def write_csv():
    new_headers = list(new_column_data_dict["1"].keys())
    # print(new_headers)
        
    with open('student.csv',"w+", newline='') as write_obj:
        writer = DictWriter(write_obj, fieldnames=new_headers)
        writer.writeheader()
        for k in new_column_data_dict:
            # print(new_column_data_dict[k])
            writer.writerow(new_column_data_dict[k])

def read_and_manipulate():
    with open('student.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        csv_headers = list(header)
        
        if header != None:
            for row in csv_reader:
                fullname = row[1]+" "+row[2]
                username = row[1][:4] + row[2][-4:]
                age_creteria = ""
                dob = datetime.datetime.strptime(row[4], '%Y-%m-%d')
                age = from_dob_to_age(dob)
                if(age <= 18):
                    age_creteria = "minor"
                elif age > 18 or age < 40:
                    age_creteria = "middle_age"
                elif age > 40:
                    age_creteria = "senior"
                new_column_data_dict[row[0]] = {"stu_id": row[0],"stuf_name": row[1],"stul_name": row[2],"stu_add": row[3],"stu_dob": row[4],"stu_email": row[5],"stu_gender": row[6],
                    "fullname": fullname, "username": username, "stu_age": age,"age_creteria": age_creteria}

read_and_manipulate()
write_csv()