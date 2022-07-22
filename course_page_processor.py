from bs4 import BeautifulSoup

from connector import Connector


class CoursePageProcessor:
    def __init__(self, connector: Connector, course_link: str):
        self.connector = connector
        self.course_link = course_link
        page_html = self.connector.session.get(course_link).text
        self.course_page_soup = BeautifulSoup(page_html, "lxml")

    def get_topic_tags(self) -> dict:
        topics = self.course_page_soup.find_all("ul", class_="ctopics")
        other_topics = topics[1].find_all("li", recursive=False)
        other_names = [topic.find("h3", class_="sectionname").text for topic in other_topics]
        try:
            first_topic = topics[0].find("li", id="section-0")
            first_name = topics[0].find("h3", class_="section-title").text
            names = [first_name] + other_names
            topics = [first_topic] + other_topics
        except Exception:
            names = other_names
            topics = other_topics

        return {
            names[i]: topics[i]
            for i in range(len(topics))
        }