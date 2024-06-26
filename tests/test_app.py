from github_actions_ci import run


def test_app(capsys):
    run()

    capture = capsys.readouterr()
    assert capture.out == "Hello world!\n"
