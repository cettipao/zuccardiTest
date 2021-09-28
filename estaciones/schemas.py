
def Estacion30300Entity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "date": item["date"],
        "humedad": item["humedad"],
        "temperatura": item["temperatura"],
    }


def Estacion30300Entities(entity) -> list:
    return [Estacion30300Entity(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}


def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]