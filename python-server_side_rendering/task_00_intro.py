import logging

logging.basicConfig(level=logging.INFO)

def generate_invitations(template, attendees):

    if not isinstance(template, str):
        logging.error("Invalid input: template must be a string.")
        return

    if not isinstance(attendees, list):
        logging.error("Invalid input: attendees must be a list of dictionaries.")
        return

    for item in attendees:
        if not isinstance(item, dict):
            logging.error("Invalid input: attendees must be a list of dictionaries.")
            return

    if template.strip() == "":
        logging.error("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        logging.error("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        content = template
        fields = ["name", "event_title", "event_date", "event_location"]

        for field in fields:
            value = attendee.get(field)
            if value is None or str(value).strip() == "":
                value = "N/A"
            content = content.replace("{" + field + "}", str(value))

        filename = f"output_{index}.txt"

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            logging.info(f"Generated: {filename}")
        except IOError as e:
            logging.error(f"Could not write {filename}: {e}")
