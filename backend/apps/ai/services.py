from .parsers.factory import ParserFactory


class ResumeParserService:

    @staticmethod
    def extract_text(file):
        parser = ParserFactory.get_parser(file)

        return parser.extract_text(file)

    @staticmethod
    def process_application(application):
        text = ResumeParserService.extract_text(
            application.resume
        )

        application.resume_text = text
        application.save(
            update_fields=["resume_text"]
        )

        return application