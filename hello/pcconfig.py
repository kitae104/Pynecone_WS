import pynecone as pc

config = pc.Config(
    app_name="hello",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    port=80,
)
