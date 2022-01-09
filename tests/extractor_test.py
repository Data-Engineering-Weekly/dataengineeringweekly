from publisher.extractor import Extractor


def test_to_json():
    extractor = Extractor()
    print(extractor.extract_weekly(36))
    # print(extractor.to_json(36))
