import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():
    def csv_file(path):
        report_file = []
        with open(path) as file:
            reports = csv.DictReader(file, delimiter=",", quotechar='"')
            for report in reports:
                report_file.append(report)
        file.close()
        return report_file

    def json_file(path):
        with open(path) as file:
            report_file = json.load(file)
        file.close()
        return report_file

    def xml_file(path):
        report_file = []
        with open(path) as file:
            reports = xmltodict.parse(file.read())["dataset"]["record"]
            for report in reports:
                report_file.append(report)
        file.close()
        return report_file

    @classmethod
    def import_data(cls, path, type):
        data = []
        if ".csv" in path:
            data = cls.csv_file(path)
        if ".json" in path:
            data = cls.json_file(path)
        if ".xml" in path:
            data = cls.xml_file(path)
        if type == "simples":
            report = SimpleReport.generate(data)
            return report
        else:
            report = CompleteReport.generate(data)
            return report

# Ref: https://docs.python-guide.org/scenarios/xml/
