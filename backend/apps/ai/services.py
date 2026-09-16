from .parsers.factory import ParserFactory
from .extractors.candidate_extractor import CandidateExtractorService
from .ranking.candidate_ranker import CandidateRanker


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


        parsed_data = CandidateExtractorService.extract(
            text
        )


        application.resume_text = text
        application.parsed_data = parsed_data

        application.save(
            update_fields=[
                "resume_text",
                "parsed_data",
            ]
        )


        CandidateRanker.rank_application(
            application
        )

        return application