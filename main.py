from connector import Connector
from course_pdf_downloader import CoursePDFDownloader
import getpass

if __name__ == "__main__":
    username = input("Please enter your username: ")
    password = getpass.getpass("Please enter your password: ")

    connector = Connector()
    connector.login(username, password)

    pdf_downloader = CoursePDFDownloader(connector)
    pdf_downloader.download()
