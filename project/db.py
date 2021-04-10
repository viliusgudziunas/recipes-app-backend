from project.extensions import db


def delete_data(data):
    db.session.delete(data)
    db.session.commit()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
