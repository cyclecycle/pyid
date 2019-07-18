import uuid


def idfy(obj):
    superclass = obj.__class__
    classname = superclass.__name__
    id_class = type(
        classname,
        (superclass,),
        {
            'id': uuid.uuid4(),
        }
    )
    id_obj = id_class(obj)
    return id_obj
