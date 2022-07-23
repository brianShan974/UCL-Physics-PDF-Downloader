from connector import Connector
import re


class CourseLinkFinder:
    def __init__(self, connector: Connector):
        self.connector = connector
        soup = self.connector.post_login_soup
        course_tags = [
            tag
            for tag in soup.find_all(
                "a", class_="list-group-item list-group-item-action"
            )
            if self.is_valid_course_name(tag.text)
        ]
        self.course_dict = {tag.text[:8]: tag["href"] for tag in course_tags}

    def is_valid_course_name(self, name: str):
        course_pattern = re.compile("\w{4}\d{4}")
        return course_pattern.match(name) is not None

    def get_course_link_by_course_id(self, course_id: str):
        return self.course_dict[course_id]

    def get_course_list(self):
        return [key for key in self.course_dict]
