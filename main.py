from connector import Connector
from course_pdf_downloader import CoursePDFDownloader


if __name__ == "__main__":
    username = input("Please enter your username:\n")
    password = input("Please enter your password:\n")

    connector = Connector()
    connector.login(username, password)

    pdf_downloader = CoursePDFDownloader(connector)
    pdf_downloader.download()