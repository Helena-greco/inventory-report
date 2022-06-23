import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

class Inventory():
    def csv_file(path):
        report_list = []
        with open(path) as file:
            reports = csv.DictReader(file, delimiter=",", quotechar='"')
            for report in reports:
                report_list.append(report)
        file.close()
        return report_list


    @classmethod
    def import_data(cls, path, type):
        data = []
        if ".csv" in path:
            data = cls.csv_file(path)
        if type == "simples":
            report = SimpleReport.generate(data)
            return report
        if type == "completo":
            report = CompleteReport.generate(data)
            return report