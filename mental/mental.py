import csv

data_path ="./survey.csv"

def run_main():

    male_set = {"male", 'm'}
    female_set = {'female', 'f'}

    result_dict = {}

    with open(data_path,'r', newline='') as csvfile:
        rows = csv.reader(csvfile)

        for i, row in enumerate(rows):
            if i == 0:
                continue
            if i % 50 == 0:
                print("正在加载{}数据.....".format(i))

             # 性别属性
            gender_var = row[2]
            contry_var = row[3]

            gender_var = gender_var.replace(" ", "")
            gender_var = gender_var.lower()

            # 判断国家是否存在
            if contry_var not in result_dict:
                result_dict[contry_var] = [0, 0]
            if gender_var in female_set:
                result_dict[contry_var][0] += 1
            elif gender_var in male_set:
                result_dict[contry_var][1] += 1
            else:
                pass
    with open('gender_country.csv','w', newline="", encoding='utf-16') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["国家", "女", "男"])

        for k, v in list(result_dict.items()):
            csvwriter.writerow([k, v[0], v[1]])













if __name__ == '__main__':

    run_main()
