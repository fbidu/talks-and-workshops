data = [
    {"id": 20, "country": "BR", "emails": ["joao@gmail.com", "jota@j.com"]},
    {"id": 22, "country": "br", "emails": ["BIDU@GMAIL.COM"]},
    {"id": 32, "country": "uk", "emails": ["maria@gmail.com"]},
    {"id": 34, "country": "BR", "emails": ["jonas@globo.com"]},
    {"id": 42, "country": "BR", "emails": ["matilde@gmail.com", "MA@gmail.com"]},
]


{
    20: ["joao@gmail.com"],
    22: ["bidu@gmail.com"],
    42: ["matilde@gmail.com", "ma@gmail.com"],
}

{
    k: v
    for k, v in {
        x["id"]: [e.lower() for e in x["emails"] if e.lower().endswith("gmail.com")]
        for x in data
        if x["country"].upper() == "BR"
    }.items()
    if v
}


def extract_brazilian_gmails(data):
    result = {}

    for record in data:
        country = record["country"].lower()

        if country == "br":
            emails = [e.lower() for e in record["emails"]]
            emails = [e for e in emails if e.endswith("gmail.com")]

            if emails:
                result[record["id"]] = emails

    return result


def extract_brazilian_gmails(data):

    def from_brazil(record):
        country = record["country"].lower()
        return country == "br"

    def extract_email(record):

        if not from_brazil(record):
            return None

        emails = [e.lower() for e in record["emails"]]
        emails = [e for e in emails if e.endswith("gmail.com")]
        return emails

    result = {r["id"]: extract_email(r) for r in data if extract_email(r)}

    return result


def emails_by_country(data, country_code="br", provider="gmail"):
    result = {}

    for record in data:
        country = record["country"].lower()

        if country == country_code:
            emails = [e.lower() for e in record["emails"]]
            emails = [e for e in emails if provider in e]

            if emails:
                result[record["id"]] = emails

    return result
