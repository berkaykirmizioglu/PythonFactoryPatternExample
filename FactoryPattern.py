class Report(object):
    url: str = ""


class Facebook(Report):
    url: str = "https://facebook.com/"


class Twitter(Report):
    url: str = "https://twitter.com/"


class Youtube(Report):
    url: str = "https://youtube.com/"


class ReportFactory:
    @staticmethod
    def create_report(report_type: Report):
        return report_type


report = ReportFactory().create_report(Facebook)
print(report.url)
