from floripa_chess_hustlers import publisher
from floripa_chess_hustlers.models import Youtube


def test_publisher() -> None:
    video = Youtube(
        title="O Mestre dos Finais arremata mais uma na defesa Philidor",
        description="",
        url="https://www.youtube.com/watch?v=AG2LUGY0Ds0"
    )
    publisher.publish_to_reddit(video)
