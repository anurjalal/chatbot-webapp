from chatterbot import ChatBot


def get_bot():
    nuizia = ChatBot(
        'Example Bot',
        database_uri= 'sqlite:///bot/db.sqlite3',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'I am sorry, but I do not understand.',
                'maximum_similarity_threshold': 0.90
            }
        ]
    )
    return nuizia
