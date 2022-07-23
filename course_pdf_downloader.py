import os

from connector import Connector
from course_link_finder import CourseLinkFinder
from course_page_processor import CoursePageProcessor


class CoursePDFDownloader:
    def __init__(self, connector: Connector):
        self.connector = connector
        self.course_link_finder = CourseLinkFinder(self.connector)

    def replace_all_slashes(self, string: str):
        return string.replace("/", "-")

    def download_pdf(self, folder_name: str, file_name: str, pdf_url: str):
        real_name = self.replace_all_slashes(file_name)
        full_name = os.path.join(folder_name, real_name)
        print(f"Trying to download <<{full_name}>>.")
        with open(full_name, "wb") as f:
            f.write(
                self.connector.session.get(pdf_url).content
            )
        print(f"Finished downloading <<{full_name}>>.")

    def find_name_and_link_by_tag(self, tag):
        subtags = [tag for tag in tag.find_all("a", class_="aalink") if "mod/resource" in tag["href"]]
        names_and_links = {
            subtag.span.text: subtag["href"]
            for subtag in subtags
        }
        return names_and_links

    def create_folder(self, parent_folder_name: str, folder_name: str, number_of_files: int):
        if number_of_files == 0:
            return
        folder_path = os.path.join(parent_folder_name, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        return folder_path

    def create_main_folder(self, folder_name: str):
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

    def download_by_course_id(self, course_id: str):
        course_link = self.course_link_finder.get_course_link_by_course_id(course_id)

        course_page_processor = CoursePageProcessor(self.connector, course_link)
        names_and_topics = course_page_processor.get_topic_tags()
        self.create_main_folder(course_id)
        for (name, topic) in names_and_topics.items():
            names_and_links = self.find_name_and_link_by_tag(topic)
            folder_path = self.create_folder(course_id, name, len(names_and_links))
            for (file_name, link) in names_and_links.items():
                self.download_pdf(folder_path, file_name[:-5] + ".pdf", link)
                print()

        print("Done!")

    def download_all_courses(self):
        course_list = self.course_link_finder.get_course_list()
        for course in course_list:
            self.download_by_course_id(course)
            print()
        print("All done!")

    def download(self):
        course_list = self.course_link_finder.get_course_list()
        print("All courses:")
        for i in range(1, len(course_list) + 1):
            print(f"{i}\t{course_list[i - 1]}")
        print(f"{len(course_list) + 1}\tDownload all courses above")
        choice = int(input("Please enter a choice:\n")) - 1

        if choice == len(course_list):
            self.download_all_courses()
        else:
            self.download_by_course_id(course_list[choice])