class Storage:
    def __init__(self):
        self.categories = list()
        self.topics = list()
        self.documents = list()

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        cat = [c for c in self.categories if c.id == category_id][0]
        cat.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        top = [t for t in self.topics if t.id == topic_id][0]
        top.topic = new_topic
        top.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        doc = [d for d in self.documents if d.id == document_id][0]
        doc.id = document_id
        doc.file_name = new_file_name

    def delete_category(self, category_id: int):
        cat = [c for c in self.categories if c.id == category_id][0]
        if cat in self.categories:
            self.categories.remove(cat)

    def delete_topic(self, topic_id: int):
        top = [t for t in self.topics if t.id == topic_id][0]
        if top in self.topics:
            self.topics.remove(top)

    def delete_document(self, document_id: int):
        doc = [d for d in self.documents if d.id == document_id][0]
        if doc in self.documents:
            self.documents.remove(doc)

    def get_document(self, document_id: int):
        return [d for d in self.documents if d.id == document_id][0]

    def __repr__(self):
        return '\n'.join(d.__repr__() for d in self.documents)
