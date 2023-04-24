import pynecone as pc

config = pc.Config(
    app_name="my_app_name",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    port=80,
)
