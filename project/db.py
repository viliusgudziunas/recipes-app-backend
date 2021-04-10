from project.extensions import db


def delete_data(data):
    db.session.delete(data)
    commit_db_changes()


def save_changes(data):
    db.session.add(data)
    commit_db_changes()


def commit_db_changes():
    db.session.commit()
