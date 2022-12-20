import csv
from db import MongoFunc


def run():
    mongodb = MongoFunc()
    with open('51job.csv', 'w+', newline='') as f:
        # 表头，需要与下面字典Key值对应
        csv_header = ['link', 'job', 'company', 'salary', 'area', 'experience', 'education', 'companytype', 'direction']
        csv_writer = csv.DictWriter(f, csv_header)
        # 表头写入
        csv_writer.writeheader()
        for data in mongodb.json_c.find():
            job_list = data['jobs']
            for job in job_list:
                data_dict = {
                    'link': job['job_href'],
                    'job': job['job_name'],
                    'company': job['company_name'],
                    'salary': job['providesalary_text'],
                    'area': job['workarea_text'],
                    'experience': '',
                    'education': '',
                    'companytype': job['companytype_text'],
                    'direction': job['companyind_text'],
                }
                if len(job['attribute_text']) < 2:
                    data_dict['experience'] = '无经验要求'
                else:
                    data_dict['experience'] = job['attribute_text'][1]

                if len(job['attribute_text']) < 3:
                    data_dict['education'] = '无学历要求'
                else:
                    data_dict['education'] = job['attribute_text'][-1]
                csv_writer.writerow(data_dict)
        print('ALL DONE')


if __name__ == '__main__':
    run()
