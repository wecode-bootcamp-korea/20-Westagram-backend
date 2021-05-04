class DuplicatedEntryError(Exception):

    def __init__(self, duplicated_field):
        super().__init__()
        self.err_message = f'Entry {duplicated_field} is duplicated.'

def check_duplicate(model, data):
    non_duplicatable_fields = [
        _.attname
        for _ in model._meta.get_fields()
        if _.unique == True
    ]

    for field in non_duplicatable_fields:
        if field in data.keys():
            field_to_check = {field: data[field]}
            if model.objects.filter(**field_to_check).exists():
                raise DuplicatedEntryError(field)

